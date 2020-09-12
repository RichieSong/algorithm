# -*- coding: utf-8 -*-
"""

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

 

进阶：

你能在线性时间复杂度内解决此题吗？

 

示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length


解题思路：
1、常规思路，见面试题，但不是最优解，也不满足此题的要求，虽然都是滑动窗口的题目，是此题的低阶版
2、双端队列实现
要点：
1) 线性的复杂度，即O(n)
2) 数值大小是海量的，肯定不能用一次将数据加载到内存的方法

所以基本锁定到 用堆(小顶堆，优先队列)，双端队列的数据结构来实现

3、动态规划

"""
from typing import *
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """使用列表模拟双端队列"""
        if not nums: return nums
        window, res = [], []  # window的第一个永远是最大元素下标
        for i, x in enumerate(nums):
            # 1、如果下标超了，并且window下标也超了 ，删除下标
            # 2、将当前元素x与下标为window[-1]的元素对比，如果x大，则剔除，同时将x下标添加window中
            # 3、当i+1 >=k时，将最大元素添加res
            if i >= k and window[0] <= i - k:  # 1
                window.pop(0)
            while window and nums[window[-1]] <= x:  # 2
                window.pop()
            window.append(i)
            if i >= k - 1:  # 3
                res.append(nums[window[0]])
        return res

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        """使用双端队列结构"""
        if not nums: return nums
        window, res = deque(), []  # window的第一个永远是最大元素下标
        for i, x in enumerate(nums):
            # 1、如果下标超了，并且window下标也超了 ，删除下标
            # 2、将当前元素x与下标为window[-1]的元素对比，如果x大，则剔除，同时将x下标添加window中
            # 3、当i+1 >=k时，将最大元素添加res
            if i >= k and window[0] <= i - k:  # 1
                window.popleft()
            while window and nums[window[-1]] <= x:  # 2
                window.pop()
            window.append(i)
            if i >= k - 1:  # 3
                res.append(nums[window[0]])
        return res
