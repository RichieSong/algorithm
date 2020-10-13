"""
稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。

示例1:

 输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ta"
 输出：-1
 说明: 不存在返回-1。
示例2:

 输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], s = "ball"
 输出：4
提示:

words的长度在[1, 1000000]之间

直接遍历太粗糙了，效率低
方法：二分法
"""
from typing import *


class Solution(object):
    def findString(self, words, s):
        l, r = 0, len(words) - 1  # 左右指针
        mid = (l + r) // 2  # 初始化
        while l <= mid <= r:
            if words[mid]:  # 若words[mid]不为空字符串
                if words[mid] > s:  # 若words[mid]字符串比目标 s 大，则目标 s 一定在左半部分
                    r = mid - 1  # 则右指针减一
                    while l <= r and words[r] == "":  # 如果发现指针指向的字符串是空，就继续减一 直到找到非空字符串
                        r -= 1  # 注意条件中需要限制 右指针在左指针的右边
                elif words[mid] < s:
                    l = mid + 1
                    while l <= r and words[l] == "":
                        l += 1
                else:
                    return mid
                mid = (l + r) // 2
            else:  # 若words[mid]为空字符串，mid自增1。
                mid += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    n = "bll"
    print(s.findString(words, n))
