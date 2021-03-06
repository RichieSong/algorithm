# coding:utf-8
'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
'''


class Solution:
    def Sqrt(self, x):
        if x == 0 or x == 1: return x
        low = 0
        mid = x // 2
        high = x
        while low <= high:  # 注意判断条件
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
            mid = (low + high) // 2
        return mid

    def mySort(self, x):
        r = x
        while r * r > x:
            r = (r - x / r) / 2
        return r


if __name__ == '__main__':
    s = Solution()
    print(s.Sqrt(4))
