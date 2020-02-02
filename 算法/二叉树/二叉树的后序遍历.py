# coding:utf-8
'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        递归
        """
        if not root: return []
        res = []

        def f(root):
            if root.left:
                f(root.left)
            if root.right:
                f(root.right)
            res.append(root.val)

        f(root)
        return res

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        非递归 其实用了两个栈 第二个栈的倒序就是后序遍历 不容易察觉
        """
        if not root: return []
        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]
