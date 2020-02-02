package main

import (
	"fmt"
	"strconv"
	"time"
)

func test_gorouting() {
	fmt.Println("xxxxxx")
}
func Read(ch chan int) {
	value := <-ch
	fmt.Println(strconv.Itoa(value))
}
func Wirte(ch chan int) {
	ch <- 1
	ch <- 2
	ch <- 3
}
func main() {
	ch := make(chan int) // 等价于make(chan int,0) 当存数据的时候，通道满了会阻塞
	for i := 1; i < 10; i++ {
		go Read(ch)
	}

	go Wirte(ch)

	time.Sleep(time.Millisecond)
	fmt.Println("end")
}
