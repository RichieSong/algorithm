# -*- coding: utf-8 -*-

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        return self.Pow(x, n)

    def Pow(self, x, n):
        if n == 0: return 1.0
        half = self.Pow(x, n / 2)
        return half * half * x if n & 1 == 1 else half * half  # python 2
