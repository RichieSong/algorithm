# -*- coding: utf-8 -*-
"""
给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 



 

返回其前序遍历: [1,3,5,6,2,4]。

 

说明: 递归法很简单，你可以使用迭代法完成此题吗?

解题思路：
1、递归
2、迭代
"""

from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        """递归"""
        if not root:return []
        res = []
        def digui(root):
            if root:
                res.append(root.val)
                for i in root.children:
                    digui(i)
        digui(root)
        return res

    def preorder1(self, root: 'Node') -> List[int]:
        """迭代"""
        if not root:return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res

