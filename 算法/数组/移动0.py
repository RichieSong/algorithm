# -*- coding: utf-8 -*-

nums = [1, 2, 0, 3, 0, 2, 1]

l, r = 0, len(nums) - 1
while l <= r:
    if nums[l] != 0:
        l += 1
    else:
        tmp = nums[l]
        nums.remove(tmp)
        nums.insert(r, tmp)
        r -= 1


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 两个指针i和j
        j = 0
        for i in range(len(nums)):
            # 当前元素!=0，就把其交换到左边，等于0的交换到右边
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
