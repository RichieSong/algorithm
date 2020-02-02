# coding:utf-8
'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.f(root.left, root.right)

    def f(self, q, p):
        if not q and not p:
            return True
        elif q and p and q.val == p.val:
            return self.f(q.left, p.right) and self.f(p.left, q.right)
        return False

    def test(self,root):
        if not root:return False
        return self.ff(root.left,root.right)

    def ff(self,q,p):
        if not q and not p:
            return True
        elif q and p and q.val==p.val:
            return self.ff(q.left,p.right) and self.ff(p.right,q.left)
        return False
