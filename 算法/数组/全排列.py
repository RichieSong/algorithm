# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/12 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
递归模板

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

"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []

        def trackback(first, track):
            if first == len(nums):
                res.append(track[:])
            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                trackback(first + 1, track)
                track.pop()

        res = []
        trackback(0, [])
        return res




