# coding:utf-8
'''


'''


def mink(s, k):
    '''
    :param s: 原数组
    :param k: int
    :return: []
    '''
    array = sorted(s[:k], reverse=True)
    for i in s[k + 1:]:
        if i < array[0]:
            array[0] = i
            array = sorted(array, reverse=True)
    return array


if __name__ == '__main__':
    s = [3, 45, 6723, 234, 9, 8, 6545, 342, 344, 212, 31, 1, 2313, 23, 42334, 656, 767, 10, 67]
    m = mink(s, 3)
    print(m)
