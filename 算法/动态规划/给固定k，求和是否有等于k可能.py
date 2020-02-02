# coding:utf-8
'''
给一个数组
arr = [2,3,45,56,6,65,4,4,3,2]
k=24
返回bool

dp 动态规划
https://www.youtube.com/watch?v=Jakbj4vaIbE
选或不选

'''


def rec_subset(arr, i, k):
    '''

    :param arr: arr
    :param i: arr for len
    :param k: sum
    :return: bool
    '''
    if k == 0:
        return True
    elif i == 0:
        return arr[0] == k
    elif arr[i] > k:
        return rec_subset(arr, i - 1, k)
    else:
        return rec_subset(arr, i - 1, k - arr[i]) or rec_subset(arr, i - 1, k)  # 选或不选


import numpy as np


def dp_subset(arr, k):
    '''

    :param arr:
    :param k:
    :return:
    '''
    subset = np.zeros((len(arr), k + 1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for s in range(1, k + 1):
            if arr[i] > s:
                subset[i, s] = subset[i - 1, s]
            else:
                subset[i, s] = subset[i - 1, s - arr[i]] or subset[i - 1, s]
    return subset[-1, -1]


arr = [2, 3, 1, 4, 5, 6, 4, 3]
print(rec_subset(arr, len(arr) - 1, 40))
print(rec_subset(arr, len(arr) - 1, 38))
print(rec_subset(arr, len(arr) - 1, 34))
print(rec_subset(arr, len(arr) - 1, 30))
print(rec_subset(arr, len(arr) - 1, 28))
print("################")
print(dp_subset(arr, 40))
print(dp_subset(arr, 38))
print(dp_subset(arr, 34))
print(dp_subset(arr, 30))
print(dp_subset(arr, 28))
