# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  19/10/13 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.

    考察二叉搜索树的性质和遍历
    1,每个节点的数值比左子树大,比右子树小
    2,中序遍历就是从小到大的排序
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        if not root: return []
        res = []
        res += self.kthSmallest(root.left, k)
        if len(res) == k:
            return res[-1]
        res.append(root.val)
        res += self.kthSmallest(root.right, k)

    def k(self,root,k):
        stack = []
        res = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left

            else:
                root = stack.pop()
                if len(res) == k:
                    return res[-1]
                res.append(root.val)
                root = root.right
