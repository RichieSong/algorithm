# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    API for project pod monitor

    :copyright: (c)  19/11/3 by Richie.Song.
    :license: OPS, see LICENSE_FILE for more details.
"""


# 等边三角形
def printSan(n):
    for i in range(0, n):
        for y in range(0, n - i):
            w = ' '
            print(w, end="")
        s = '* ' * i
        print(s)


name = "小米"

def say_hello():
    '''hello'''
    print("hello1")
    print("hello2")
    print("hello3")


print(name)
