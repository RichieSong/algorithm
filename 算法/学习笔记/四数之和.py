# coding:utf-8
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        向中间压缩的方式 O(n^3)
        """
        res = set()
        if len(nums) < 4:
            return []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.add((nums[i], nums[j], nums[l], nums[r]))
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return map(list, res)

    def fourSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        方法二 O(n^3) 有点问题
        """
        res = set()
        if len(nums) < 4:
            return []
        nums.sort()
        for i, v in enumerate(nums[:-3]):
            for j, vv in enumerate(nums[i + 1:-2]):
                if j > 1 and vv == nums[j - 1]:
                    continue
                d = {}
                for k in nums[j + 1:]:
                    if k not in d:
                        d[target - v - vv - k] = 1
                    else:
                        res.add((v, vv, k, target - vv - v - k))
        return map(list, res)


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,-1,0,-2,2]
    print(s.fourSum(nums, 0))
    print(s.fourSum1(nums, 0))
