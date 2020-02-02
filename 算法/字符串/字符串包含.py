# coding:utf-8
'''
给定两个分别由字母组成的字符串A和字符串B，字符串B的长度比字符串A短。请问，如何最快地判断字符串B中所有字母是否都在字符串A里？

方法：
    先排序，在比较 （代码略）
    直接比较
'''


def f(str1, str2):
    '''
    :param str1: A
    :param str2: B
    :return: bool
    方法一
    '''
    flag = True
    for i in str2:
        if i not in str1:
            flag = False
    return flag


def f1(str1, str2):
    '''
    :param str1: A
    :param str2: B
    :return: bool
    方法二：BF暴力匹配
    '''
    s2_len = len(str2)
    s2 = str2
    s2_index = 0
    for s in str1:
        sub_str = s2[s2_index]
        if s == sub_str:
            s2_index += 1
        else:
            s2_index = 0


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


if __name__ == '__main__':
    str1 = "abcdfe"
    str2 = "bwc"
    print(kmp_match(str1, str2))
