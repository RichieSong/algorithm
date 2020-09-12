# coding:utf-8
'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:

输入: [1,3,4,2,2]
输出: 2
示例 2:

输入: [3,1,3,4,2]
输出: 3
说明：

不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        通常能想到的方案
        """
        d = {}
        l = len(nums)
        for i in range(l):
            d[nums[i]] = d.get(nums[i], 0) + 1
        for k, v in d.items():
            if v > 1:
                return k

    def findDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        想象成链表，判断是否有环,利用快慢指针
        空间复杂度为1，时间复杂度为n

        [3,1,3,4,2]
        首先第一个数字3指向下标3的数字4，

        数字4指向下标4的数字2

        数字2指向下标2的数字3

        数字1指向下标1的数字1


        举例来说，假设我们有一个数组是nums[]=[1，2，3，4，5，5，6，7]，
        pf代表快指针，ps代表慢指针，初始ps指向nums[0]，即1，
        pf指向nums[nums[0]]，即2,
        行动一次后，ps指向nums[1],即2，pf指向nums[nums[2]],即4，
        再动一次，ps指向nums[2],即3，pf则指向了nums[nums[4]],即5；
        可以发现pf一旦指向5后便不会再动，因为nums[5]一直为5，直到ps慢慢追上，
        然后令pf从头开始，ps一直在5处停留，最后定会相遇在这里，而这里就是重复数字。这里举了个最简单的例子，是为了方便大家理解，
        实际上实际的圆环顺序与数组的顺序是没有关系的，不信可以自己在纸上画一画，当数组变成nums[]=[4,6,5,1,3,2,5,7]的样子，你会更加理解这个算法的！

        """
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]
            fast = 0
            while slow != fast:
                fast = nums[fast]
                slow = nums[slow]
            return slow
        return -1


class Solution1:
    def findRepeatNumber(self, nums: [int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

    def findRepeatNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(s.findDuplicate(nums))
    print(s.findDuplicate1(nums))
