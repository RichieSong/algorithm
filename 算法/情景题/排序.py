# -*- coding: utf-8 -*-
"""

有一个整形数组，包含正数和负数，然后要求把数组内的所有负数移至正数的左边，且保证相对位置不变，
要求时间复杂度为O(n), 空间复杂度为O(1)。
例如，{10, -2, 5, 8, -4, 2, -3, 7, 12, -88, -23, 35}变化后是{-2, -4，-3, -88, -23,5, 8 ,10, 2, 7, 12, 35}

1、for循环，单指针记录

"""


def sort1(nums):
    """空间复杂度O(n)"""
    left, right = 0, len(nums) - 1
    index = -1
    while left <= right:
        if nums[left] < 0:
            index += 1
            tmp = nums[left]
            nums.remove(tmp)
            nums.insert(index, tmp)
        left += 1
    print nums


def sort(nums):
    """空间复杂度O(1)"""
    j = 0
    for i in range(len(nums)):
        if nums[i] < 0:  # 当前元素小于0时候，进行交换
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    print nums


if __name__ == '__main__':
    array = [10, -2, 5, 8, -4, 2, -3, 7, 12, -88, -23, 35]
    sort(array)
