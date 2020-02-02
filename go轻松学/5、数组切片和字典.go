package main

import (
	"fmt"
	"strings"
	"time"
)

func main() {
	var x [8]int                                      //数组定义
	var xx = [19]int{1, 2, 3, 3, 34, 23, 5, 65, 6, 6} // 有初始值的数组定义
	var xxx = [...]int{}
	x[0] = 1
	x[2] = 2
	x[0] = 23
	fmt.Println(x)
	var sum int
	for _, elem := range xx {
		sum += elem
	}
	fmt.Println(sum)
	fmt.Println(xx)
	fmt.Println(len(xx))
	fmt.Println(xxx)

	//切片一
	var a = make([]float64, 5) //定义切片
	fmt.Println(cap(a), len(a))
	var b = make([]float64, 5, 10)
	fmt.Println(cap(b), len(b))
	for i := 0; i < len(a); i++ {
		a[i] = float64(i)
	}
	fmt.Println(a)

	for i := 0; i < len(b); i++ {
		b[i] = float64(i)
	}
	var arr = append(b, 5, 6, 7, 8, 9, 19) //Go在默认的情况下，如果追加的元素超过了容量大小，Go会自动地重新为切片分配容量，容量大小为原来的两倍
	//b[5] = 10 虽然切片的容量可以大于长度，但是赋值的时候要注意最大的索引仍然是len(b)－1 ,否则会报索引超出边界错误
	fmt.Println("b", b)
	fmt.Println(arr)
	fmt.Println("arr:", cap(arr), len(arr))
	//切片二
	var c = arr[2:3] //[min_index:max_index] 方式
	fmt.Println(c)
	fmt.Println(cap(c), len(c))
	var d = b[:] //相当于复制
	d[0] = 100
	fmt.Println(cap(d), len(d))
	fmt.Println(d)
	s := make([]float64, 3, 10)
	copy(s, d)
	fmt.Println(s)
	fmt.Println(cap(s), len(s))
	//总结一下，数组和切片的区别就在于[]里面是否有数字或者...。因为数值长度是固定的，而切片是可变的。

	// 字典方式一
	var m = map[string]string{ //初始化定义dict
		"a": "a",
		"b": "b",
		"c": "c",
		"d": "d",
	}
	for k, v := range m {
		fmt.Println(k, v)
	}
	m["e"] = "e"
	fmt.Println(m)
	var m1 = make(map[string]string) //make初始化dict
	m1["f"] = "f"
	fmt.Println(m1["g"]) //不存在的值为空
	if val, ok := m1["g"]; ok {
		fmt.Println(val)
	}
	var m2 = make(map[string]int)
	m2["a"] = 1
	fmt.Println(len(m2))

	var fb = make(map[string]map[string]int)
	fb["aa"] = map[string]int{"a": 1}
	fb["bb"] = map[string]int{"b": 2}
	fb["cc"] = map[string]int{"c": 3}
	fmt.Println(fb)
	//遍历字典
	for k, v := range fb {
		fmt.Println(k)
		for kk, vv := range v {
			fmt.Println(kk, vv)
		}
		fmt.Println()
	}
	var y = [...]int{1, 2, 3, 4, 5}
	yy := y[:3]
	//y:= append(y,11)
	yy = append(yy, 11)
	fmt.Println(y, yy)
	fmt.Printf("%T %T", y, yy)
	loc, _ := time.LoadLocation("Asia/Shanghai")
	fmt.Println("aaaa", loc)
	var str = "[19/Jun/2018:23:17:59"
	//ssss := strings.Replace(str, "[", "", -1)
	t, err := time.ParseInLocation("02/Jun/2006:15:04:05", strings.Replace(str, "[", "", -1), loc)
	fmt.Println(t, err)
	//fmt.Println(ssss)
	fmt.Println(time.Now())
	var runes []rune
	for _, st := range "我的名字叫songming！" {
		runes = append(runes, st)
	}
	fmt.Printf("%q", runes)
}
