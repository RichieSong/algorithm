# -*- coding: utf-8 -*-

"""
给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
进阶:

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """借用两个字典，用于计数，然后找到共同的数，1、如果计数相等，则乘以计数，2、如果不相等，则乘以两个字典的最小值"""
        n1_dic = {}
        n2_dic = {}
        res = []
        for n1 in nums1:
            n1_dic[n1] = n1_dic.get(n1, 0) + 1
        for n2 in nums2:
            n2_dic[n2] = n2_dic.get(n2, 0) + 1

        for n, c in n1_dic.items():
            if n2_dic.get(n) == c:
                res += [n] * c
            elif n in n2_dic:
                res += [n] * min(c, n2_dic.get(n))
        return res

    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """先排序，再用双指针法,空间复杂度为O(1)"""
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j, k = 0, 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]

    def intersect3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """先排序，再用双指针法,空间复杂度为O(n)"""
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        res = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res


if __name__ == '__main__':
    s = Solution()
    n1 = [54, 93, 21, 73, 84, 60, 18, 62, 59, 89, 83, 89, 25, 39, 41, 55, 78, 27, 65, 82, 94, 61, 12, 38, 76, 5, 35, 6,
          51,
          48, 61, 0, 47, 60, 84, 9, 13, 28, 38, 21, 55, 37, 4, 67, 64, 86, 45, 33, 41]
    n2 = [17, 17, 87, 98, 18, 53, 2, 69, 74, 73, 20, 85, 59, 89, 84, 91, 84, 34, 44, 48, 20, 42, 68, 84, 8, 54, 66, 62,
          69,
          52, 67, 27, 87, 49, 92, 14, 92, 53, 22, 90, 60, 14, 8, 71, 0, 61, 94, 1, 22, 84, 10, 55, 55, 60, 98, 76, 27,
          35,
          84, 28, 4, 2, 9, 44, 86, 12, 17, 89, 35, 68, 17, 41, 21, 65, 59, 86, 42, 53, 0, 33, 80, 20]
    # n1 = [4,9,5]
    # n2 = [9,4,9,8,4]
    print(sorted(s.intersect1(n1, n2)))
    nr = [54, 21, 73, 84, 60, 18, 62, 59, 89, 89, 41, 55, 27, 65, 94, 61, 12, 76, 35, 48, 0, 60, 84, 9, 28, 55, 4, 67,
          86, 33]
    print(sorted(nr))
