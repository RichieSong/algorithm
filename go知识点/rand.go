package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"time"
)

func main() {
	fmt.Println(time.Now().UnixNano())
	rand.Seed(time.Now().UnixNano())
	fmt.Println(runtime.GOMAXPROCS(runtime.NumCPU()))
	fmt.Println(runtime.NumCPU())
	fmt.Println(time.Since(time.Now()))

}
