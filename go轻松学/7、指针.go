package main

import "fmt"

//指针即存储变量的地址
// & 取一个变量的地址
// * 取一个指针变量所指向的地址的值

func change(t *int) {
	*t = 200
}
func set_value(x *int) {
	*x = 100
}
func swap(b, c *int) {
	*b, *c = *c, *b
}
func test() {
	a := 100
	b := 100
	fmt.Println(a == b)
	fmt.Println(&a == &b)
	c := a + b
	fmt.Println(c)
	fmt.Println(&c)
}
func main() {
	var x int
	var xx *int
	x = 10
	xx = &x
	fmt.Println(x)
	fmt.Println(xx)
	fmt.Println(*xx)
	fmt.Println(&xx)
	//指针的一大用途就是可以将变量的指针作为实参传递给函数，从而在函数内部能够直接修改实参所指向的变量值。
	//Go的变量传递都是值传递。
	var t int = 100
	fmt.Println(t)
	change(&t)
	fmt.Println(t)
	// new 函数
	//new来初始化一个指针
	a := new(int)
	set_value(a)
	fmt.Println(a)  //存储指针a的地址
	fmt.Println(&a) //a本身的地址
	fmt.Println(*a) //a的值
	b := 100
	c := 200
	swap(&b, &c)
	fmt.Println(b)
	fmt.Println(c)
	test()
}
