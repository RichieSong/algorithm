# -*- coding: utf-8 -*-
"""
 左侧是排好序的 右侧是未排序的
"""


def sort(listA):
    for i in range(1, len(listA)):
        for j in range(i, 0, -1):
            if listA[j] < listA[j - 1]:
                listA[j], listA[j - 1] = listA[j - 1], listA[j]
            else:
                break
    print listA


if __name__ == '__main__':
    nums = [1, 5, 7, 9, 0, 6, 67, 4, 3, 34]
    sort(nums)
