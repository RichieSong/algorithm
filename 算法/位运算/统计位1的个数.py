# coding:utf-8
'''
n = n &(n-1) 排除最后位1的数值
n & -n  得到最后位1得数值
n&1 ==1 判断奇数偶数 相当于n%2 ==1
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            n = n & (n - 1) # 清理掉最后为1的位数
            count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(10))
