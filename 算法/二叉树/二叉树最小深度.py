# coding:utf-8
'''
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。

示例:

给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回它的最小深度  2.
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        if not root: return 0 # 最终返回的结果
        if not root.left: return 1 + self.minDepth(root.right) # 如果左子树为空，找右子树
        if not root.right: return 1 + self.minDepth(root.left) # 如果右子树为空，找左子树
        leftDepth = self.minDepth(root.left) # 左子树深度
        rightDepth = self.minDepth(root.right) # 右子树深度
        return 1 + min(leftDepth, rightDepth)
