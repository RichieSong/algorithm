package main

import (
	"fmt"
	"strings"
	"time"
)

func add(a int, b int) int {
	var sum int
	sum = a + b
	return sum
}

func sroll() {
	for i := 0; i < 100; i++ {
		go fmt.Println(i)

	}
	fmt.Println("aaaa")
	fmt.Println("finish")
}
func mapp() {
	m := map[string]string{
		"a": "aa",
		"b": "bb",
	}
	m2 := make(map[string]string) // m2==empty map
	var m3 map[string]string      //m3==nil
	fmt.Println(m, m2, m3)
	for k, v := range m {
		fmt.Println(k, v)
	}
	a, ok := m["a"]
	fmt.Println(a, ok)
	b, ok := m["m"]
	fmt.Println(b, ok)
	m4 := make(map[byte]int)
	fmt.Println(m4)
}
func test_pip() {
	pipe := make(chan int, 3)
	pipe <- 1
	pipe <- 2
	pipe <- 3
	sum := <-pipe
	fmt.Println(len(pipe))
	fmt.Println(sum)
}
func test_pop() {
	fmt.Println("adfasdf")
}

func main() {
	fmt.Println("helloson")
	// s:= add(100,200)
	time.Sleep(time.Second)
	// fmt.Println(s)
	sroll()
	// test_pip()
	mapp()
	a := []int{1, 2, 3, 4}
	a = append(a, 5)
	fmt.Println(len(a), cap(a))
	b := a[2:]
	fmt.Println(len(b), cap(b))
	fmt.Println(b)
	c := b[3:]
	fmt.Println(len(c), cap(c))
	c = append(c, 6)
	fmt.Println(len(c), cap(c))
	fmt.Println(a)
	d := make(map[int]int, 1)
	d[1] = 2
	d[1] = 3
	d[2] = 2

	fmt.Println(d)
	fmt.Println(len(d))
	str := "qb-dev-1-qb"
	str1 := "qb-pro"
	str2 := "qb-qa-1"
	fmt.Println(strings.Split(str, "-")[1])
	fmt.Println(strings.Split(str1, "-")[1])
	fmt.Println(strings.Split(str2, "-")[1])
	//fmt.Println(strings.Replace(limit(str), "qb", "qingniu", 2))
	fmt.Println(3|9)

}
