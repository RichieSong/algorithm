# -*- coding: utf-8 -*-
"""
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

示例:

输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。


解题思路：
本以为看错了，怎么会有这么简单的算法题
首先想到用一行代码搞定
1、内置函数
但不太死心，总感觉官方会有更优秀的方法，于是搜罗一会
2、原地计数
计算单词的数量，就等同于计数单词开始的下标个数
"""


class Solution:
    def countSegments(self, s: str) -> int:
        """效率高，空间新开辟"""
        return len(s.split())

    def countSegments1(self, s: str) -> int:
        """省空间，效率低"""
        res = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i - 1] == ' '):
                res += 1
        return res
