# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums) / 2)]

    def majorityElement1(self, nums: List[int]) -> int:
        """
        可以看做好几个不同军队抢夺一个高地，他们一对一消耗
        因为有个军队超过了n/2，经过消耗后，还有人活着
        :param nums:
        :return:
        """
        key = nums[0]
        count = 0
        for i in range(len(nums)):
            if nums[i] == key:
                count += 1
            else:
                count -= 1
            if count <= 0:
                key = nums[i + 1]
        return key


if __name__ == '__main__':
    n = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement(n))
