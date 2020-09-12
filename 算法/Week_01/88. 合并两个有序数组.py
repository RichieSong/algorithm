# -*- coding: utf-8 -*-
"""

给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]


解题思路：
跟合并两个链表一样的思路
此题鄙人采用指针法，但是其核心思想不变

"""
from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1_copy = nums1[:m]  # 截取长度为m的列表
        # nums1[:] = []  # 清空nums1

        ## 一行替换2行
        p1, p2, nums1_copy, nums1[:] = 0, 0, nums1[:m], []
        while p1 < m and p2 < n:  # 索引
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        # if p1 < m:  # 如果nums1还有剩余元素
        #     nums1[p1 + p2:] = nums1_copy[p1:]
        # if p2 < n:  # 如果nums2还有剩余元素
        #     nums1[p1 + p2:] = nums2[p2:]

        ## 上面四行代码替换成一行
        nums1[p1 + p2:] = nums1_copy[p1:] if nums1_copy[p1:] else nums2[p2:]

        return nums1


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 3, 5, 7, 0, 0, 0, 0, 0]
    nums2 = [2, 4, 6, 8]
    print(s.merge(nums1, 4, nums2, 4))
