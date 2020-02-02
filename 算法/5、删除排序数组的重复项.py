# coding:utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = []
        for n in nums:
            if n not in res:
                res.append(n)
        return len(res), res


if __name__ == '__main__':
    s = Solution()
    res = s.removeDuplicates([1, 1, 2])
    print(res)
