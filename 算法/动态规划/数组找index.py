# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  2020/9/18 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.

有序数组:查出第一个重复数或指定的第一个索引
如:给定 [1,2,3,3,5,5,5,7,8,9,10]
指定3,返回2
指定5,返回4
"""


def f(nums, key):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (r - l) // 2
        if nums[mid] == key and nums[mid - 1] != key:
            return mid
        elif nums[mid] == key or nums[mid] > key:
            r -= 1
        elif nums[mid] < key:
            l += 1
    return -1

if __name__ == '__main__':
    n = [1,2,3,3,5,5,5,7,8,9,10]
    print(f(n,3))

