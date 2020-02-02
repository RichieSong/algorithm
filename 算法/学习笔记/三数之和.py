# coding:utf-8
"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# [-4,-1,-1,0,1,2]
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        技术栈：set、计数、 map 空间复杂度O(n),时间复杂度O(n^2)
        """
        res = set()
        if len(nums) < 3:
            return []
        nums.sort()
        for i, v in enumerate(nums[:-2]):  # 因为是三个数
            if i >= 1 and v == nums[i - 1]:  # 判断此次的值跟上一次的值相同，就没必要在执行一次循环了
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:  # 判断结果有没有
                    d[-x - v] = 1  # 计数
                else:
                    res.add((v, -v - x, x))
        return map(list, res)  # map

    def threeSum1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        技术栈：两边向中间压缩 空间复杂度O(1),时间复杂度O(n^2)
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return map(list,res)

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(
        s.threeSum(nums))
    print(s.threeSum1(nums))
