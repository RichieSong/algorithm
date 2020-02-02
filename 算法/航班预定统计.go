package main

import (
	"fmt"
	"time"
)

/*
这里有 n 个航班，它们分别从 1 到 n 进行编号。

我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。

请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。



示例：

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]


提示：

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000

*/

func corpFlightBookings(bookings [][]int, n int) []int {
	up, down := make([]int, n+1), make([]int, n+1)
	for _, v := range bookings {
		fmt.Println(v)
		up[v[0]] += v[2]
		down[v[1]] += v[2]
	}
	re := []int{}
	num := 0
	fmt.Println(up)
	fmt.Println(down)

	for i := 1; i <= n; i++ {
		num += up[i] - down[i-1] //精妙之处 有点不懂
		re = append(re, num)
	}
	return re
}
func corpFlightBookings1(bookings [][]int, n int) []int {
	res := make([]int, n+1)
	for _, book := range bookings {
		res[book[0]-1] += book[2]
		res[book[1]] -= book[2]
	}
	for i := 1; i <= n; i++ {
		res[i] += res[i-1]
	}
	return res[:n]
}

func main() {
	bookings := [][]int{
		{1, 2, 10},
		{2, 3, 20},
		{2, 5, 25},
	}
	re := corpFlightBookings1(bookings, 5)
	fmt.Println(re)
	time.Sleep(time.Second)
}
