# coding:utf-8
'''
输入一个数组和一个数字，在数组中查找两个数，使得它们的和正好是输入的那个数字。
要求时间复杂度是O(N)。如果有多对数字的和等于输入的数字，输出任意一对即可。
例如输入数组1、2、4、7、11、15和数字15。由于4+11=15，因此输出4和11。
'''


def f(array, target):
    '''
    :param array:
    :param target:
    :return: []
    解法一：暴力求解 o（n^2）
    解法二：o(n)
    '''
    for i, d in enumerate(array):
        s = target - d
        if s in array[i + 1:]:
            return d, s
    return


def f1(array, target):
    '''
    :param array:
    :param target:
    :return: []
    解法一：暴力求解 o（n^2）
    解法二：o(n)
    如果是有序的,二分法
    '''
    if len(array) < 2: return
    head = 0
    tail = len(array) - 1
    while head < tail:
        if array[head] + array[tail] < target:
            head += 1
        elif array[head] + array[tail] > target:
            tail -= 1
        else:
            return array[head], array[tail]
    return


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(f(a, 8))
    print(f1(a, 8))
