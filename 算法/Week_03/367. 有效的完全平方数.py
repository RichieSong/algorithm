# -*- coding: utf-8 -*-
"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False


解题思路：
二分法
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if not num: return True
        l, r = 0, num
        while l <= r:
            mid = (r + l) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False
    def isPerfectSquare1(self, num: int) -> bool:
        """牛顿迭代法"""

