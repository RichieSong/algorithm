package main

import (
	"fmt"
	"github.com/mgutz/str"
	"strconv"
	"time"
	"strings"
	"bytes"
)

func main() {
	str1 := "abcdefghigklmn"
	s1 := str.IndexOf(str1, "f", 0)
	fmt.Println(s1)
	s2 := str.IndexOf(str1, "b", 0)
	fmt.Println(s2)
	s3 := str.Substr(str1, s1, s2-s1) //从下标为s1 开始截取一直到s2-s1个字符
	fmt.Println(s3)
	print(getTime("day"))

	str2 := "我是爱投着 wo"
	for i, k := range str2 { // 对于字符串的for的k是字节序列，在试图找字节序列包含的utf-8编码值，而索引值i不一定是连续的
		fmt.Printf("%d: %q [% x] \n",i, k,[]byte(string(k)),k) // 编码unicode
	}
	c:=strings.Join([]string{"a","b"},",")
	fmt.Println(c)
	fmt.Println(strings.Compare("3","2"))
	var builder1 strings.Builder
	builder1.Grow(10)
	s,err:=builder1.Write([]byte("aaa"))
	if err!=nil{
		fmt.Println(err)
	}
	fmt.Println(s)
	builder1.Reset()
	builder1.WriteString("aaa")
	var buf bytes.Buffer
	buf.String()
	builder1.String()

}

func getTime(timeType string) string {
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
