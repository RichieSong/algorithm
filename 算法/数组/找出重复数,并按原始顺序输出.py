# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/8/27 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""


def test(l):
    temp = {}
    res = []
    ret = []
    for i in l:
        if temp.get(i, 0) >= 1:
            res.append(i)
        else:
            temp[i] = temp.get(i, 0) + 1
    for i in l:
        if i in res and i not in ret:
            ret.append(i)
    return ret
