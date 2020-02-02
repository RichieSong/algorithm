# coding:utf-8
'''
在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

'''


def f(array, n):
    '''
    :param array:[[],[]]
    :param n:
    :return: bool
    定位法
    '''
    if len(array) == 0: return False
    for line in range(len(array)):
        end = array[line][-1]
        if n > end:
            continue
        elif n < end: #
            # 二分法
            if n in array[line]:
                return True
        else:
            return True
    return False


array = [[1, 3, 7],
         [4, 5, 6],
         [8, 9, 19]]
print(f(array, 18))
