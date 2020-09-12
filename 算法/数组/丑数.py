# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/11 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0  # res 存储丑数
        for i in range(1, n):  # 注意1也是丑数，但比较特殊，这里不用管，此时n-1的值就是我们要找的丑数
            n1, n2, n3 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1: a += 1  # 匹配之后，更新索引
            if dp[i] == n2: b += 1
            if dp[i] == n3: c += 1
        return dp[-1]
