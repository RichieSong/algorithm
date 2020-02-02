#coding:utf-8
"""

合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6


解决思路：
1、两两合并
2、最后合并成大的链表
or
1、先合并前两个，成新的链表
2、在与第三个合并，依次合并


or

1、优先队列
2、多路归并
3、分治
4，最小堆

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """