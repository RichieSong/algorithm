# coding:utf-8
'''
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = []
        res = 0
        for i in s:
            if i in l:
                l = l[l.index(i) + 1:]
            l.append(i)
            res = res if res > len(l) else len(l)
        return res

    def lengthOfLongestSubstring1(self, s):
        m = {}  #
        start = 0  # 最长无重复字串的首个index
        length = 0  # 最长无重复字串的长度
        for i, ch in enumerate(s):
            if not m.get(ch):
                m[ch] = 0
            if m.get(ch) >= start:
                start = m.get(ch) + 1
            if i - start + 1 > length:
                length = i - start + 1
            m[ch] = i

        return length


if __name__ == '__main__':
    s = Solution()
    str = "dvdfeghkg3232"
    print(s.lengthOfLongestSubstring(str))
    print(s.lengthOfLongestSubstring1(str))
