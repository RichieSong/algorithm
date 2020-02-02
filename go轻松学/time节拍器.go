package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	fmt.Println("start。。。")
	tick := time.Tick(2 * time.Second)
	abort := make(chan struct{})
	go func() {
		os.Stdin.Read(make([]byte, 1))
		abort <- struct{}{}
	}()
	for i := 0; i <= 10; i++ {
		fmt.Println(i)
		select {
		case <-tick:
		case <-abort:
			fmt.Println("Lanund abort!")
			return
		}
	}
	fmt.Println("end")
}
