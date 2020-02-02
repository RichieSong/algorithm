#!/usr/bin/python
# encoding: utf-8


"""
@author:  
@contact:  
@time: 
"""
from mrjob.job import MRJob
import os
class WordCounter(MRJob):

    def mapper_init(self):
        # 下面代码获得输入文件的名字，可以根据文件名做不同的处理工作
        envs = os.environ
        fn = os.environ["mapreduce_map_input_file"]


    def mapper(self,key,line):

        # -----------------------------
        for word in line.split():
                yield word,1

    def reducer(self,word,count):
        yield word,sum(count)

if __name__=='__main__':

    WordCounter().run()