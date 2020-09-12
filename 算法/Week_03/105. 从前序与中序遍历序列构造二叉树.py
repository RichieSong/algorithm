# -*- coding: utf-8 -*-
"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

解题思路：

递归
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder): return  #判断终止条件
        root = TreeNode(preorder[0]) # 前序能直接找到根节点
        mid_index = inorder.index(preorder[0]) #获取根节点下标
        root.left = self.buildTree(preorder[1:mid_index + 1], inorder[:mid_index]) # 构建左子树
        root.right = self.buildTree(preorder[mid_index + 1:], inorder[mid_index + 1:]) # 构建右子树
        return root
