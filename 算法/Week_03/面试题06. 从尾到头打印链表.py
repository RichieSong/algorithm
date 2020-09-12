# -*- coding: utf-8 -*-
"""

"""

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        """列表反转"""
        if not head: return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]

    def reversePrint1(self, head: ListNode) -> List[int]:
        """栈特性"""
        if not head: return []
        stack = []
        res = []
        while head:
            stack.append(head.val)
            head = head.next
        while stack:
            n = stack.pop()
            res.append(n)
        return res
