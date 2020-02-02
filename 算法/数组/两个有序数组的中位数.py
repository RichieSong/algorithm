# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/9/8 by Richie.Song.

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if ((len(nums2) + len(nums1)) % 2) == 0:
            l = (len(nums2) + len(nums1)) / 2
            flag = 1
        else:
            l = (len(nums2) + len(nums1)) / 2 + 1
            flag = 2
        if not nums1:
            return float(nums2[l] + nums2[l - 1]) / 2 if flag == 1 else nums2[l - 1]
        elif not nums2:
            return float(nums1[l] + nums1[l - 1]) / 2 if flag == 1 else nums1[l - 1]
        res = []
        while nums1 and nums2:
            if nums1[0] > nums2[0]:
                res.append(nums2[0])
                nums2.pop(0)
            else:
                res.append(nums1[0])
                nums1.pop(0)
            if len(res) >= l + 1:
                return float(res[l] + res[l - 1]) / 2 if flag == 1 else res[l - 1]

        while nums1:
            res.append(nums1[0])
            nums1.pop(0)
        while nums2:
            res.append(nums2[0])
            nums2.pop(0)
        return float(res[l] + res[l - 1]) / 2 if flag == 1 else res[l - 1]

    def NewMiddleNumber(self, num1, num2):
        nums = num1 + num2
        nums.sort()
        if len(nums) % 2 == 0:
            mid = float(nums[len(nums) / 2] + nums[(len(nums) / 2) + 1]) / 2
        else:
            mid = nums[nums(len(nums) / 2) + 1]
        return mid


if __name__ == '__main__':
    s = Solution()
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 3, 4, 5]

    print(s.findMedianSortedArrays(num1, num2))
