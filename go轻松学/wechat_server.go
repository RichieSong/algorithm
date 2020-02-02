package main

import (
	"fmt"
	"github.com/gpmgo/gopm/modules/log"
	"net"
)

func CheckErr(err error) {
	if err != nil {
		panic(err)
	}
}
func ProcessInfo(conn net.Conn) {
	buf := make([]byte, 1024)
	defer conn.Close()
	for {
		numOfBytes, err := conn.Read(buf)
		CheckErr(err)
		if numOfBytes != 0 {
			fmt.Printf("Received Message: %s", string(buf))
		}

	}
}
func main() {
	listen, err := net.Listen("tcp", ":8000")
	if err != nil {
		log.Fatal(err.Error())
	}
	defer listen.Close()
	for {
		conn, err := listen.Accept()
		CheckErr(err)
		go ProcessInfo(conn)

	}

}
