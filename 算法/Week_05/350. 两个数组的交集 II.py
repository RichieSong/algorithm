"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

"""
from typing import *


class Solution:
    """py3"""
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
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

    def intersect2(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        py2  更容易理解
        """
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
