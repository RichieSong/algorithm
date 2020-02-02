package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
)

func b2s(c []uint8) string {
	var b = []byte{}
	for _, k := range c {
		b = append(b, k)
	}
	return string(b)
}

func main() {
	const filename = "test.txt"
	//一次性读取
	if contents, err := ioutil.ReadFile(filename); err != nil {
		panic(err)
	} else {
		fmt.Println(string(contents))
	}
	//逐行读取
	if file, err := os.Open(filename); err == nil {
		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			fmt.Println(scanner.Text())
		}
	} else {
		panic(err)
	}
}
