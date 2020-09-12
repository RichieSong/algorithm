# -*- coding: utf-8 -*-
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 示例：

输入：[1,8,6,2,5,4,8,3,7]
输出：49

双指针
"""


def f(nums):
    left, right = 0, len(nums) - 1
    maxarea = 0
    while left < right:
        if nums[left] < nums[right]:
            maxarea = max(maxarea, nums[left] * (right - left))
            left += 1
        else:
            maxarea = max(maxarea, nums[right] * (right - left))
            right -= 1
    return maxarea


if __name__ == '__main__':
    nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(nums)
