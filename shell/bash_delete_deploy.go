package main

import (
	"bytes"
	"fmt"
	"os/exec"
)

func exec_shell(s string) (string, error) {
	cmd := exec.Command("/bin/bash", "-c", s)
	var out bytes.Buffer
	cmd.Stdout = &out
	err := cmd.Run()
	checkErr(err)
	return out.String(), err
}

func checkErr(err error) {
	if err != nil {
		fmt.Println(err)
		panic(err)
	}
}

func main() {
	result, err := exec_shell("ls")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(result)

}
