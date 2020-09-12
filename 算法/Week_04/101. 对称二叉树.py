# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.f(root.left, root.right)

    def f(self, q, p):
        if not q and not p:
            return True
        elif q and p and q.val == p.val:
            return self.f(q.left, p.right) and self.f(p.left, q.right)
        return False
