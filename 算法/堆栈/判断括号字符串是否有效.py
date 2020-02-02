# coding:utf-8
"""
技术栈：栈
"""


def isValid(s):
    map = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c not in map:
            stack.append(c)
        elif not stack or map[c] != stack.pop():  # 如果stack不为空或者 pop出的值是否跟map中value不一样
            return False
    return not stack


def isvalid(s):
    map = {"}": "{", "]": "[", ")": "("}
    stack = []
    for i in s:
        if i not in map:
            stack.append(i)
        elif not stack or stack.pop() != map[i]:
            return False
    return not stack


if __name__ == '__main__':
    s = "{()}"
    print(isValid(s))
    print(isvalid(s))
