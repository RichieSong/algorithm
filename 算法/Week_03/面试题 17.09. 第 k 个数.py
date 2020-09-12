# -*- coding: utf-8 -*-
"""
有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，5，7，9，15，21。

示例 1:

输入: k = 5

输出: 9


解题思路：
跟49、丑数 解法一模一样


"""

class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp, a, b, c = [1] * k, 0, 0, 0  # res 存储丑数
        for i in range(1, k):  # 注意1也是丑数，但比较特殊，这里不用管，此时n-1的值就是我们要找的丑数
            n1, n2, n3 = dp[a] * 3, dp[b] * 5, dp[c] * 7
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1: a += 1  # 匹配之后，更新索引
            if dp[i] == n2: b += 1
            if dp[i] == n3: c += 1
        return dp[-1]
