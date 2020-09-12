# -*- coding: utf-8 -*-
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6

解题思路：
乍一看跟老师的柱状图求面积一样 解法一样

双指针：
动态规划
栈：
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, res, maxl, maxr = 0, len(height) - 1, 0, 0, 0
        while l < r:
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                res += maxl - height[l]
                l += 1
            else:
                maxr = max(maxr, height[r])
                res += maxr - height[r]
                r -= 1
        return res
