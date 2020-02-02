# coding:utf-8
# 方法一
import re
from collections import Counter

d = Counter()
with open("./log.txt", "rb") as f:  # 以iter的方式读取，rb比r快6倍
    for l in f:
        ips = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", l)
        if len(ips) == 1:
            d.update({ips[0]: 1})
    print(d.most_common(100))
# 方法二
# with open("./log.txt", "r") as f: #适合大文件 每次读一行
#     d = {}
#     while True:
#         line = f.readline()
#         if not line:
#             break
# 方法三

# count = 1
# while True:
#     text = linecache.getline("./log.txt", count) # 有待验证是否适合大文件
#     count += 1
#     print(text)
#     if not text:
#         break
# 方法四
# text = linecache.getlines("./log.txt") # 不适合大文件 底层用的readlines
# print(text)
