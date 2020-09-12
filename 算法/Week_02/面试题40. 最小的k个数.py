# -*- coding: utf-8 -*-
"""
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]
 
限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

解题思路:
1、先排序，在找最小k个数 因为大小限制 不推荐
2、大顶堆heapq

"""
from typing import *
import heapq


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """时间nlogn  空间O(k)"""
        if len(arr) <= k: return arr
        arr = sorted(arr)
        return arr[:k]

    def getLeastNumbers1(self, arr: List[int], k: int) -> List[int]:
        """大顶堆"""
        return heapq.nsmallest(k, arr)

    def getLeastNumbers2(self, arr: List[int], k: int) -> List[int]:
        """堆的实现"""
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)  # 堆化,递增，结果就是第一个元素必然是最小的
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)# 删除堆顶元素，即最小值
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans


if __name__ == '__main__':
    s = Solution()
    arr = [3, 2, 1, 0, 4, 5]
    k = 2
    print(s.getLeastNumbers2(arr, k))
