# -*- coding: utf-8 -*-
"""
数组中存有1-3的三种数字,
例如[1,2,3,1,2,2,1,3,3]，将其排序为[1,1,1,2,2,2,3,3,3]，
要求时间复杂度O(n)，后续将内容变为一个对象，继续排序
"""


def sort(nums):
    x, y = 0, len(nums) - 1
    for i in range(len(nums)):
        if i > y:
            break
        if nums[i] == 1:
            nums[x], nums[i] = nums[i], nums[x]
            x += 1
        elif nums[i] == 3:
            while y > 0:
                if nums[y] == 3:
                    y -= 1
                else:
                    break
            nums[y], nums[i] = nums[i], nums[y]
            if nums[i]==1:
                nums[x], nums[i] = nums[i], nums[x]
                x += 1
            y -= 1
    print nums

if __name__ == '__main__':
    nums = [2,3,2,1,3,1,2,3,1,2,2,1,3,3]
    sort(nums)