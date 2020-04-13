# coding:utf-8
'''
dp练习

[1, 2, 3, 4, 5, 43, 2]

不相邻的数字之和最大

这里是 2+4+43 = 49


'''
import numpy as np


def dp_sum(arr):
    dp = np.zeros(len(arr))
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])
    for i in range(len(arr)):
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 1])
    return dp[-1]

# dp[i] = max(dp[i-2]+arr[i],dp[i-1])
arr = [1, 2, 3, 4, 5, 43, 2]
print(dp_sum(arr))
