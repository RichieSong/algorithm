# coding:utf-8
'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, result):
        '''
        :param left: 用完（ 的次数
        :param right: 用完 ）的次数
        :param n:
        :param result:
        :return: 剪枝思想  一直想不明白。。。
        '''
        if left == n and right == n:  # 左括号和右括号都用完即结束条件
            self.list.append(result)
            return
        if left < n:  # 左括号没用完
            self._gen(left + 1, right, n, result + "(")
        if left > right and right < n:  # 右括号没用完并且右括号必须比左括号少
            self._gen(left, right + 1, n, result + ")")


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
