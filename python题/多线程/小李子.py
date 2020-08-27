# -*- coding: utf-8 -*-
"""
通过以上对join()    setDaemon()方法的实验,我们总结如下:
程序运行是一个进程,一个进程最少有一个线程，这个线程就是主线程;执行一个主线程，
如果主线程又创建一个或多个子线程，主线程和子线程就分兵多路，分别运行，那么当主线程完成想退出时，
会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。就要加join()方法实现;
但是有时候我们需要的是，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon方法了
"""

import threading
import time


def read():
    i = 0
    while True:
        print('i')
        i += 1
        time.sleep(1)


def write():
    while True:
        s = input()
        if s == 'EXIT':
            break


if __name__ == '__main__':
    print('test begin...')

    tw = threading.Thread(target=write)
    tr = threading.Thread(target=read,daemon=True)
    tw.start()
    tr.start()
    ## join 主线程A创建子线程B，当B执行完成之后，再执行A主线程下面的内容
    ## daemon 主线程A创建了子线程B，此时B也是守护进程，当A结束了，不管主线程B执行是否完成，都会跟着A一起结束
    while True:
        time.sleep(1)
        print("主")

