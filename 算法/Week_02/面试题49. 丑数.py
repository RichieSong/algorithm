# -*- coding: utf-8 -*-

"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。

 

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  

1 是丑数。
n 不超过1690。


解题思路：
压根没找到规律，数学概念不清晰，因子是什么？看了题解之后，竟然发现动态规划也能解题，看了代码之后，秒懂
1、动态规划
1.1、分别定义2、3、5的索引和res结果数组
1.2、遍历输入的n，n其实就作为索引来使用
1.3、dp方程 dp[i] = min(dp[a]*2,dp[b]*3,dp[c]*5)  a、b、c是各自的索引
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0  # res 存储丑数
        for i in range(1, n):  # 注意1也是丑数，但比较特殊，这里不用管，此时n-1的值就是我们要找的丑数
            n1, n2, n3 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n1, n2, n3)
            if dp[i] == n1: a += 1 # 匹配之后，更新索引
            if dp[i] == n2: b += 1
            if dp[i] == n3: c += 1
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))
