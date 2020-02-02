package main

import (
	"crypto/sha1"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"math/rand"
	"net/url"
	"os"
	"runtime"
	"strings"
	"sync"
	"sync/atomic"
	"time"
)

func createFile(p string) *os.File {
	fmt.Println("creating")
	f, err := os.Create("test.txt")
	if err != nil {
		panic(err)
	}
	return f
}
func wirteFile(f *os.File) {
	fmt.Println("writing")
	fmt.Fprint(f, "data")
}
func closeFile(f *os.File) {
	fmt.Println("closing")
	f.Close()
}

type Response1 struct {
	Page   int
	Fruits []string
}
type Response2 struct {
	Page   int      `json:"page"`
	Fruits []string `json:"fruits"`
}

func main() {

	data := "abc123!?$*&()'-=@~abc123!?$*&()'-=@~"
	//标准编码
	senc := base64.StdEncoding.EncodeToString([]byte(data))
	fmt.Println(senc)
	sdec, _ := base64.StdEncoding.DecodeString(senc)
	fmt.Println(sdec)
	fmt.Println(string(sdec))

	// url的base64编码和解码
	uenc := base64.URLEncoding.EncodeToString([]byte(data))
	fmt.Println(uenc)
	udnc, _ := base64.URLEncoding.DecodeString(uenc)
	fmt.Println(udnc)
	fmt.Println(string(udnc))
	//这两种方法都将原数据编码为base64编码，区别在于标准的编码后面是+，而兼容URL的编码方式后面是-。

	// go defer 释放资源
	f := createFile("test.txt")
	defer closeFile(f)
	wirteFile(f)

	// os.Exit 当使用`os.Exit`的时候defer操作不会被运行，
	//os.Exit(3) //defer不会执行，注意，Go和C语言不同，main函数并不返回一个整数来表示程序的退出状态，而是将退出状态作为os.Exit函数的参数。

	// json数据的编码和解码
	//基础数据编码
	bolB, _ := json.Marshal(true)
	fmt.Println(string(bolB))

	intB, _ := json.Marshal(2)
	fmt.Println(string(intB))

	fltB, _ := json.Marshal(2.34)
	fmt.Println(string(fltB))

	strB, _ := json.Marshal("abc")
	fmt.Println(string(strB))

	arr := []string{"a", "c", "d"}
	dicB, _ := json.Marshal(arr)
	fmt.Println(string(dicB))

	mapd := map[string]int{"a": 1, "b": 2}
	mapB, _ := json.Marshal(mapd)
	fmt.Println(string(mapB))

	resD := Response2{
		Page:   1,
		Fruits: []string{"a", "b", "o"}}
	resB, _ := json.Marshal(resD)
	fmt.Println(string(resB))
	res1D := &Response1{
		Page:   1,
		Fruits: []string{"a", "b", "o"}}
	res1B, _ := json.Marshal(res1D)
	fmt.Println(string(res1B))

	byt := []byte(`{"num":2.3,"strs":["a","b"]}`)
	var dat map[string]interface{}
	if err := json.Unmarshal(byt, &dat); err != nil { //解码过程，并检测相关的错误
		panic(err)
	}
	fmt.Println(dat)
	num := dat["num"].(float64)
	fmt.Println(num)

	strs := dat["strs"].([]interface{})
	str1 := strs[0].(string)
	fmt.Println(str1)
	enc := json.NewEncoder(os.Stdout)
	d := map[string]int{"a": 1, "b": 2}
	enc.Encode(d)

	// lines filters
	//scanner := bufio.NewScanner(os.Stdin)
	//for scanner.Scan() {
	//	ucl := strings.ToUpper(scanner.Text())
	//	fmt.Println(ucl)
	//}
	//if err := scanner.Err(); err != nil {
	//	fmt.Fprint(os.Stderr, "error", err)
	//	os.Exit(1)
	//}
	//Panic表示的意思就是有些意想不到的错误发生了。通常我们用来表示程序正常运行过程中不应该出现的，或者我们没有处理好的错误。

	//SHA1散列经常用来计算二进制或者大文本数据的短标识值。git版本控制系统用SHA1来标识受版本控制的文件和目录。

	h := sha1.New()
	s := "sha1 this string"
	h.Write([]byte(s))
	bs := h.Sum(nil) //这里计算最终的hash值，Sum的参数是用来追加而外的字节到要计算的hash字节里面
	fmt.Println(s)
	fmt.Printf("%x\n", bs) // SHA1散列值经常以16进制的方式输出，这样，所以可以使用`%x`来将散列结果格式化为16进制的字符串

	// string and Byte切片转换
	// String转换到Byte数组时，每个byte(byte类型其实就是uint8)保存字符串对应字节的数值。
	//注意Go的字符串是UTF-8编码的，每个字符长度是不确定的，一些字符可能是1、2、3或者4个字节结尾。
	s1 := "宋明"
	r1 := []rune(s1)
	fmt.Println(r1) //每个字一个数值
	s2 := "abc"
	r2 := []byte(s2)
	fmt.Println(r2)

	// url解析
	s3 := "postgres://user:pass@host.com:5432/path?k=v#f"
	u, err := url.Parse(s3) //解析url并保证没有错误
	if err != nil {
		panic(err)
	}
	fmt.Println(u.Scheme) //直接访问解析之后的模式
	fmt.Println(u.User)   // 获取信息
	fmt.Println(u.User.Username())
	fmt.Println(u.User.Password())
	fmt.Println(u.Host)
	hos := strings.Split(u.Host, ":")
	fmt.Println(hos)
	fmt.Println(u.Path)     //获取path的uri
	fmt.Println(u.Fragment) //获取#后面的flag
	fmt.Println(u.RawQuery)
	m, _ := url.ParseQuery(u.RawQuery) //获取k=v
	fmt.Println(m)

	// go 互斥
	// 使用Mutex来在多个协程之间安全地访问数据。
	var stats = make(map[int]int)
	var mutex = &sync.Mutex{}
	var ops int32 = 0
	for r := 0; r < 100; r++ { //读
		go func() {
			total := 0
			for {
				key := rand.Intn(5)
				mutex.Lock()
				total += stats[key]
				mutex.Unlock()
				atomic.AddInt32(&ops, 1)
				runtime.Gosched() //手动地释放资源控制权
			}
		}()
	}
	for r := 0; r < 10; r++ {
		go func() {
			for {
				key := rand.Intn(6)
				value := rand.Intn(100)
				mutex.Lock()
				stats[key] = value
				mutex.Unlock()
				atomic.AddInt32(&ops, 1)
				runtime.Gosched()
			}
		}()
	}
	time.Sleep(time.Second)
	opsf := atomic.LoadInt32(&ops)
	fmt.Println("opsf", opsf)
	fmt.Println(ops)

	mutex.Lock()
	fmt.Println("state", stats)
	mutex.Unlock()
	// go 处理信号

}
