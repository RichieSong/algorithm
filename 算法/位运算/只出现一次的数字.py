# coding:utf-8
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
            if dic[n] == 2:
                del dic[n]
        return dic.keys()[0]

    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思路
            限制线性时间复杂度且不使用额外空间。采用位运算异或^。

            交换律 a^b=b^a

            结合律 (a^b)^c=a^(b^c)

            与本身异或等于0 a^a=0

            与0异或等于本身 a^0=a

            例如

            4^1^2^1^2=4^1^1^2^2=4^(1^1)^(2^2)=4^0^0=4。
            ---------------------

        """
        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == '__main__':
    s = Solution()
    n = [1, 1, 2, 2, 3, 3, 4, 4, 7, 6, 8, 6, 5, 5, 7]
    print(s.singleNumber(n))
    print(s.singleNumber1(n))
