# coding:utf-8
'''
2N个元素，有N+1个不同的元素，这些元素中有一个重复了N次

找出重复的元素

'''


def f(nums):
    a = set()
    for n in nums:
        if n in a: return n
        a.add(n)
