# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？



"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        if not root: return []
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if root:
            res.append(root.val)
            self.preorder(root.left, res)
            self.preorder(root.right, res)

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """迭代：利用栈，但技巧是遍历树的时候，先遍历右子树，再遍历左子树"""
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
