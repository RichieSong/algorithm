package main

import (
	"fmt"
	"math"
	"math/cmplx"
	"strconv"
)

var i uint8 //无符号整型
var ii int8 //有符号整型

var s byte

var ss rune //相当与char

var f float32 = 12
var ff float32 = 23
var f1 float64 = 23
var f2 float64 = 34

var a = "aa \n bb" // 双引号被转义
var b = `aa \n bb` // `不能被转义
var c = "你好"

func constes() {
	const a, b = 2, 3
}
func emuns() {
	const (
		app    = 1
		java   = 2
		python = 3
		golang = 4
	)
	fmt.Println(app, java, python, golang)
	const (
		a = 1 << (10 * iota)
		b
		c
		d
		f
	)
	fmt.Println(a, b, c, d, f)

}
func main() {
	fmt.Println(f / ff)
	fmt.Println(f2 / f1)
	fmt.Println(a)
	fmt.Println("----------")
	fmt.Println(b)
	fmt.Println(len(a))
	fmt.Println(len(b))
	fmt.Println(a + b)
	fmt.Println(a[1]) //go的字符串是有字节组成
	fmt.Println(c[1]) //go的字符串是有字节组成
	fmt.Println(&c)   //得到内存地址
	var equal bool
	var aa int = 10
	var bb int = 20
	equal = (aa != bb)
	fmt.Println(equal)
	fmt.Println(cmplx.Abs(-1))
	fmt.Println(strconv.Itoa(aa))

	//任何空值(nil)或者零值(0, 0.0, "")都不能作为布尔型来直接判断。
	//if 0 {
	//	fmt.Println("0")
	//}
	//if nil {
	//	fmt.Println("nil")
	//}
	//if "" {
	//	fmt.Println("null str")
	//}
	var c int = int(math.Sqrt(float64(aa*aa + bb*bb)))
	fmt.Println(c)
	emuns()
	i := make(chan int, 3)
	fmt.Println(i)

}
