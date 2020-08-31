# coding:utf-8
'''
输入一个整形数组，数组里有正数也有负数。数组中连续的一个或多个整数组成一个子数组，每个子数组都有一个和。 求所有子数组的和的最大值，要求时间复杂度为O(n)。

例如输入的数组为1, -2, 3, 10, -4, 7, 2, -5，和最大的子数组为3, 10, -4, 7, 2， 因此输出为该子数组的和18。

方程：dp[i]=max(dp[i-1]+arr[i],dp[i])
'''


def MaxSubArray(array):
    currSum = 0
    maxSum = 0
    for i in range(len(array)):
        currSum = array[i] if array[i] > currSum + array[i] else currSum + array[i]
        maxSum = max(maxSum, currSum)
    return maxSum


a = [1, -2, 3, 10, -4, 7, 2, -5]
print(MaxSubArray(a))
