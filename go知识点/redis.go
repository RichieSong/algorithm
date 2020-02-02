package main

import (
	"fmt"
	"github.com/astaxie/goredis"
	"reflect"
)

var client goredis.Client

func redisConnect(addr, passwd string) {
	client.Addr = addr
	client.Password = passwd
}
func main() {
	redisConnect("172.28.46.125:6379", "")
	err := client.Set("a", []byte("b"))
	fmt.Println(reflect.TypeOf(client))
	if err != nil {
		panic(err)
	}

}
