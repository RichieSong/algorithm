# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """递归"""
        if not root: return []
        res = []

        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                res.append(root.val)

        postorder(root)
        return res

    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """迭代：利用stack，有个小技巧，先遍历左子树，在遍历右子树，保存val，看样子像后序遍历，其实将结果res反转就是了,效率比递归高"""
        if not root: return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
