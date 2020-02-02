# coding:utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        h = ListNode(-1)
        cur = h
        # 判断链表是否为空
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        # 指针操作
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # 判断节点是否还有剩余数据
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return h.next

    def merge(self, l1, l2):
        h = ListNode(-1)
        cur = h
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return h.next

    def test(self,l1,l2):
        l = ListNode(-1)
        cur = l
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        while l1 and l2:
            if l1.val >= l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return l.next

