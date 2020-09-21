# coding:utf-8
"""

给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3


并查集核心思想：
1、初始化
- 每个元素的值都是它自己，比如数组array(2,23,45,7,54,5), root[0]=2 ,root[1]=23 下标为n 的元素值是arr[n]
2, 并集
- 找老大。 两个集合的跟节点合并
3，查
- 最后合并成一个多叉树


岛屿问题解决
1、染色 bfs/dfs
2、并查集
https://leetcode-cn.com/problems/number-of-islands/solution/dao-yu-lei-wen-ti-de-tong-yong-jie-fa-dfs-bian-li-/


"""
from typing import List


class Solution(object):
    def dfs(self, grid, r, c):
        grid[r][c] = 0
        nr, nc = len(grid), len(grid[0])
        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]: # 四个方向遍历
            if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1": # 防止越界 并且当前节点是还是陆地
                self.dfs(grid, x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    self.dfs(grid, r, c) # 目的是把陆地填成海洋 即 1改变成0

        return num_islands
