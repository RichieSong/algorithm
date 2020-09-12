# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  20/9/9 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
    给您A，B两个整数，求A除以B的商和余数。
"""


def f(a, b):
    if b - a < 0: return 0, a
    s, y = a, b
    for i in range(1, b):
        if y - i * s < 0:
            return s, y
        else:
            s = i * s
    return s, y


if __name__ == '__main__':
    s = 1
    n = 2
