# coding:utf-8
"""

给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。
滑动窗口每次只向右移动一位。

返回滑动窗口最大值。



技术栈：优先队列，
"""
from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        列表作为双端队列实现
        """
        if k == 1:
            return nums
        res = nums[:k]
        ns = nums[k:]
        ret = [max(res)] if res else []
        for data in ns:
            if res and len(res) == k:
                res.pop(0)
                res.append(data)
                ret.append(max(res))
        return ret

    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        双端队列实现
        """
        if k == 1:
            return nums
        res = deque(maxlen=k)
        res.extend(nums[:k])
        ns = nums[k:]
        ret = [max(res)] if res else []
        for data in ns:
            if res and len(res) == k:
                res.append(data)
                ret.append(max(res))
        return ret

    def maxSlidingWindow2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        双端队列实现
        """
        if not nums: return nums
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:  # window下标限制在k个元素之内，超过就剔除
                window.pop(0)
            while window and nums[window[-1]] <= x:  # 判断window里下标的元素与当前元素谁大，如果当前元素大，则剔除window下标
                window.pop()
            window.append(i)  # 将新元素下标添加到window
            if i >= k - 1:  # 当遍历的次数>=k次的时候，必有res输出
                res.append(nums[window[0]])
        return res

    def f(self, nums, k):
        if not nums: return nums
        window, res = [], []
        for i, x in enumerate(nums):
            if i <= k and window[0] <= i - k:
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 4, 2, 3, 3, 5, 3, 2]
