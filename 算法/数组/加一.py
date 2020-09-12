# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/11 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""


def fuck(nums):
    for i in range(len(nums) - 1, -1, -1):
        if (nums[i] + 1) % 10 != 0:
            nums[i] += 1
            return nums
        else:
            nums[i] = 0
    nums.insert(0, 1)
    return nums
