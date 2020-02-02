# coding:utf-8
"""
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

    def isPalindromes(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        i = 0
        while x > i:
            i = i * 10 + x % 10  #取字符串末尾字符 首次是1 再次12 接着123
            x /= 10 # 取字符串去掉末尾单个字符之后的字符 首次是1232 再次123
        return x == i or x == i / 10

if __name__ == '__main__':
    s=Solution()
    s.isPalindromes(12321)