package main

import (
	"fmt"
	"time"
)

func main() {

	l := [...]int{1, 2, 3, 4, 5, 6}
	for i := range l {
		if i == 4 {
			l[i] = 10
		}
	}
	fmt.Println(l)

	numbers2 := [...]int{1, 2, 3, 4, 5, 6} // 注意 数组和切片会影响结果不一样，换成切片试试？[]int{1, 2, 3, 4, 5, 6}
	maxIndex2 := len(numbers2) - 1
	for i, e := range numbers2 { // 切片是引用，数组是值类型的。改变引用类型的时候，对应遍历的也会变
		if i == maxIndex2 {
			numbers2[0] += e
		} else {
			numbers2[i+1] += e
		}
	}
	fmt.Println(numbers2)

	time.Sleep(time.Second)

}
