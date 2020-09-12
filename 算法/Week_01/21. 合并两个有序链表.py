# -*- coding: utf-8 -*-

"""

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

解题思路：
1、迭代
2、递归
3、分治
"""
from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """迭代法"""
        if not l1: return l2
        if not l2: return l1
        pre_node = ListNode(-1)
        pre = pre_node
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return pre_node.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归:比迭代速度更快"""
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists1(l1.next, l2)
        return l1 or l2
