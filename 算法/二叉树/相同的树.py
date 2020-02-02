# coding:utf-8
'''
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false


头条文章
https://www.toutiao.com/a6657774953942745603/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1553571848&app=news_article&utm_source=weixin&utm_medium=toutiao_ios&group_id=6657774953942745603

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        暴力解法
        """
        return self.valid(q) == self.valid(p)

    def valid(self, root):
        res = []
        stack = [root]
        while stack:
            r = stack.pop()
            if r:
                res.append(r.val)
                stack.append(r.left)
                stack.append(r.right)
            else:
                res.append(r.val)
        return res

    def issameTree(self, p, q):
        '''
        :param p:
        :param q:
        :return:
        递归
        '''
        if not q and not p: return True
        if q and p:
            res = p.val == q.val
            res = res and self.issameTree(p.left, q.left)
            return res and self.issameTree(p.right, q.right)
        return False

    def test(self, p, q):
        if not q and not p: return True
        if q and p:
            res = q.val == p.val
            res = res and self.test(q.left, p.left)
            return res and self.test(q.right, p.right)
        return False
