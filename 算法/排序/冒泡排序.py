# -*- coding: utf-8 -*-
"""
空间复杂度
"""


def bufferpool(array):
    lenth = len(array)
    haschange = True
    for i in range(lenth - 1):
        haschange = False
        for j in range(lenth - 1 - i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
                haschange = True
    print array


if __name__ == '__main__':
    nums = [1, 5, 7, 9, 0, 6, 67, 4, 3, 34]
    bufferpool(nums)
