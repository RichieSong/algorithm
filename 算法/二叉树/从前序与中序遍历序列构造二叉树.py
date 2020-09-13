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


解题思路:

通过先序遍历我们可以找到root，根据root我们可以再中序找到当前root对应的左右子树，

再递归对当前root的左右子树进行构造

(递归的时候别想多，把看到的一堆想成一个整体就好,想好递归终止条件，剩下的让程序去做吧，不然容易把自己陷入死循环弄得一头雾水)。

递归思想


"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: return

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])  # left = inorder[1:idx+1] right = inorder[idx+1:]
        root.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root
