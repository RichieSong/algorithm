# -*- encoding: utf-8 -*-
"""
    :copyright: (c)  19/9/16 by Richie.Song.

给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoor" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]


思路1：words中全排列，对每个排列项 跟字符串s匹配，如果匹配成功，记录索引
思路2：从words中拿出来一个单词，进行s匹配，如果匹配成功，则从匹配成功的前或后截取相同长度的字符，
继续在words匹配，匹配成功，删除words中单词，继续匹配直到words中单词为空为止，如果有任何一个没匹配成功，代表没有匹配成功。

"""



class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        pass

