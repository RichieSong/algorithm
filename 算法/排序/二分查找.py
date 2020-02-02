# coding:utf-8
"""
二分查找的必要条件：
1，必须是数组
2，必须是有序
3，不适合数据量太大或太小的情况，太大可能会申请内存失败(申请内存必须是连续的，而零散的内存会失败)，太小没必要，直接遍历即可
"""


# 最简单的二分查找
def bsearch(arr, length, value):
    """
    :param length: 数组长度
    :param value:  查找的值
    :return:
    """
    low = 0
    high = length - 1
    while high >= low:  # 注意一定是大于等于
        mid = (
                      low + high) / 2  # 有点问题 如果特别大的话，会导致内存溢出，优化方案：low+(high-low)/2  ,当然也可以用位运算，low+((high-low)>>1)相对于计算机来说位运算比除法会更难快
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# 常见的二分查找变型问题
# 查找第一个值等于给定的值的元素
def bsearch1(arr, length, value):
    """
    :param length: 数组长度
    :param value:  查找的值
    :return: int
    有重复元素
    [0,1,2,3,4,5,6,7,8,8,8,8,9,10] 给定值为8 找出下标为8的元素 return 8
    """
    low = 0
    high = length - 1
    while high >= low:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        elif arr[mid] > value:
            high = mid - 1
        else:
            if length == 0 or arr[mid - 1] != value:
                return mid
            else:
                high = mid - 1
    return -1


# 查找最后一个值等于给定值的元素
def bsearch2(arr, length, value):
    """
    :param length: 数组长度
    :param value:  查找的值
    :return: int
    有重复元素
    [0,1,2,3,4,5,6,7,8,8,8,8,9,10] 给定值为8 找出下标为11的元素 return 11
    """
    low = 0
    high = length - 1
    while high >= low:
        mid = low + ((high - low) >> 1)
        if arr[mid] > value:
            high = mid - 1
        elif arr[mid] < value:
            low = mid + 1
        else:
            if mid == length - 1 or arr[mid + 1] != value:
                return mid
            else:
                low = mid + 1
    return -1


# 查找第一个值大于等于给定值的元素
def bsearch3(arr, length, value):
    """
    :param length: 数组长度
    :param value:  查找的值
    :return: int
    [0,1,2,3,4,5,7,8,8,8,8,9,10] 给定值为6 找出下标为6的元素 return 6
    """
    low = 0
    high = length - 1
    while high >= low:
        mid = low + ((high - low) >> 1)
        if arr[mid] < value:
            low = mid + 1
        else:
            if mid == 0 or arr[mid - 1] < value:
                return mid
            else:
                high = mid - 1
    return -1


# 查找最后一个值小于等于给定值的元素
def bsearch4(arr, length, value):
    """
    :param length: 数组长度
    :param value:  查找的值
    :return: int
    [0,1,2,3,4,5,7,8,8,8,8,9,10] 给定值为6 找出下标为5的元素 return 5
    """
    low = 0
    high = length - 1
    while high >= low:
        mid = low + ((high - low) >> 1)
        if arr[mid] > value:
            high = mid - 1
        else:
            if mid == length - 1 or arr[mid + 1] > value:
                return mid
            else:
                low = mid + 1
    return -1


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr1 = [0, 1, 2, 3, 6, 7, 8, 8, 8, 8, 9, 10]
    # print(bsearch(arr, 10, 11))
    print(bsearch1(arr1, len(arr1), 8))
    print(bsearch2(arr1, len(arr1), 5))
    print(bsearch3(arr1, len(arr1), 4))
