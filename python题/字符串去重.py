# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/8/21 by Richie.Song.

"""
import time
import threading

def test1(i):
    li = str.split(",")
    d = set()
    for l in li:
        d.add(".".join(l.split(".")[-2:]))
    print(i)

if __name__ == '__main__':
    str = "ipos-set.wangyinbao.com,autom.wangyinbao.com,callb.wangyinbao.com,p2p0.wangyinbao.com,p2p.wangyinbao.com"
    start = time.time()
    for i in range(100):
        test1(i)
        # t = threading.Thread(target=test1,args=(i,))
        # t.start()
    end = time.time()
    print("aaa")
    print(end-start)
