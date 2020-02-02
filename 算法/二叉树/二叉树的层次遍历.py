# coding:utf-8
'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

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
'''
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        bst 广度优先搜索
        """
        if not root: return []
        res = []
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            current_level = []
            for _ in range(size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(current_level)
        return res

    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        dst 深度优先搜索 先构造结构 在填充数据
        """
        if not root: return []
        res = []
        self._dfs(root, 0, res)
        return res

    def _dfs(self, node, level, res):
        if not node: return
        if len(res) < level + 1:
            res.append([]) # 添加结构
        res[level].append(node.val) # 填充数据
        self._dfs(node.left, level + 1, res)
        self._dfs(node.right, level + 1, res)
