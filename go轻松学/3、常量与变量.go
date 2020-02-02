package main

import (
	"fmt"
	"math"
)

var x string = "hello world" //全局定义
var a1 string = "1"

func main() {
	const age int8 = 12
	fmt.Println(x)
	var xx string // 定义方式
	xx = "hello2" + a1
	fmt.Println(xx)

	x3 := "hello3" //快捷定义方式 只能在函数内部使用
	fmt.Println(x3)
	//fmt.Println(int8(a)) //同类型之间转换
	var f float64 = 23.923
	fmt.Println(int8(f))
	c := a1 + "2"
	fmt.Println(c)
	//age = 34 不能给常量更改
	fmt.Println(age)
	var f1 float64 = 10
	var area = math.Pow(f1, 2) * math.Pi
	fmt.Println(area)
	// 同时定义多个变量或常量
	var (
		a  int     = 10
		b  float64 = 23.1
		c1 bool    = false
	)
	const (
		Pi   float64 = 3.15
		True bool    = true
	)
	fmt.Println(a, b, c1)
	//fmt.Println(Pi, True)
	fmt.Println(a1)
	var s = []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	s1 := s[2:4]
	s2 := s1[1:3]
	s1[1] = 199
	fmt.Println(s)
	fmt.Println(s1)
	fmt.Println(s2)
	s1 = append(s1, s2...)
	fmt.Println(s1, cap(s1))
	s1 = append(s1, s...)
	fmt.Println(s1, cap(s1))
	sb := make([]int, 20)
	copy(sb, s1)
	fmt.Println(sb)

}
