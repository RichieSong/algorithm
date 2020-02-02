package main

import (
	"fmt"
)

/*
select通switch类似
select限制较多
其中每个case都必须是一个io操作
*/
func selectProcess(ch chan int, ch2 chan int) {
	select {
	case <-ch:
		// code
	case ch2 <- 1:
		//code
	default:
		//如果上面都没成功，code
	}
}

func main() {
	value2 := [...]int8{0, 1, 2, 3, 4, 5, 6}
	switch value2[4] {
	case 0, 1:
		fmt.Println("0 or 1")
	case 2, 3:
		fmt.Println("2 or 3")
	case 4, 5, 6:
		fmt.Println("4 or 5 or 6")
	}

}
