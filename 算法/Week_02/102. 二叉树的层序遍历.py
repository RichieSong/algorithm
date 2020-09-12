# -*- coding: utf-8 -*-
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]


层次遍历也就bfs，广度优先
数据结构用队列，可以用列表模拟队列，也可以用语言自带deque or queue

"""
from typing import *
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """bfs 迭代：相对来说用队列就能实现"""
        if not root: return []
        res = []
        queue = [root]
        while queue:
            level_node = []
            temp = []
            for i in queue:
                level_node.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            res.append(level_node)
            queue = temp
        return res

    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        """递归"""
        if not root: return []
        res = []

        def bfs(nodes, level):
            level_node = []
            temp = []
            for i in nodes:
                level_node.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            res.append(level_node)
            if temp:  # 终止条件
                bfs(temp, level + 1)

        bfs([root], 0)
        return res
