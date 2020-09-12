# -*- coding: utf-8 -*-

"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

输入: 38
输出: 2
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？

解题思路：
第一印象一看就是一看就是取模方法
1、取模


2、
"""


class Solution:

    def addDigits(self, num: int) -> int:
        """取模"""
        while num >= 10:
            num = num % 10 + int(num / 10)  # python3 默认结果是个浮点型，需要转换int
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))
