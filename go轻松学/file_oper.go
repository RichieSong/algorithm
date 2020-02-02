package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
	"path/filepath"
	"runtime"
	"strings"
)

func parse_log_dir(p string) {
	fi, err := os.Stat(p)
	fmt.Println(fi.IsDir())
	path, err := ioutil.ReadDir(p)
	if err != nil {
		log.Fatalf(err.Error())
	}
	for _, f := range path {
		if f.IsDir() && !strings.HasPrefix(f.Name(), ".") {
			if !strings.HasSuffix(p, "/") {
				p = p + "/"
			}
			pp := p + f.Name() + "/"
			parse_log_dir(pp)
		} else {
			ok := strings.HasSuffix(f.Name(), ".log")
			if ok {
				fmt.Println(p + f.Name())
			}
		}

	}
}
func filePath() {
	fp, err := filepath.Abs(".")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(fp)
}
func main() {
	path := "/tmp/"
	parse_log_dir(path)
	filePath()
	fmt.Println(runtime.GOOS) // return os type
}
