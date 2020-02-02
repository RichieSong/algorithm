package main

import (
	"fmt"
)

type tester interface {
	test()
	string() string
}
type stringer interface {
	string() string
}

type data struct {
}

type datas struct {
}

func (datas) string() string {
	return "datas string"
}
func (*data) test() {
	fmt.Println("test....")
}
func (data) string() string {
	return "string"
}
func pp(a stringer) {
	fmt.Println(a.string())
}
func main() {
	var d data
	var t tester = &d
	var dd datas
	var s stringer = &dd
	pp(s)
	t.test()
	fmt.Println(t.string())

}
