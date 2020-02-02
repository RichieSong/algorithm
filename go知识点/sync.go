package main

import (
	"fmt"
	"sync"
)

func withchannel() {
	sign := make(chan byte, 3)
	go func() {
		fmt.Println(2)
		sign <- 2
	}()
	go func() {
		fmt.Println(3)
		sign <- 3
	}()
	go func() {
		fmt.Println(4)
		sign <- 4
	}()
}
func withwaitgroup() {
	var wg sync.WaitGroup
	wg.Add(3)
	go func() {
		fmt.Println(2)
		wg.Done()
	}()
	go func() {
		fmt.Println(3)
		wg.Done()
	}()
	go func() {
		fmt.Println(4)
		wg.Done()
	}()
	wg.Wait()
}
func main() {
	//withchannel()

	withwaitgroup()

	fmt.Println("main")

}
