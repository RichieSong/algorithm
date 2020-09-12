# -*- coding: utf-8 -*-

"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321


解题思路：
1、解决数字为9的进位即可，利用数学倒序取模
1.1、当num % 10 !=0 时候，返回num + 1
1.2、当num % 10 ==0 时候，返回0
1.3、注意当最高位num % 10 ==0 时，数组前必须补个1
"""
from typing import *


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if (digits[i] + 1) % 10 != 0:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9]))
