# -*- coding: utf-8 -*-
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

 

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]


"""
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):  # [8]
            if nums[i] > 0: break  # [7]
            if i > 0 and nums[i] == nums[i - 1]: continue  # [1]

            l, r = i + 1, length - 1  # [2]
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:  # [3]
                    l += 1
                elif total > 0:  # [4]
                    r -= 1
                else:  # [5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:  # [6]
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # [6]
                        r -= 1
                    l += 1
                    r -= 1
        return res

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        """重点解法"""
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:  # 判断重复数字
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(s.threeSum(nums))
