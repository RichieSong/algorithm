package main

import (
	"fmt"
	"time"
)

func sum(num int, dev int, res chan int) {
	sum := 0
	for value := 0; value < num; value++ {
		if value%dev == 0 {
			sum += value
		}
	}
	res <- sum
}

func main() {
	res := make(chan int, 3)
	limit := 100000000
	t_start := time.Now()
	go sum(limit, 3, res)
	go sum(limit, 5, res)
	sum3, sum5 := <-res, <-res
	fmt.Println(sum3)
	fmt.Println(sum5)
	go sum(limit, 15, res)
	sum15 := <-res
	s := sum3 + sum5 - sum15
	t_end := time.Now()
	fmt.Println(s)
	fmt.Println(t_end.Sub(t_start))

}
