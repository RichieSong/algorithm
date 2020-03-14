# -*- coding: utf-8 -*-
# 反转链表
"""
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def f(self, head):
        """链表中是否有环"""
        fast = slow = head
        while fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False

    def f1(self, head):
        """  给定 1->2->3->4, 你应该返回 2->1->4->3."""
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next  # 1
            b = a.next  # 保存节点2
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next







