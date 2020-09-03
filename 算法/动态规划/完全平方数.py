# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/3 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

动态规格dp
dp[i] = min(dp[i],dp[i-j*j]+1) i代表当前数字, j*j表示平方数
"""
import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(n):
                if i - j * j >= 0:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
                else:
                    break
        return dp[-1]

    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float('inf')] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    n = 2342
    print(s.numSquares(n))
    print(s.numSquares1(n))
