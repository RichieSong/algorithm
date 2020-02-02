# coding:utf-8
"""
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 方法一
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        中序遍历：升序即可
        """
        inorder = self.search(root)
        return inorder == list(sorted(inorder))

    def search(self, root):
        if not root:
            return []
        return self.search(root.left) + [root.val] + self.search(root.right)


# 方法二
class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        中序遍历：升序
        """
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):  # 判断左子树
            return False
        if self.prev and self.prev.val >= root.val:  # 判断右子树
            return False
        self.prev = root
        return self.helper(root.right)

    def test(self, root):
        self.prev = None

        def helper(root):
            if root is None:
                return True
            if not helper(root.left):
                return False
            if self.prev and self.prev.val >= root.val:
                return False
            self.prev = root
            return helper(root.right)

        return helper(root)

    def test1(self, root):
        def search(root):
            if not root: return []
            return search(root.left) + [root.val] + search(root.right)

        return search(root) == sorted(search(root))
