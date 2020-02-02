#!/usr/bin/env python
# encoding: utf-8


"""
@author:  
@contact:  
@time:


输出：
cat data/*|python mapper.py |sort -k1,2
1       A:BJ
1       B:1:1
1       B:2:2
1       B:3:2
1       B:5:3
2       A:TJ
2       B:4:3
3       A:BJ

"""

import sys

for line in sys.stdin:
    user_id = None
    product_id = None
    user_loc = None
    order_id = None
    source = None
    line = line.strip()
    if line == "":
        continue
    fields = line.split('\t')
    if len(fields) == 3:
        # user data
        source = 'A'
        user_id,_,user_loc = fields
        print '{0}\t{1}:{2}'.format(user_id,source,user_loc)

    elif len(fields) == 4:
        source = 'B'
        order_id,user_id,product_id,price = fields
        print '{0}\t{1}:{2}:{3}'.format(user_id,source,order_id,price)

