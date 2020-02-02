# coding:utf-8
'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i]:最长上升《连续》子序列的长度
        dp[i]
        """
        if not nums: return 0
        dp = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
        return max(dp) + 1

    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i]:最长上升子序列的长度
        dp[i] 0(n**2)
        """
        if not nums: return 0

        dp = [1 for _ in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    nums = [2,2]
    print(s.lengthOfLIS(nums))
    print(s.lengthOfLIS1(nums))
