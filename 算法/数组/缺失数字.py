# coding:utf-8

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        最能想到的方案：时间复杂度为O(n),但很多的查询都是无效的
        """
        for i in range(len(nums)):
            if i not in nums:
                return i
        return len(nums)

    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        位运算：时间复杂度中规中矩
        """
        res = len(nums)  # 当nums中有数字缺失的时候，for循环必然多出一个序列长度为len(nums)的数值，必须^消掉才可以
        for i in range(res):
            res ^= i
            res ^= nums[i]
        return res

    def missingNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


if __name__ == '__main__':
    s = Solution()
    nums = [9, 6, 4, 8,3, 5, 7, 0, 1]
    print(s.missingNumber1(nums))
