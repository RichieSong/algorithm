package main

import (
	"fmt"
	"runtime"
	"sync"
)

/*
并发的难度在于协调，而协调就要通过交流

工程上通用并发通信模型：
1、共享数据
2、消息

总结：“不要通过共享内存来通信,而应该通过通信来共享内存。”

*/
var counter int
var wg sync.WaitGroup
var a string

var once sync.Once

func Count(lock *sync.Mutex) {
	defer wg.Done()
	lock.Lock()
	counter++
	fmt.Println(counter)
	lock.Unlock()
}
func CounterChannel(ch chan int) {
	defer wg.Done()
	ch <- 1
	fmt.Println("counter")
}

func setup() {
	a = "hello"
}
func doprint() {
	once.Do(setup)
	fmt.Println(a)
}
func towprint() {
	go doprint()
	go doprint()
}
func main() {
	lock := &sync.Mutex{}
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go Count(lock)
	}
	for {
		lock.Lock()
		c := counter
		lock.Unlock()
		runtime.Gosched()
		if c >= 10 {
			break
		}
	}
	chs := make([]chan int, 10)
	for i := 0; i < 10; i++ {
		chs[i] = make(chan int)
		wg.Add(1)
		go CounterChannel(chs[i])
	}
	for _, ch := range chs {
		fmt.Println(<-ch)
	}
	towprint()
	wg.Wait()

}
