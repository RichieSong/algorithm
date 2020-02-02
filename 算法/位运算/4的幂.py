# coding:utf-8
'''
给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
'''


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        位运算 特点除了只有一个1外 而且后面的0个数为偶数
        """
        if num != 0 and num & (num - 1) == 0 and len(bin(num).split("1")[-1]) & 1 == 0:
            return True
        else:
            return False

    def isPowerOfFour1(self, num):
        """
        :type num: int
        :rtype: bool
        循环
        """
        while num:
            num = num / 4.0
            if num == 4:
                return True
            elif num < 4:
                break
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(16))
    print(s.isPowerOfFour1(64))
