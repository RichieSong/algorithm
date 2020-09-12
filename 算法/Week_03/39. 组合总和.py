# -*- coding: utf-8 -*-
"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:

输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

解题思路：
回溯+剪枝
"""
from typing import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        n = len(candidates)
        def backtrack(i, tmp_sum, track):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(track)
            backtrack(i, tmp_sum + candidates[i], track + [candidates[i]])
            backtrack(i + 1, tmp_sum, track)

        backtrack(0, 0, [])
        return res
