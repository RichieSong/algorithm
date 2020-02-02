package main

import (
	"io"
	"log"
	"net"
	"time"
)

func handlerConn(conn net.Conn) {
	defer conn.Close()
	for {
		_, err := io.WriteString(conn, time.Now().Format("15:04:05\n"))
		if err != nil {
			return
		}
		time.Sleep(time.Second * 2)
	}
}

func main() {
	listen, err := net.Listen("tcp", "127.0.0.1:9090")
	if err != nil {
		panic(err)

	}
	for {
		conn, err := listen.Accept()
		if err != nil {
			log.Fatalf(err.Error())
		}
		go handlerConn(conn)

	}
}
