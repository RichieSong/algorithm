# coding:utf-8
"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。
"""


def f(nums):
    return sorted(nums)[len(nums) >> 1]


"""
求众数 II
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
"""


def f1(nums):
    if not nums: return []
    n = len(nums) / 3 + 1
    dic = {}
    res = []
    for i in nums:
        dic[i] = dic.get(i, 0) + 1
    for k, v in dic.items():
        if v >= n:
            res.append(k)
    return res


def majorityElement(nums):
    if not nums:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 1
    for n in nums:
        if n == candidate1:
            count1 += 1
        elif n == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = n, 1
        elif count2 == 0:
            candidate2, count2 = n, 1
        else:
            count1, count2 = count1 - 1, count2 - 1
    return [n for n in (candidate1, candidate2)
            if nums.count(n) > len(nums) // 3]


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 3,3, 2, 2, 2]
    print majorityElement(nums)
    print f1(nums)
