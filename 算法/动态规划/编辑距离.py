# coding:utf-8
'''
https://leetcode-cn.com/problems/edit-distance/

https://www.youtube.com/watch?v=Mowr0huRJFA   讲解的非常经典

给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
示例 2:

输入: word1 = "intention", word2 = "execution"
输出: 5
解释:
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')



'''


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        dp[i][j],表示word1前i个字符替换word2前j个字符，最少需要的步数
        """
        m, n = len(word1), len(word2)
        # dp = [[0] * (n + 1)] * (m + 1)  # m,n matrix
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1),
                                   dp[i][j - 1] + 1, dp[i - 1][j] + 1
                                   )
        return dp[m][n]

    def test(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1), dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1)
        return dp[m][n]

    def test1(self, word1, word2):
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1), dp[i][j - 1] + 1,
                                   dp[i - 1][j] + 1)
        return dp[m][n]


if __name__ == '__main__':
    s = Solution()
    print(s.test1("abc", "bcdd"))
