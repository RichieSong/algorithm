# coding:utf-8
'''

输入一个整数数组，调整数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。要求时间复杂度为O(n)。

推荐：双指针
'''


def f(array):
    head = 0
    tail = len(array) - 1
    while head < tail:
        if array[head] & 1 == 0:  # 头是偶数 置换
            array[head], array[tail] = array[tail], array[head]
            tail -= 1
        else:
            head += 1
    return array


a = [1, 2, 5, 4, 3, 7, 6, 8, 9]
print(f(a))
