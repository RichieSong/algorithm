# -*- coding: utf-8 -*-
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。



解题思路：
1、借用字典记录，每个元素sord之后作为key，列表中元素作为value，遍历完之后，取字典中values()即可
2、利用asii，本质思想跟1差不多
2.1、遍历以空格分开的列表，每个元素为item
2.2、定义一个长度为26，元素为0的数组
2.3、遍历每个item，每个元素为i，将字符的asii值：(ord(i))-ord('a')的值的范围在[0,26]之间，放在对应的位置上，并计数
2.4、遍历完之后，将统计的值作为key，item作为value，放在定义在字典列表中
2.5、返回字典的values()




"""

from typing import *
import collections



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """常规方法"""
        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

    def groupAnagrams1(strs):
        """利用asii"""
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()
