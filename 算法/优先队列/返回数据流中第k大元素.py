# coding:utf-8
'''
设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。

# 方法:
1,优先队列，即 堆 或二叉搜索树
2、排序 取k大元素

方法二。
小顶堆

取大元素用小顶堆：堆顶元素最小
取小元素用大顶堆：堆顶元素最大



'''
import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = heapq.nlargest(k, nums) # 取出当前k大的值
        print(self.pool)
        heapq.heapify(self.pool)  # 堆化：将list变成heap
        self.k = k

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            heapq.heappushpop(self.pool, val)
        print(self.pool)
        return self.pool[0] # 堆顶


if __name__ == '__main__':
    n = [1, 3, 4567, 2134, 78, 56, 2334, 54634, 34, 5, 34, 5, 34, 53, 45, 34, 5]
    k = KthLargest(4, n)
    print k.add(5000)
