# -*- coding: utf-8 -*-
"""

n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。


"""
from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """利用模板"""
        res = []

        def backtrack(board, row):
            if row == len(board):
                res.append(board[:])
            for col in range(n):
                if not self.IsValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'

        return res

    def IsValid(self, board, row, col):
        pass

    def solveNQueens1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        难度 *****
        """

        def DFS(queues, xy_dif, xy_sum):  # xy_dif xy_sum 对角线
            p = len(queues)
            if p == n:  # 代表已经放满了
                result.append(queues)
                return
            for q in range(n):  # q==col
                if q not in queues and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queues + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []
        DFS([], [], [])
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
