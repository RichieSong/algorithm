# -*- coding: utf-8 -*-
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mim_p = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > mim_p:
                res = max(prices[i] - mim_p, res)
            else:
                mim_p = prices[i]
        return res
