package main
import (
	"fmt"
)
type student struct {
	Name string
	Age  int
}
func pase_student() map[string]*student {
	m := make(map[string]*student)
	stus := []student{
		{Name: "zhou", Age: 24},
		{Name: "li", Age: 23},
		{Name: "wang", Age: 22},
	}
	// 遍历的map的value是个指针
	for _, stu := range stus {
		//stu := stus[i] // 注意 新加的
		fmt.Println(&stu) // **** 此时的地址会覆盖上一次的地址，而地址是不嫩被复制的，所以此时打印没问题
		m[stu.Name] = &stu // 一旦存储多个这样的地址必然是一样的
	}
	for k,v := range stus{
		fmt.Println(k,&v)
	}
	// 遍历map的value是值类型的，发现不是按顺序的
	//值所以不是固定顺序，是因为for range map开始处理循环逻辑的时候就开始随机播种
	// 为什么这样设计？最重要的原因就是当map因扩张而重新hash时，各个键值对存储位置可能会发生改变
	s:= make(map[int32]string)
	s[0]="test0"
	s[1]="test1"
	s[2]="test2"
	s[3]="test3"
	s[4]="test4"
	s[5]="test5"
	for k,v :=range s{
		fmt.Println(k,v)
	}
	return m
}
func main() {
	students := pase_student()
	for k, v := range students {
		fmt.Printf("key=%s,value=%v \n", k, v)
	}
}