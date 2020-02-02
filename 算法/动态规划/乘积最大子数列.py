# coding:utf-8
'''
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        暴力求解
        O(n^2)
        """
        len_nums = len(nums)
        maxResult = nums[0]
        for i in range(len_nums):
            x = 1
            for j in range(i, len_nums):
                x *= nums[j]
                if x > maxResult:
                    maxResult = x
        return maxResult

    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp：动态规划
        O(n)
        """
        nums_len = len(nums)
        maxend = nums[0]
        minend = nums[0]
        maxResult = nums[0]
        for i in range(1, nums_len):
            end1, end2 = maxend * nums[i], minend * nums[i]
            maxend = max(max(end1, end2), nums[i])
            minend = min(min(end1, end2), nums[i])
            maxResult = max(maxResult, maxend)
        return maxResult

    def test(self, nums):
        maxnum = nums[0]
        minnum = nums[0]
        resnum = nums[0]
        for i in range(1, len(nums)):
            end1, end2 = maxnum * nums[i], minnum * nums[i]
            maxnum, minnum = max(end1, end2, nums[i]), min(end1, end2, nums[i])
            resnum = max(resnum, maxnum)
        return resnum


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 2, -3, 5, -2, -5]
    print(s.maxProduct(nums))
    print(s.maxProduct1(nums))
