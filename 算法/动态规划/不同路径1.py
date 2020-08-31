# -*- coding: utf-8 -*-
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？



例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9


分析：
n=m=3
1 0 0
0 0 0
0 0 1

结果
6 3 1
3 2 1
1 1 0

0 0 0
0 0 0

因为只能向下，向右走不能回去
所以当前只有两种可能

dp[i][j] = dp[i-1][j]+dp[i][j-1]
[[1, 1, 1],
[1, 2, 3],
[1, 3, 6]]
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        一维数组
        """
        cur = [1] * n
        for raw in range(1, m):
            for col in range(1, n):
                cur[col] += cur[col - 1]
                print(cur)
        return cur[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(7, 3))
    print(s.uniquePaths1(7, 3))
