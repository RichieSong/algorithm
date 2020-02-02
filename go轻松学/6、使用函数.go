package main

import (
	"fmt"
)

func slice_num(arr []int) (sum int) {
	sum = 0
	for _, e := range arr {
		sum += e
	}
	return
}
func slice_num1(arr []int) int {
	sum := 0
	for _, e := range arr {
		sum += e
	}
	return sum
}
func slice_num2(base int, arr ...int) int {
	sum := 0
	base += 100
	for _, e := range arr {
		sum += e
	}
	return base
}
func create() func() uint {
	i := uint(0)
	return func() (ret uint) {
		ret = i
		i += 2
		return
	}
}
func factorial(x int) int {
	if x == 0 {
		return 1
	}
	return factorial(x-1) * x
}
func fibonacci(x int) int {
	if x == 1 {
		return 1
	} else if x == 2 {
		return 2
	} else {
		return fibonacci(x-2) + fibonacci(x-1)
	}
}
func main() {
	var arr1 = []int{1, 2, 3, 4, 5}
	var arr2 = []int{3, 4, 5, 6, 7, 8}
	fmt.Println(slice_num(arr1))
	fmt.Println(slice_num(arr2))

	//闭包 闭包函数对它外层的函数中的变量具有访问和修改的权限
	var base int = 10
	var num int = slice_num2(base, arr1...)
	fmt.Println(num)
	inc := func() {
		base += 1
	}
	fmt.Println(base)
	inc()
	fmt.Println(base)

	cr := create()
	fmt.Println(cr())
	fmt.Println(cr())
	fmt.Println(cr())
	fmt.Println(cr())
	// 递归函数
	//阶乘
	ff := factorial(5)
	fmt.Println(ff)
	//斐波拉切数列
	fmt.Println(fibonacci(11))
	// 异常处理
	defer fmt.Println(ff) //Go语言提供了关键字defer来在函数运行结束的时候运行一段代码或调用一个清理函数,是在main函数执行结束的时候才调用的。最后调用
	//defer用途最多的在于释放各种资源

	// panic & recover panic和recover是Go语言提供的用以处理异常的关键字。panic用来触发异常，而recover用来终止异常并且返回传递给panic的值。（注意recover并不能处理异常，而且recover只能在defer里面使用，否则无效。）
	//panic触发的异常通常是运行时错误。比如试图访问的索引超出了数组边界，忘记初始化字典或者任何无法轻易恢复到正常执行的错误。

	defer func() {
		msg := recover()
		fmt.Println(msg)
	}()
	fmt.Println("I am working")
	panic("It starts to rain cats")

}
