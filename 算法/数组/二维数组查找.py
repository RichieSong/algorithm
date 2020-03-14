# -*- coding: utf-8 -*-
"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数

1、暴力解法：对数组第一行进行二分查找，再对数组第二行进行二分查找。
2、矩阵是有序的：利用二维数组由上到下，由左到右递增的规律。
那么选取右上角或者左下角的元素a[row][col]与target进行比较，
    当target小于元素a[row][col]时，那么target必定在元素a所在列的左边,即col--；
    当target大于元素a[row][col]时，那么target必定在元素a所在行的下边,即row++。

"""


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array) - 1
        cols = len(array[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target == array[i][j]:
                return True
            elif target < array[i][j]:
                i -= 1
            else:
                j += 1
        return False
