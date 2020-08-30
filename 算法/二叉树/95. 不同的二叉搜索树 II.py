# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/8/30 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.

给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。

示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int):
        def generateTrees(start, end):
            if start > end:
                return [None, ]
            alltree = []
            for i in range(start, end + 1):
                lefttree = generateTrees(start, i - 1)
                righttree = generateTrees(i + 1, end)
                for l in lefttree:
                    for r in righttree:
                        currtree = TreeNode(i)
                        currtree.left = l
                        currtree.right = r
                        alltree.append(currtree)
            return alltree

        return generateTrees(1, n) if n else []


if __name__ == '__main__':
    s = Solution()
    print(s.generateTrees(3))
