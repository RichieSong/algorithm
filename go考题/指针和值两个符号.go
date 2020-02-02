package main

import "fmt"

func main() {
	var a int = 1
	var b *int = &a // 整数值1的地址
	var c **int = &b // 整数1的地址的地址
	var x int = *b // 整数1的值
	fmt.Println("a = ",a) // 1
	fmt.Println("&a = ",&a)// xxxx
	fmt.Println("*&a = ",*&a)// 1
	fmt.Println("b = ",b) // xxxx
	fmt.Println("&b = ",&b) // yyyy
	fmt.Println("*&b = ",*&b) // xxxx
	fmt.Println("*b = ",*b)// 1
	fmt.Println("c = ",c) //yyy
	fmt.Println("*c = ",*c) // xxx
	fmt.Println("&c = ",&c)// zzzz
	fmt.Println("*&c = ",*&c)// yyyy
	fmt.Println("**c = ",**c)//1
	fmt.Println("***&*&*&*&c = ",***&*&*&*&*&c)//1
	fmt.Println("x = ",x)//1
}

