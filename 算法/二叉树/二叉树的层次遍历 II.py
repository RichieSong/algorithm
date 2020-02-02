# coding:utf-8
'''
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
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue = [root]
        res = []
        while queue:
            nodes = []
            node_val = []
            for node in queue:
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
                node_val += [node.val]
            res.append(node_val)
            queue = nodes
        return res[::-1]

