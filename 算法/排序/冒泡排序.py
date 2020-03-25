# -*- coding: utf-8 -*-
"""
空间复杂度
"""


def bufferpool(array):
    lenth = len(array)
    for i in range(lenth - 1):
        for j in range(lenth - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
    print array


if __name__ == '__main__':
    nums = [1, 5, 7, 9, 0, 6, 67, 4, 3, 34]
    bufferpool(nums)
