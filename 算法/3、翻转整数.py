# coding:utf-8
"""

给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。

"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        R = str(x)[::-1]
        R = int(R)
        if -2 ** 31 <= R <= 2 ** 31 - 1:
            return R * flag
        return 0

    def reverses(self, x):
        R = 0  # 返回值
        flag = 1  # 标记输入值的正负
        if x < 0:
            x = abs(x)
            flag = -1  # 输入是负数
        while x != 0:
            R = R * 10 + x % 10  # 十位数+余数
            x = x // 10

        if -2147483647 < R < 2147483648:  # 判断是否越界
            return R * flag
        else:
            return 0


if __name__ == '__main__':
    l = 1230123
    s = Solution()
    res = s.reverse(l)
    print(res)
