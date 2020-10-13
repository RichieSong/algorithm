# -*- coding: utf-8 -*-
"""
给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

 

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:

输入: nums = [1], k = 1
输出: [1]
 

提示：

你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。

解题思路:
1、小顶堆(优先队列) 符合O(nlogn)时间复杂度
2、遍历数组，计数，然后找出最大的k个数

"""
from typing import *

import heapq
from collections import Counter
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """heapq python3"""
        import heapq
        from collections import Counter
        counter = Counter(nums)
        return heapq.nlargest(k, counter.keys(), key=counter.get)

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        """python2"""
        return zip(*collections.Counter(nums).most_common(k))[0]

    def topKFrequent3(self, nums, k):
        """python内建堆heapq"""
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()]  # 为堆化作准备
        print(max_heap)
        heapq.heapify(max_heap)  # 堆化,默认是大顶堆，堆顶元素最小，
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(s.topKFrequent3(nums, k))
