# -*- coding: utf-8 -*-

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

解题思路：
1、双指针
慢指针指向0的元素
快指针指向非零元素
1.1、当满足上面的条件时，进行元素交换，同时快慢指针继续向下走
1.2、继续判断是否满足条件，直到快指针结束为止

"""

from typing import *


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        :param nums:
        :return:
        """
        if not nums: return nums
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
