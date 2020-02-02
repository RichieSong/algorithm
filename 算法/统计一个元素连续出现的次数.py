# coding:utf-8
'''
最大连续1的个数
给定一个二级制数组 计算其中最大连续1的个数？
比如 1110101001011111001011110
返回 11111 count = 5

输入的数组只包含0和1
输入数组的长度是正整数，且不超过1000
'''


# 方法1 计算元素1的个数放在字典并计数，如果遇见0，重新计数并将统计结果值存在列表或set中，遍历结束 统计max(list or set)  时间复杂度O(n)

# 方法2

def findMaxCountOnes(nums):
    res = count = 0
    for n in nums:
        if n:
            count += 1
        else:
            res = max(res, count)
            count = 0
    return max(res, count)


if __name__ == '__main__':
    nums = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(findMaxCountOnes(nums))
