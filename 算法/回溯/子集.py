# -*- coding: utf-8 -*-
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯
        """

        def callback(first=0, curr=[]):
            if len(curr) == k:
                res.append(curr[:])
            for i in range(first, len(nums)):
                curr.append(nums[i])
                callback(i + 1, curr)
                curr.pop()

        res = []
        for k in range(len(nums) + 1):
            callback()
        return res

    def subsets2(self, nums):
        """
        回溯2
        :param nums:
        :return:
        """
        n = len(nums)
        res = []

        def callback(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                callback(j + 1, tmp + [nums[j]])

        callback(0, [])
        return res

    def subsets1(self, nums):
        """递归，理解简单，效果明显 O(nlogn)"""
        res = [[]]
        for i in nums:
            res += [r + [i] for r in res]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3]
    # print s.subsets1(nums)
    print s.subsets2(nums)
