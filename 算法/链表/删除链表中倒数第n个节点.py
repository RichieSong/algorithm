# coding:utf-8
"""



"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def deleteNode(self, head, n):
        """
        :param n: 倒数第n个节点
        :return:
        思路：两个指针(fast,slow) 其中一个指针fast先走n步，然后两个指针同时走，当fast走都尾部的时候，slow就是要删除的节点
        """
        h = ListNode(-1)
        h.next = head
        fast = slow = h
        for _ in range(n + 1):
            fast = fast.next
        while fast:  # 双指针同时走
            fast = fast.next
            slow = slow.next
        # 删除slow指针操作
        slow.next = slow.next.next
        return h.next

    def delete(self,head,n):
        pre = ListNode(-1)
        pre.next = head
        fast = slow = pre
        for _ in range(n+1):
            fast =fast.next
        while fast:
            fast = fast.next
            slow  = slow.next
        slow.next = slow.next.next
        return pre.next
