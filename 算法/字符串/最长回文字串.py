# coding:utf-8
'''
https://leetcode-cn.com/problems/longest-palindromic-substring/

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

基本思路是对任意字符串，如果头和尾相同，
那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。
如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        dp[i][j] 代表从i到j的最长回文字串数
        dp[i][i]=1 永远是1
        dp[i][j]=dp[i+1][j-1]+2  # 如果字符串的头和尾相同，即s[i]==s[j]
        dp[i][j]=max(dp[i+1][j],dp[i][j-1])# 如果字符串的头和尾不相同，即s[i]！=s[j]
        """
        pass

    def longestPalindrome1(self, s):
        n = len(s)
        maxl = 0
        start = 0
        for i in range(n):
            if i - maxl >= 1 and s[i - maxl - 1: i + 1] == s[i - maxl - 1: i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            if i - maxl >= 0 and s[i - maxl: i + 1] == s[i - maxl: i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start: start + maxl]

    # 这个好理解
    def test1(self, s):
        if not s: return ""
        res = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and s[i:j + 1] == s[i:j + 1][::-1]:
                    res = s[i:j + 1] if len(s[i:j + 1]) > len(res) else res
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.test1("aabbcbba"))
