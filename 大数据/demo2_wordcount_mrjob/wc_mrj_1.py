#!/usr/bin/python
# encoding: utf-8


"""
@author:  
@contact:  
@time: 
"""
from mrjob.job import MRJob
class WordCounter(MRJob):
    def mapper(self,_,line):
       for word in line.split():
           yield word,1

    def reducer(self,word,count):
        yield word,sum(count)

if __name__=='__main__':
    WordCounter().run()

