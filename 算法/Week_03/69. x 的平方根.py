# -*- coding: utf-8 -*-
"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

二分+—分治
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, res = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

    def mySqrt1(self, x: int) -> int:
        """牛顿迭代法：记住即可"""
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r
