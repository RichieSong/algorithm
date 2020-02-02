# coding:utf-8
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        for k, v in dic.items():
            if v == max(dic.values()):
                return k

    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) >> 1]


if __name__ == '__main__':
    s = Solution()
    nums = [3, 3, 4, 4, 4, 1, 2, 2, 6, 6, 5, 4, 3]
    print(s.majorityElement(nums))
