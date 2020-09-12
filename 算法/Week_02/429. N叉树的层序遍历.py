# -*- coding: utf-8 -*-
"""
给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :


返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]


"""
from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """bfs,迭代"""
        if not root: return []
        res = []
        stack = [root]
        while stack:
            temp = []
            nodes = []
            for i in stack:
                temp.append(i)
                for c in i.children:
                    nodes.append(c)
            res.append(temp)
            stack = nodes
        return res

    def levelOrder1(self, root: 'Node') -> List[List[int]]:
        """dfs"""
        res = []

        def dfs(root, depth):
            if not root: return []
            if len(res) <= depth:
                res.append([])
            res[depth].append(root.val)
            for ch in root.children:
                dfs(ch, depth + 1)

        dfs(root, 0)
        return res
