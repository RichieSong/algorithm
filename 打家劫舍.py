# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/11 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""
nums = [1 ,2, 3, 4, 5,]


def f(nums):
    if len(nums) <= 2: return max(nums)
    dp = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i]<0:
            continue
        dp[i] = max(dp[i - 1], dp[i - 2] + max(nums[i],0))
    return dp[-1]


if __name__ == '__main__':
# dp[i] = max(dp[i],dp[i-1]+nums[i])


