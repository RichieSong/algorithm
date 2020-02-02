package main

import (
	"fmt"
	"regexp"
)

func main() {
	isok, _ := regexp.Match("[a-zA-Z]{3}", []byte("zhaddfa1i"))
	fmt.Println(isok)
	s1 := regexp.MustCompile("<span>(.*?)</span>")
	fmt.Println(s1)
	res := s1.FindAllStringSubmatch("<span>abc</span>", 1)
	ret := s1.FindAllString("<span>abc</span>", -1)
	fmt.Println(res)
	fmt.Println(ret)
	for i, v := range ret {
		fmt.Println(i, v)
	}

}
