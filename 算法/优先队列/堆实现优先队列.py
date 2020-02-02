#coding:utf-8
'''
10亿取出top10
思路1，

这一题应用堆排序算法复杂度只有O(nlog k)，堆是完全二叉树的一种，最大堆就是最上面的数是最大的
该方法基于二叉树或者堆来实现，首先把数组前k个数字构建一个最大堆，然后从第k+1个数字开始遍历数组，如果遍历到的
元素小于堆顶的数字，那么久将换两个数字，重新构造堆，继续遍历，最后剩下的堆就是最小的k个数，时间复杂度O(nlog k)。

思路2：排序

'''
import heapq

def min_num(k,nums):
    smallest=heapq.nsmallest(k,nums)
    heapq.heapify(smallest) #
    return smallest


if __name__ == '__main__':
    nums = [274563,4, 2,31,23,123]
    small=min_num(4,nums)
    print(small)
    heapq.heappushpop(small,1)
    print(small)

