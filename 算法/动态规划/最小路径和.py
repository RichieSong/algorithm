# coding:utf-8
'''

https://leetcode-cn.com/problems/minimum-path-sum/submissions/

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        dp方程二维：试试一维的？？？
        """
        row, col = len(grid), len(grid[0])
        # dp = np.zeros((row, col), dtype=int)
        dp = [[0] * col] * row  # 有问题 不要这样用
        for i in range(row):
            for j in range(col):
                if i == 0:
                    if j == 0:
                        dp[i][j] = grid[i][j]
                    else:
                        dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

    def test1(self, grid):
        '''

        dp[i][j]=min(dp[i-1][j],dp[i][j-1])+nums[i][j]
        :param grid:
        :return:
        '''
        row, col = len(grid), len(grid[0])
        dp = [[0 for _ in range(col)] for _ in range(row)]
        for r in range(row):
            for c in range(col):
                if r == 0:
                    if c == 0:
                        dp[r][c] = grid[r][c]
                    else:
                        dp[r][c] = dp[r][c - 1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                else:
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
        return dp[-1][-1]


if __name__ == '__main__':
    arr = [
        [1, 3, 1],
        [1, 0, 1],
        [1, 2, 1]
    ]
    s = Solution()
    print(s.minPathSum(arr))
    print(s.test1(arr))
