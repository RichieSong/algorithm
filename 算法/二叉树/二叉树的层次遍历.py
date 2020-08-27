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
            res.append([])  # 添加结构
        res[level].append(node.val)  # 填充数据
        self._dfs(node.left, level + 1, res)
        self._dfs(node.right, level + 1, res)

    def levelOrder1(self, root):
        # bfs非递归
        res = []
        if root is None:
            return res
        queue = [root]
        # 列表为空时，循环终止
        # 可以省去len(queue)!=0
        while queue and len(queue) != 0:
            # 使用列表存储同层节点
            level_val = []
            # 同层节点的个数
            length = len(queue)
            for i in range(length):
                # 将同层节点依次出队
                h = queue.pop(0)
                if h.left:
                    # 左孩子入队
                    queue.append(h.left)
                if h.right:
                    # 右孩子入队
                    queue.append(h.right)
                level_val.append(h.val)
            res.append(level_val)
        return res

    def levelOrder4(self, root):
        """bfs非递归 双端队列"""
        res = []
        if not root:
            return res
        # 导包
        import collections
        # 双端队列定义
        queue = collections.deque()
        queue.append(root)
        # visited = set(root)
        while queue:
            length = len(queue)
            level_val = []
            for _ in range(length):
                # 弹出最左边的节点
                node = queue.popleft()
                level_val.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_val)
        return res

    def levelOrder3(self, root):
        """bfs递归"""
        if root is None:
            return []
        self.res = []
        self.bfs([root], 0)
        return self.res

    def bfs(self, level_nodes, level):
        if not level_nodes:
            return
        self.res.insert(level, [])
        temp = []
        for node in level_nodes:
            self.res[level].append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        self.bfs(temp, level + 1)

    def levelOrder2(self, root):
        # dfs递归
        # 特殊情况处理
        if not root:
            return []
        # 定义结果list
        self.result = []
        # 调用函数
        self.dfs(root, 0)
        # 返回结果
        return self.result

    # dfs函数
    def dfs(self, root, level):
        if not root: return
        # 这一行很关键，主要是用来为访问下一层的节点添加一个空的list
        if len(self.result) < level + 1:
            self.result.append([])
        # 访问对应level的list，并添加数据
        self.result[level].append(root.val)
        # 左孩子递归
        if root.left:
            self.dfs(root.left, level + 1)
        # 右孩子递归
        if root.right:
            self.dfs(root.right, level + 1)
