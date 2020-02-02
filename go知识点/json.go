package main

import (
	"encoding/json"
	"fmt"
)

func test1() {
	s1 := make(map[string]string)
	r1, err := json.Marshal(s1)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println("%v", string(r1))
}
func test2() {
	x := [5]int{1, 2, 3, 4, 5}
	//r1, err := json.Marshal(x) // 编码
	r1, err := json.MarshalIndent(x, "", "\t") // 编码 可读性很好
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(string(r1))
	var r3 interface{}
	json.Unmarshal([]byte(r1), &r3) // 解码
	fmt.Println(r3)
}

func main() {
	test1()
	test2()
}
