# -*- coding: utf-8 -*-
"""
二面：分糖果  【3，2，1，2，3】  5个盒子 如果小孩拿到其中一个盒子的糖果 就不能拿相邻的盒子的糖果 问最多能拿到多少糖果？

#dp[i]定义最多的糖果数
      拿  不拿
i=0   3    0
i=1   2   3
i=2   1+3   2
i=3   2+2  4
i=4   3+4  4

dp[i] = max(dp[i-2]+array[i],dp[i-1])

"""



def f(nums):
    if not nums:return 0
    if len(nums)<=2:return max(nums)
    dp = [0]*len(nums)
    for i in range(len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]


if __name__ == '__main__':
    nums = [3,2,1,2,3]
    print f(nums)