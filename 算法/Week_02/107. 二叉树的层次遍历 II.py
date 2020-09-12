# -*- coding: utf-8 -*-
"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
解题思路：
1、按照正常逻辑遍历，得到的结果直接反转
2、bfs在层级上倒序实现

"""
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        queue = [root]
        while queue:
            res.insert(0,[])
            n = len(queue)
            for i in range(n):
                i = queue.pop(0)
                res[0].append(i.val)
                if i.left:
                    queue.append(i.left)
                if i.right:
                    queue.append(i.right)
        return res
