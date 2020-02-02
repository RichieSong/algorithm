package main

import (
	"fmt"
)

type Str struct {
	Name string `json:"name"`
}

//结构体方法：有接受者
func (s Str) get() string {
	return s.Name
}

//纯函数
func GetOther(s Str) string {
	return s.Name
}
func main() {
	// 方法实现
	ss := Str{Name: "richie"}
	fmt.Println(ss.get())
	// 函数实现
	fmt.Println(GetOther(ss))
}
