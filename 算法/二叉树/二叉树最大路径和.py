# -*- coding: utf-8 -*-
"""
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_gain(node):
            nonlocal res
            if not root: return 0
            left = max(0, max_gain(node.left))
            right = max(0, max_gain(node.right))
            res = max(res, left + right + node.val)
            return max(left, right) + node.val
        res = float('-inf')
        max_gain(root)
        return res
