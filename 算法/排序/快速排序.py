# coding:utf-8
'''
快速排序 O(nlogn) 最糟糕O(n**2)
合并排序 总是O(nlogn) 但一般情况 快速更快

'''
from random import randint


def quickSort(array):
    if len(array) < 2:
        return array
    provit = array[0]  # 以第一个元素为基准值
    print(provit)
    less = [i for i in array[1:] if i <= provit]
    greater = [i for i in array[1:] if i > provit]
    return quickSort(less) + [provit] + quickSort(greater)


def quickSort1(array):
    if len(array) < 2:
        return array
    provit = array[randint(0, len(array))]  # 以随机一个元素为基准值
    print(provit)
    less = [i for i in array if i <= provit]
    greater = [i for i in array if i > provit]
    return quickSort(less)  + quickSort(greater)


if __name__ == '__main__':
    nums = [3, 6, 56, 7, 78, 89, 47, 5, 645, 4, 2, 33]
    print(quickSort(nums))
    print(quickSort1(nums))
