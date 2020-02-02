package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"flag"
	"fmt"
	"github.com/Sirupsen/logrus"
	"github.com/mediocregopher/radix.v2/pool"
	"github.com/mgutz/str"
	"io"
	"net/url"
	"os"
	"strconv"
	"strings"
	"time"
)

type cmdParams struct {
	logFilePath string
	routeingNum int
}
type urlData struct {
	data  digdata
	uid   string
	unode urlNode
}
type urlNode struct {
	unType string
	unRid  int
	unUrl  string
	unTime string
}
type digdata struct {
	time  string
	ua    string
	refer string
	url   string
}

type storageBlock struct {
	countType    string
	unode        urlNode
	storageModel string
}

const HANDLE_DIG = " /dig?"
const HANDLE_MOVIE = "/movie/"
const HANDLE_LIST = "/list/"
const HANDLE_HTML = ".html"

var log = logrus.New()

func init() {
	log.Out = os.Stdout
	log.Level = logrus.DebugLevel

}
func main() {
	// 获取参数
	logFilePath := flag.String("logFilePath", "./log.txt", "log file path")
	routeingNum := flag.Int("n", 5, "go routing number")
	l := flag.String("l", "./a.log", "this runtime log for log path")
	flag.Parse()
	params := cmdParams{*logFilePath, *routeingNum}

	// 打日志
	logFd, err := os.OpenFile(*l, os.O_CREATE|os.O_WRONLY, 0644)
	if err == nil {
		log.Out = logFd
		defer logFd.Close()
	}
	log.Infof("Exec start!")
	log.Infof("Params logFilePath=%s, gorouteNum=%s", params.logFilePath, params.routeingNum)
	fmt.Println("start")
	// 初始化参数用于数据传递
	var logChannel = make(chan string, 3*params.routeingNum)
	var pvChannel = make(chan urlData, params.routeingNum)
	var uvChannel = make(chan urlData, params.routeingNum)
	var StorageChannel = make(chan storageBlock, params.routeingNum)

	// 建立redis pool连接池，用于存储分析结果数据
	redisPool, err := pool.New("tcp", "172.28.46.125:6379", params.routeingNum)
	if err != nil {
		log.Fatalln("Redis pool create failed")
		panic(err)
	} else {
		go func() {
			for {
				redisPool.Cmd("PING")
				time.Sleep(3 * time.Second)
			}
		}()
	}

	// 日志消费者
	go readLogLinebyLine(params, logChannel)
	//创建一组日志处理
	for i := 1; i <= params.routeingNum; i++ {
		go logConsumer(logChannel, pvChannel, uvChannel)
	}

	// 创建pv uv统计器
	go pvCounter(pvChannel, StorageChannel)
	go uvCounter(uvChannel, StorageChannel, redisPool)

	// 创建存储器
	go dataStorage(StorageChannel, redisPool)
	time.Sleep(1000 * time.Second)
}
func dataStorage(storechannel chan storageBlock, redispool *pool.Pool) {
	for b := range storechannel {
		prefix := b.countType + "_"
		setKeys := []string{
			prefix + "day_" + getTime(b.unode.unTime, "day"),
			prefix + "hour_" + getTime(b.unode.unTime, "hour"),
			prefix + "min_" + getTime(b.unode.unTime, "min"),
			prefix + b.unode.unType + "_day_" + getTime(b.unode.unTime, "day"),
			prefix + b.unode.unType + "_hour_" + getTime(b.unode.unTime, "hour"),
			prefix + b.unode.unType + "_min_" + getTime(b.unode.unTime, "min"),
		}
		Rowid := b.unode.unRid
		for _, key := range setKeys {
			ret, err := redispool.Cmd(b.storageModel, key, 1, Rowid).Int()
			if ret <= 0 || err != nil {
				log.Errorf("dataStorage redis storage error.", b.storageModel, key, Rowid)
			}
		}
	}
}
func pvCounter(pvchannel chan urlData, storagechannel chan storageBlock) {

	for item := range pvchannel {
		storage := storageBlock{"pv", item.unode, "ZINCRBY"}
		storagechannel <- storage
	}
}
func uvCounter(uvchannel chan urlData, storagechannel chan storageBlock, redispool *pool.Pool) {
	for item := range uvchannel {
		HyperLoglog := "uv_hpll_" + getTime(item.data.time, "day")
		ret, err := redispool.Cmd("PFADD", HyperLoglog, item.uid, "EX", 86400).Int()
		if err != nil {
			log.Warnf("unCounter check redis failed", err)
		}
		if ret != 1 {
			continue
		}
		sitem := storageBlock{"uv", item.unode, "ZINCRBY"}
		storagechannel <- sitem

	}
}
func getTime(logtime, timeType string) string {
	var item string
	switch timeType {
	case "day":
		item = "2006-01-02"
		break
	case "hour":
		item = "2006-01-02 11"
		break
	case "min":
		item = "2006-01-02 11:11"
		break

	}
	t, _ := time.Parse(item, time.Now().Format(item))
	return strconv.FormatInt(t.Unix(), 10)
}
func readLogLinebyLine(params cmdParams, logchannel chan string) error {
	fd, err := os.Open(params.logFilePath)
	if err != nil {
		log.Warnf("ReadFileLinebyLine can`t open file %s failed", params.logFilePath)
		return err
	}
	defer fd.Close()
	count := 0
	bufferRead := bufio.NewReader(fd)
	for {
		line, err := bufferRead.ReadString('\n')
		logchannel <- line
		count++
		if count%(1000*params.routeingNum) == 0 {
			log.Infof("ReadFileLinebyLine read line: %d", count)
		}
		if err != nil {
			if err == io.EOF {
				time.Sleep(3 * time.Second)
				log.Infof("ReadFileLinebyLine wait, readline:%d", count)
			} else {
				log.Warnf("ReadFileLinebyLine read log error: %s", err)
			}
		}

	}
	return nil

}
func logConsumer(logchannel chan string, pvchanel, uvchanel chan urlData) error {
	for logstr := range logchannel {
		// 切割日志
		data := cutLog(logstr)
		// 模拟生成uid
		hasher := md5.New()
		hasher.Write([]byte(data.ua + data.refer))
		uid := hex.EncodeToString(hasher.Sum(nil))

		udata := urlData{data, uid, formatUrl(data.url, data.time)}
		pvchanel <- udata
		uvchanel <- udata

	}
	return nil
}
func formatUrl(url, t string) urlNode {
	pos1 := str.IndexOf(url, HANDLE_MOVIE, 0)
	if pos1 != -1 {
		pos1 += len(HANDLE_MOVIE)
		pos2 := str.IndexOf(url, HANDLE_HTML, 0)
		idstr := str.Substr(url, pos1, pos2-pos1)
		id, _ := strconv.Atoi(idstr)
		return urlNode{"movie", id, url, t}
	} else {
		pos1 = str.IndexOf(url, HANDLE_LIST, 0)
		if pos1 != -1 {
			pos1 += len(HANDLE_LIST)
			pos2 := str.IndexOf(url, HANDLE_HTML, 0)
			idstr := str.Substr(url, pos1, pos2-pos1)
			id, _ := strconv.Atoi(idstr)
			return urlNode{"list", id, url, t}
		} else {
			return urlNode{"home", 1, url, t}
		}
	}
}
func cutLog(s string) digdata {
	logStr := strings.TrimSpace(s)
	pos1 := str.IndexOf(logStr, HANDLE_DIG, 0)
	if pos1 == -1 {
		return digdata{}
	}
	pos1 += len(HANDLE_DIG)
	pos2 := str.IndexOf(logStr, "HTTP/", pos1)
	d := str.Substr(logStr, pos1, pos2-pos1)

	urlinfo, err := url.Parse("http://localhost?" + d)
	if err != nil {
		return digdata{}
	}
	data := urlinfo.Query()
	return digdata{
		data.Get("time"),
		data.Get("ua"),
		data.Get("refer"),
		data.Get("url"),
	}
}
