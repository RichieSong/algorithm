# coding:utf-8
'''
输入一个字符串，打印出该字符串中字符的所有排列。
例如输入字符串abc，则输出由字符a、b、c 所能排列出来的所有字符串
abc、acb、bac、bca、cab 和 cba。
'''
# 方法一
from itertools import permutations

str = ["a", "b", "c"]
for p in permutations(str):
    print(p)


# 方法二 递归
def perm(s=""):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl
if __name__ == '__main__':
    print(perm("abc"))
