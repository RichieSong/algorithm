# coding:utf-8
'''
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
A&-A = A原码的最后一个1代表的数字。

求这个有什么用呢？

在数组中所有的数字异或之后，得到的数字是两个只出现过一次的数字的异或值，因为出现过两次的数字，就是自身异或自身得0，所以异或完后得到的就是两个要求的数的异或值。

其次，这个1代表什么呢？代表这两个要求的数在这一位不同，因为异或是相同为0，不同为1，所以既然求得了1，所以两个数在这一位上一定不相同，那么这样就好求了，首先对于多有的数异或，求得结果后与自己的相反数做与操作得到res。然后对于数组中多有的数，如果 num&resInt == 1 说明该数在这一位为1。用一个数res[0]不断相与，最后得到一个数就是要求的数之一。 如果 num&resInt == 0 说明这些数该位为0，用另一个数res[1]不断异或这些数，得到的就是另一个我们要求的数
'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        如何用位运算实现
        """
        result = [0, 0]
        res = 0
        for n in nums:
            res ^= n
        res &= -res  # 得到最后一个为1的
        for n in nums:
            if n & res == 0:
                result[0] ^= n
            else:
                result[1] ^= n
        return result


if __name__ == '__main__':
    s = Solution()
    n = [1, 2, 1, 3, 2, 5, 3, 6]
    print(s.singleNumber(n))
