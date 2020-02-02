#coding:utf-8
'''
https://www.youtube.com/watch?v=dgPabAsTFa8
KMP算法
BF(brute force)暴力搜索：非常慢
RK（BF的升级版）在bf基础上利用hash函数，即对每一个字串求哈希值，然后拿字串的哈希值跟模式串的hash值比较，

'''

def kmp_match(s, p):
    m = len(s)
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:  # 只去匹配前m-n个
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:  # for 循环中，如果没有从任何一个 break 中退出，则会执行和 for 对应的 else
            # 只要从 break 中退出了，则 else 部分不执行。
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret