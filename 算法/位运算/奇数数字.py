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
        res^=i
    return res

if __name__ == '__main__':
    nums = [1,1,2,3,3,2,3]
    print(fuck(nums))