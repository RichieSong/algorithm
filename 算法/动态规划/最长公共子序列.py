# -*- coding: utf-8 -*-
"""
给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。

若这两个字符串没有公共子序列，则返回 0。

 

示例 1:

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0。

这类关于字符串公共的类型的题目，一般都采用二维数组
    a b c d e
a   1 1 1 1 1
c   1 1 2 2 2
e   1 1 2 2 3
--------------
    a b c d e
a   1 1 1 1 1
e   1 1 1 1 2
c   1 1 2 2 2
--------------
    a b c d e
d   0 0 0 1 1
a   1 1 1 1 1
e   1 1 1 1 2


动态方程：
1、如果对比字符串相同 text1[i]== text2[j]
dp[i][j] = dp[i-1][j-1] +1
2、如果对比的字符串不同
dp[i][j] = max(dp[i-1][j],dp[i][j-1])

"""


class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1) + 1
        n = len(text2) + 1

        dp = [[0 for _ in range(m)] for _ in range(n)]  # 可优化成一维
        for i in range(1, n):
            for j in range(1, m):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]



if __name__ == '__main__':
    text1 = "abcde"
    text2 = "dc"
    s = Solution()
    print s.longestCommonSubsequence(text1, text2)
