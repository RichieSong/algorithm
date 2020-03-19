# -*- coding: utf-8 -*-

"""
如何在有序数组中指定的元素的第一个位置？

1、直接变量一遍 时间复杂度O(n)
2、二分查找 O(logn)
"""


def binarySearch(nums, value):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + ((r - l) >> 1)
        if nums[mid] > value:
            r = mid - 1
        elif nums[mid] < value:
            l = mid + 1
        else:
            while mid != -1:
                if nums[mid - 1] != value:
                    return mid
                mid -= 1
    return -1


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 90, 90, 90, 90, 100]
    print binarySearch(nums, 90)
