package main

import (
	"fmt"
)

func main() {
	fmt.Println("start")
	for i := 0; i < 10; i++ {
		go func() { // go函数执行时间永远滞后go语句
			fmt.Println(i) // 所以此行基本不会打印，大部分情况因为还没给执行机会，整个main函数执行完了，注意：主函数(main)执行完了，子函数(go func)即使没执行也就结束了
		}()
		fmt.Println("md")
	}
	fmt.Println("end")
}
