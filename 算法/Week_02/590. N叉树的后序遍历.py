# -*- coding: utf-8 -*-
"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :


返回其后序遍历: [5,6,3,2,4,1].
 
说明: 递归法很简单，你可以使用迭代法完成此题吗?

"""

from typing import *
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """递归"""
        if not root:return []
        res = []
        def digui(root):
            if root:
                for i in root.children:
                    digui(i)
                res.append(root.val)
        digui(root)
        return res

    def postorder1(self, root: 'Node') -> List[int]:
        """迭代"""
        if not root:return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            for i in node.children:
                stack.append(i)
            res.append(node.val)
        return res[::-1]