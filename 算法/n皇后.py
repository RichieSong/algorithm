# coding:utf-8
'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

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
'''


class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        难度 *****
        """

        def DFS(queues, xy_dif, xy_sum):  # xy_dif xy_sum 对角线
            print queues, xy_dif, xy_sum
            p = len(queues)
            if p == n:  # 代表已经放满了
                result.append(queues)
                return
            for q in range(n):  # q==col
                if q not in queues and p - q not in xy_dif and p + q not in xy_sum:
                    DFS(queues + [q], xy_dif + [p - q], xy_sum + [p + q])

        result = []

        DFS([], [], [])
        # return result
        print result
        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
