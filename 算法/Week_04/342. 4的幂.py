# -*- coding: utf-8 -*-
class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num != 0 and num & (num - 1) == 0 and len(bin(num).split("1")[-1]) & 1 == 0:
            return True
        else:
            return False

    def isPowerOfFour1(self, num):
        if num <= 0: return False
        while num % 4 == 0:
            num /= 4
        return True if num == 1 else False
