# coding:utf-8
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def reverseBST(self, root):
        if root:
            root.left, root.right = root.right, root.left
            self.reverseBST(root.left)
            self.reverseBST(root.right)
        return root

    def test(self, root):
        if not root: return False
        root.left, root.right = root.right, root.left
        self.test(root.left)
        self.test(root.right)
        return root

    def test1(self, root):
        if not root: return True
        root.left, root.right = root.right, root.left
        self.test1(root.left)
        self.test1(root.right)
        return root

    def test2(self, root):
        if not root: return root
        root.left, root.right = root.right, root.left
        self.test2(root.left)
        self.test2(root.right)
        return root
