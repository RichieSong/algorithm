# coding:utf-8
'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

'''


class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            res.append(self.count(i))
        return res

    def count(self, n):
        count = 0
        while n:
            n = n & (n - 1)
            count += 1
        return count

if __name__ == '__main__':
    s =Solution()
    print(s.countBits(10))