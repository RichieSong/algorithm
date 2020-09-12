# -*- coding: utf-8 -*-
"""

94. 二叉树的中序遍历
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？


"""

from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        if not root: return []
        res = []
        self.get_data(root, res)
        return res

    def get_data(self, root, res):
        if root:
            self.get_data(root.left, res)
            res.append(root.val)
            self.get_data(root.right, res)

    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        """迭代，利用栈"""
        stack = []
        res = []
        p = root
        while p or stack:
            while p:  # 一直找左子树，直到没有左子树节点位置
                stack.append(p)  # 左子树节点存下来
                p = p.left
            p = stack.pop()  # 将最深层的节点从stack弹出
            res.append(p.val)  #
            p = p.right
        return res

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        p = lambda x: p(x.left) + [x.val] + p(x.right) if x else []
        return p(root)
