# -*- coding: utf-8 -*-

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

解题思路：
回溯
1、终止条件 len(nums)== len(track)
2、套用回溯模板
"""
from typing import *


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []

        def backtrack(track):
            if len(nums) == len(track):
                res.append(track[:])
            for n in nums:
                # 排除不合法的
                if n in track:
                    continue
                track.append(n)
                backtrack(track)
                track.pop()

        backtrack([])
        return res

    def permute1(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []

        def backtrack(first=0):
            if len(nums) == first:
                res.append(nums[:])
            for i in range(first, len(nums)):
                nums[i], nums[first] = nums[first], nums[i]
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]

        backtrack()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute1([1, 2, 3]))
