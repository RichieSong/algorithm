# coding:utf-8
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
        翻转链表
        """
        curr, prev = head, None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def reverselist(self, head):
        cur, pre = head, None
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        给定 1->2->3->4, 你应该返回 2->1->4->3.
        """
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next  # 2
            b = a.next  # 3
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next

    def checkCicle(self, head):
        """
        判断链表是否有环
        :param head:
        :return: bool
        """
        fast = slow = head
        while fast and fast.next.next and slow.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reversel(self,head):
        pre ,cur = None,head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre



if __name__ == '__main__':
    list_node1 = ListNode(1)
    list_node2 = ListNode(2)
    list_node3 = ListNode(3)
    list_node4 = ListNode(4)
    list_node5 = ListNode(5)
    list_node1.next = list_node2
    list_node2.next = list_node3
    list_node3.next = list_node4
    list_node4.next = list_node5
    s = Solution()
    res = s.reverseList(list_node1)
    print(res)
