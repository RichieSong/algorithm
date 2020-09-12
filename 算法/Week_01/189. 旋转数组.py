# -*- coding: utf-8 -*-
from typing import *

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]

说明:

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
要求使用空间复杂度为 O(1) 的 原地 算法。

解题思路：
刚拿到这个题是考虑O（1）的空间复杂度，即原来的元素上交换，但如何交换效率更能符合题目要求呢？
想了半天也没想出更优秀的解决方案：直接看答案吧 自己也只能想出暴力求解，时间复杂度O(n**2)吧 

无论怎么想都需要新建一个新的数组，不符合题意，符合题意的效率太低，无非就多遍历几次



看了答案之后 感觉自己太笨了

先说方法一：反转 k=3
原始数组                  : 1 2 3 4 5 6 7
反转所有数字后             : 7 6 5 4 3 2 1
反转前 k 个数字后          : 5 6 7 4 3 2 1
反转后 n-k 个数字后        : 5 6 7 1 2 3 4 --> 结果

方法二：环状替换  还没搞明白原理  


"""


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        """国外大神 几行代码解决，果然是大神，但是没看懂"""
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
        return nums

    def rotate1(self, nums, k):
        """反转更好理解一点点,但是代码有问题，执行不成功"""
        if len(nums)<=k:
            nums.reverse()
            return nums
        nums.reverse()
        numk, nume = nums[:k], nums[k:]
        numk.reverse()
        nume.reverse()
        nums[:k] = numk
        nums[k:] = nume
        return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 3, 4, 5, 6]
    k = 3
    # print(s.rotate(nums, k))
    print(s.rotate1(nums, k))
