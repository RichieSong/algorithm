# coding:utf-8
import re

phone = "13612345678"
s = re.search(r"^1[35678]\d{9}$", phone).group()
h = re.findall(r"^1[356789][0-9]{9}$", phone)
print(s, h)
