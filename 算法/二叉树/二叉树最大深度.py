# coding:utf-8
'''
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。

解题思路：
1、递归
2、
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        非递归  没想出来。。。。。。。。。。。。
        """
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
