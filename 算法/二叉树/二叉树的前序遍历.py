# coding:utf-8
'''
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        递归
        """
        if not root: return []
        res = []

        def f(root):
            res.append(root.val)
            if root.left:
                f(root.left)
            if root.right:
                f(root.right)

        f(root)
        return res

    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        非递归
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return res

    def test(self,root):
        if not root: return []
        stack = [root]
        res =[]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res

