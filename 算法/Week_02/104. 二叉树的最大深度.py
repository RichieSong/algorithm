# -*- coding: utf-8 -*-
"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。


解题思路：
1、递归
2、bfs
3、dfs
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """递归"""
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth1(self, root: TreeNode) -> int:
        """迭代"""
        if not root: return 0  # 条件
        level = 0
        queue = [root]
        while queue:
            n = len(queue)  # 将queue长度固定
            for i in range(n):
                node = queue.pop(0)  # 总是从第一个元素pop出来
                if node:  # 首先判断第一个节点不能为空
                    if node.left:  # 上面的if node判断不要的话 可以用node.left is not None
                        queue.append(node.left)
                    if node.right:  # 上面的if node判断不要的话 可以用node.right is not None
                        queue.append(node.right)
            level += 1
        return level
