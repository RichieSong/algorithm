# -*- coding: utf-8 -*-
from typing import *

"""
leetcode: 
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

难度：简单

解决思路：
其实题目描述的很清楚，也很简单
1、是个排序数组
2、原地删除重复元素
3、返回移除之后的新长度
4、特别关注的一点，O(1)额外空间复杂度完成删除操作，意味着不允许开辟新的数组


## 方法一：借用字典来记录元素的个数，然后通过个数大于1，依次删除元素，只留下一个即可
这个方法大众都能想得到，也有可能太low了，说实话，做完之后想不出第二种方式来实现

## 方法二：快慢指针，这个不容易想到
特别优雅，重点推荐
i慢指针，j快指针
1、当nums[i] == nums[j] :j挑出重复项
2、当nums[i]!=nums[j]:将nums[j]赋值给nums[i+1],同时i向下再走一步
一秒即懂得动画：
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/shi-ping-dong-hua-jie-xi-bao-ni-dong-by-novice2mas/
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """虽然通过了，但效率太低"""
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1

        for num, c in count.items():
            if c > 1:
                for _ in range(1, c):
                    nums.remove(num)
        return len(nums)

    def removeDuplicates1(self, nums: List[int]) -> int:
        """双指针"""
        if not nums: return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1  # i向下走一步
                nums[i] = nums[j]  # 赋值，即原地替换
        return i + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1,1,3]
    print(s.removeDuplicates(nums))
    print(s.removeDuplicates1(nums))
