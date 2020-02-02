package main

import (
	"crypto/md5"
	"fmt"
)

func test() {
	Md5Inst := md5.New()
	Md5Inst.Write([]byte("songming"))
	ret := Md5Inst.Sum([]byte("aaa")) // aaa相当于salt
	fmt.Printf("%v", string(ret))     //md5 结果 他是一大串乱码 不太友好
	fmt.Printf("%x\n\n", ret)         // 友好结果
	fmt.Println(string(ret))
}
func main() {
	test()
}
