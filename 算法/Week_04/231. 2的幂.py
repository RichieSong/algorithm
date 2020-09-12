# -*- coding: utf-8 -*-
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        while n:
            n = n / 2.0
            if n == 1:
                return True
            elif n < 1:
                break
        return False

    def isPowerOfTwo1(self, n: int) -> bool:
        if n != 0 and (n & (n - 1) == 0):
            return True
        else:
            return False
