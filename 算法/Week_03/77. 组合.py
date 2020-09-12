# -*- coding: utf-8 -*-
"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

解题思路：
回溯+剪枝

"""
from typing import *


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 先去掉不符合条件的
        if n <= 0 or k <= 0 or k > n: return []

        res = []

        # 回溯核心
        def backtrack(n, k, start, track):
            if len(track) == k:  # 终止条件
                res.append(track[:])  # 如果是引用，切记将引用copy到结果值中
                return
            for s in range(start, n + 1):  # 遍历选择
                track.append(s)  # 做出选择
                backtrack(n, k, s + 1, track)  # 递归调用
                track.pop()  # 因为有全局遍历，需要撤销选择

        backtrack(n, k, 1, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))
