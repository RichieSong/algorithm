#!/usr/bin/python
# encoding: utf-8


"""
@author:  
@contact:  
@time: 
"""

from mrjob.job import MRJob
import os
import sys
class UserOrderJoin(MRJob):
    SORT_VALUES = True
    # 二次排序参数：http://mrjob.readthedocs.io/en/latest/job.html
    def mapper(self, _, line):
        fields = line.strip().split('\t')
        if len(fields) == 2:
            # user data
            source = 'A'
            user_id = fields[0]
            user_name = fields[1]
            yield  user_id,[source,user_name]
        elif len(fields) == 3:
            # order data
            source ='B'
            user_id = fields[0]
            order_id = fields[1]
            price = fields[2]
            yield user_id,[source,order_id,price]
        else :
            pass

    def reducer(self,user_id,values):
        '''
        每个用户的订单列表
        "01:user1"	"01:80,02:90"
        "02:user2"	"03:82,04:95"

        :param user_id:
        :param values:
        :return:
        '''
        values = [v for v in values]
        if len(values)>1 :
            user_name = values[0][1]
            order_info = [':'.join([v[1],v[2]]) for v in values[1:]]
            yield ':'.join([user_id,user_name]),','.join(order_info)




def main():
    UserOrderJoin.run()

if __name__ == '__main__':
    main()