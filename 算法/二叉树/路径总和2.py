# coding:utf-8
"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]



"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def helper(root, tmp):
            if not root: return
            tmp.append(root.val)
            if not root.left and not root.right and sum(tmp) == s:
                res.append(tmp[:])
            helper(root.left, tmp)
            helper(root.right, tmp)
            tmp.pop()

        helper(root, list())
        return res
