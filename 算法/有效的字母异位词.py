# coding:utf-8

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}
        for i in s:
            map_s[i] = map_s.get(i, 0) + 1
        for j in t:
            map_t[j] = map_t.get(j, 0) + 1
        return map_t == map_s
