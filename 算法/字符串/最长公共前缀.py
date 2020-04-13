# -*- coding: utf-8 -*-
"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

"""
from typing import List


class Solution:
    """py3"""
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ss = list(map(set,zip(*strs)))
        print(ss)
        res = ''
        for i,c in enumerate(ss):
            x = list(c)
            if len(x)>1:
                break
            res+=x[0]
        return res

class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ''
        s1 = min(strs)
        s2 = max(strs)
        for i , c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1

if __name__ == '__main__':
    s=Solution()
    strs = ["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))