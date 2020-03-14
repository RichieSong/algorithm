# -*- coding: utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
"""


def f(num):
    map = {')': '(', '}': '{', ']': '['}
    stack = []
    for l in num:
        if l not in map:
            stack.append(l)
        elif not stack or map[l] != stack.pop():
            return False
    return not stack


if __name__ == '__main__':
    num = ['(', ')', '{', '}', '[', ']']
    print f(num)
