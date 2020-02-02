package main

import (
	"fmt"
)

// if ... else if ... else
// switch
// for

func main() {
	var age = 10
	if age > 10 {
		fmt.Println("1")
	} else if 10 > age && age > 0 {
		fmt.Println("2")
	} else {
		fmt.Println("3")
	}
	switch age / 10 {
	case 0:
		fmt.Println("0")
	case 1:
		fmt.Println("1")
	case 3:
		fmt.Println("3")
	default:
		fmt.Println("default")
	}
	var i int = 1
	for ; i <= 100; i++ {
		fmt.Println(i) // 如果前面加go的话 ，则发现 少打印数据，猜测变量i被覆盖了
	}

}
