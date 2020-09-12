# -*- coding: utf-8 -*-
"""

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

解题思路：
二叉搜索树的特点：中序遍历是递增的
1、中序遍历之后，元素跟排序之后的元素对比
2、bfs，每个元素跟前一个元素比，一直大则ture


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """inorder"""
        res = []

        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)

        inorder(root)
        return res == list(sorted(set(res)))

    def isValidBST1(self, root: TreeNode) -> bool:
        inorder = self.search(root)
        return inorder == list(sorted(set(inorder)))

    def search(self, root):
        if root is None:
            return []
        return self.search(root.left) + [root.val] + self.search(root.right)

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.prev = None  # 定义一个前驱节点
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):  # 判断左子树
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)
