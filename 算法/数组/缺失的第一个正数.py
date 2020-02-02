# coding:utf-8
'''
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:

输入: [1,2,0]
输出: 3

示例 2:

输入: [3,4,-1,1]
输出: 2

示例 3:

输入: [7,8,9,11,12]
输出: 1
说明:

你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。

题目分析：本题的难点在于只能使用常数级别的空间，也就是说，不能开辟一个flag数组，若出现某个数，就将flag值标1，
最后看flag数组第一个为0的下标。本题的思路是从前往后将数放到它正确的位置上去。

举个例子，假设有序列[4,2,6,1,-3]，首先看第一个数4，它正确的位置应该是在序列的第4个位置（位置数从1开始，正确的位置是第一个位置放1，
第二个位置放2，第三个位置放3……最后我们只要看哪个位置放的不是理想的数，那么它就是第一个缺失的正数）。我们将4与第4个位置上的“1”进行交换，序列变成[1,2,6,4,-3]；
接着我们还是看第一个数，现在变成了“1”，它的确在它正确的位置，好了，我们再看第二个数2，也在正确的位置。第三个数6，
本来应该放在第6个位置，可是该序列总共就5个位置，所以不移动；第四个数4在它的正确位置，不动；第五个数是负数，不动。
最后，从前往后看，发现在第三个位置本该出现的3没有出现，所有该序列缺失的第一个正数是3。

所以归纳来说，将每个数放在它正确的位置，前提是该数是正数，并且该数小于序列长度，并且它正确位置上的那个数不是它，
也就是说，把4要放在第4个位置，要保证第4个位置上的数不是4，如果是4的话，交换前后没什么变换，把两个4移来移去，还会造成死循环。


'''


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[
                nums[i] - 1]:  # 该数是正数，该数大于等于序列长度 ，它正确的位置上的数不是它
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    def first(self, nums):
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 4]
    print(s.firstMissingPositive(nums))
    print(s.first(nums))
