package main

import (
	"fmt"
)

func plus(a int, b int) (res int) {
	return a + b
}
func main() {
	//反射
	//reflect.TypeOf()
	//reflect.ValueOf()
	//reflect.Kind() 类别
	// 计算
	res := plus(1, 2)
	fmt.Println(res)
	// go的原子计数器
	//Go里面的管理协程状态的主要机制就是通道通讯。这些我们上面的例子介绍过。这里还有一些管理状态的机制，
	// 下面我们看看多协程原子访问计数器的例子，这个功能是由sync/atomic包提供的函数来实现的。

}
