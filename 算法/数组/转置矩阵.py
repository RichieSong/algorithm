# coding:utf-8
'''
给定一个矩阵 A， 返回 A 的转置矩阵。

矩阵的转置是指将矩阵的主对角线翻转，交换矩阵的行索引与列索引。



示例 1：

输入：[[1,2,3],[4,5,6],[7,8,9]]
输出：[[1,4,7],[2,5,8],[3,6,9]]
示例 2：

输入：[[1,2,3],[4,5,6]]
输出：[[1,4],[2,5],[3,6]]

'''


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for a in range(len(A[0])):
            j = []
            for i in A:
                j.append(i[a])
            res.append(j)
        return res


if __name__ == '__main__':
    s = Solution()
    r = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.transpose(r))
