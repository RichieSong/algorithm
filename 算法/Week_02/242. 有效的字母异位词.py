# -*- coding: utf-8 -*-
"""

解题思路：
1、常规做法，先排序，再对比
2、开辟两个字典，分别记录每个元素的个数，然后对比字典是否相同
3、开辟一个字典，遍历s，统计，遍历t，每个统计值减一，如果字典所有的值都为0，则代表True。
注意：假如t包含s呢？注意值得增减，防止异常报错
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """思路一"""
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        """思路二"""
        s_dic, t_dic = {}, {}
        for i in s:
            s_dic[i] = s_dic.get(i, 0) + 1
        for j in t:
            t_dic[j] = t_dic.get(j, 0) + 1
        return s_dic == t_dic

    def isAnagram2(self, s: str, t: str) -> bool:
        """思路一"""
