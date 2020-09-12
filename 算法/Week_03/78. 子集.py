# -*- coding: utf-8 -*-

"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

解题思路：
1、回溯
2、遍历自己
"""
from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """遍历"""
        res = [[]]
        for i in nums:
            res += [r + [i] for r in res]
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []

        def backtrack(first=0, track=[]):
            # 终止条件
            if k == len(track):
                res.append(track[:])
            for i in range(first, len(nums)):
                # 过滤条件没有
                track.append(nums[i])
                backtrack(i + 1, track)
                track.pop()

        for k in range(len(nums) + 1):
            backtrack()
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    print(s.subsets(nums))
