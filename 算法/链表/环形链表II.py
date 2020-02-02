# coding:utf-8、
'''
https://leetcode-cn.com/problems/linked-list-cycle-ii/

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。



示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。

'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        其实就是判断有环无环 有就返回当前节点 无就返回None
        长短指针法
        """

        fast = slow = head
        while fast and fast.next.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
