# -*- coding: utf-8 -*-\

def soul(nums):
    res = 0
    for i in range(1,len(nums)):
        if nums[i-1]>nums[i]:
            res+=nums[i-1]-nums[i]
    return res