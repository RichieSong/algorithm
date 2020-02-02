# coding:utf-8
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

https://leetcode-cn.com/problems/maximum-subarray/
'''


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i] 子序列最大和 空间O(n) 时间O(n)
        """
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp[i] 子序列最大和 空间O(1) 时间O(n)
        """
        endHere = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            endHere = max(endHere + nums[i], nums[i])
            res = max(res, endHere)
        return res

    def test(self,nums):
        end = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            end = max(end+nums[i],nums[i]) #-1 2 12 8 15 17 12
            res = max(end,res) #1 2 12 12 15 17 17
            print(end,res)
        return res



if __name__ == '__main__':
    s = Solution()
    nums = [1, -2, 3, 10, -4, 7, 2, -5]
    print(s.maxSubArray(nums))
    print(s.maxSubArray1(nums))
    print(s.test(nums))
