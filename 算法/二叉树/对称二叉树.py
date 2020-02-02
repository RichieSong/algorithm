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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归方法
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.isSymmetric1(root.left, root.right)

    def isSymmetric1(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        if left.val == right.val:
            return self.isSymmetric1(left.left, right.right) and self.isSymmetric1(left.right, right.left)
        return False


# 非递归

class Solution1(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        res = [root.left, root.right]
        while res:
            # 1、判断res是否是对称的
            if res != res.reverse():
                return False
            # 2、遍历res，替换成子节点
            r = []
            while res:
                node = res.pop(0)
                r.append(node.left)
                r.append(node.right)
            res = r
            # 3、继续循环
        return True
