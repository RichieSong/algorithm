package main

import (
	"fmt"
)

//
//给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
//
//你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
//
//示例:
//
//给定 nums = [2, 7, 11, 15], target = 9
//
//因为 nums[0] + nums[1] = 2 + 7 = 9
//所以返回 [0, 1]

func towSum(nums []int, target int) []int {
	hash_map := make(map[int]int)
	for i, x := range nums {
		xx := target - x
		for k, v := range hash_map {
			if xx == k {
				var data []int
				data = append(data, v)
				data = append(data, i)
				return data
			}
		}
		hash_map[x] = i
	}
	return []int{}
}

func main() {
	nums := []int{2, 11, 7, 19}
	target := 9
	fmt.Println(towSum(nums, target))

}
