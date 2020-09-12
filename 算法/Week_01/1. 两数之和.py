# -*- coding: utf-8 -*-
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

 

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

解题思路：
1、暴力求解，2层循环 时间复杂度O(n**2)   不推荐
2、利用字典记录信息，一遍循环即可 时间复杂度 O(n)

"""

from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for i, v in enumerate(nums):
            if v in map_dict:
                return [i, map_dict[v]]
            map_dict[target - v] = i
        return []


if __name__ == '__main__':
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
