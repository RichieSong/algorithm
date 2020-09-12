# -*- coding: utf-8 -*-
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]

解题思路：
本质上是递归，想想递归模板
有时候自己人肉递归，会把自己绕进去，本人想个比较好的方法来理解递归
把每层递归想象成一个for循环：以此题为例
第一个递归==for循环
第二个递归==for的子循环
每次调用都调用2个for循环
因为他们每一层递归都有共用结果值，初始值=空字符
       ""    初始值
        |
        (    第一个for
      /   \
     ((    ()
     / \      \
  (((  (()          ()(
   /    \   \       /   \
 ((() (()) (()(    ()((   ()()
 /     /     \       /       \
((()) (())(  (()()   ()(()    ()()(
 |       |      |      \       \
 ((())) (())()  (()())   ()(())  ()()()



"""
from typing import *


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def _gen(left, right, n, res_str):
            if left == n and right == n:
                res.append(res_str)
                return
            if left < n: _gen(left + 1, right, n, res_str + "(")
            if right < left: _gen(left, right + 1, n, res_str + ")")

        _gen(0, 0, n, "")
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
