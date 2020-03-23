# -*- coding: utf-8 -*-
"""

是一种通过探索所有可能的候选解来找出所有的解的算法。如果候选解被确认 不是 一个解的话（或者至少不是 最后一个 解），回溯算法会通过在上一步进行一些变化抛弃该解，即 回溯 并且再次尝试。

这里有一个回溯函数，使用第一个整数的索引作为参数 backtrack(first)。

如果第一个整数有索引 n，意味着当前排列已完成。
遍历索引 first 到索引 n - 1 的所有整数。Iterate over the integers from index first to index n - 1.
在排列中放置第 i 个整数，
即 swap(nums[first], nums[i]).
继续生成从第 i 个整数开始的所有排列: backtrack(first + 1).
现在回溯，即通过 swap(nums[first], nums[i]) 还原.

"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print s.permute(nums)