# coding:utf-8
'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方
'''


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        while n:
            n /= 2.0
            print(n)
            if n == 1:
                return True
            elif n < 1:
                break
        return False

    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        位运算 特点是有且仅有一个位为1的二进制
        """
        if n != 0 and (n & (n - 1) == 0):
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(1))
