# -*- coding: utf-8 -*-
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

解题思路：
1、套用回溯模板，结果去重


"""
from typing import *


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        nums.sort()
        def backtrack(nums, track):
            if not nums:
                res.append(track)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[:i] + nums[i + 1:], track + [nums[i]])
        backtrack(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    n = [1, 1, 2]
    print(s.permuteUnique(n))
