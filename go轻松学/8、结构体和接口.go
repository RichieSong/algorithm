package main

import "fmt"

//Go函数的参数传递方式是值传递
type st struct {
	width, length float64
}
type phone struct {
	price int
	size  int
	st
}
type Iphone struct {
	phone
	mode int
}

func (s *st) area() float64 { //是不是用指针，取决于你是否试图在函数内部改变传递进来的参数的值
	return s.width * s.length
}

func main() {
	//赋值方式1
	var b st
	b.width = 100 // 区别是通过.来访问数据
	b.length = 200
	fmt.Println(b.width * b.length)
	//赋值方式2
	var c = st{width: 100, length: 200}
	fmt.Println(c.width * c.length)
	//赋值方式3 顺序
	var d = st{200, 300}
	fmt.Println(d.width * d.length)
	f := new(st) // f是pointer
	f.width = 2
	f.length = 4
	fmt.Println(f.width)
	fmt.Println(f.length)
	fmt.Println(f.area())

	//内嵌结构体
	var p Iphone
	p.price = 100
	p.mode = 2
	p.size = 29
	p.length = 111
	p.width = 222
	fmt.Println(p)
	fmt.Println(p.area()) // 继承结构体的函数

	// 接口
	// 在Go语言里面，一个类型A只要实现了接口X所定义的全部方法，那么A类型的变量也是X类型的变量。
	// 在上面的例子中，NokiaPhone和IPhone都实现了Phone接口的call()方法，所以它们都是Phone

	type iphone interface {
		call()
		sales() int
	}
}
