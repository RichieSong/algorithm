# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/11 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""


def fuck(nums):
    res = 0
    for i in nums:
        res ^= i
    rightone = res & (~res + 1)  # 取出最右边的1
    onlyone = 0
    for i in nums:
        if i & rightone != 0: # 只与都为1或都为0的数
            onlyone ^= i
    return onlyone, onlyone ^ res


if __name__ == '__main__':
    nums = [2, 3, 2, 1, 2, 3, 4, 2, 4, 5]
    print(fuck(nums))
