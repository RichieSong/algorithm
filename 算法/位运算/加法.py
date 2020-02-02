# coding:utf-8
'''

如果我们将两个数转换成二进制，则有 0+0=0，0+1=1，1+1=10，我们忽略掉进位的话就变成了0+0=0, 0+1=1, 1+1=0，这个时候我们完全可以把+替换成^。
但是如何处理进位呢？

我们会发现只有1+1时才发生进位，即1&1才进位，但是进位是进到前面一位的，所以我们要将进位的1再左移一位。这个时候我们将上述得到的两个新数再次执行异或，

如果没有进位的话，这将是最后我们要的结果，但是有可能还有进位。若还有进位的话，我们就要重复上面的步骤，一直到处理完所有的进位。

最后的结果将是异或不会再次遇到进位问题，得到最终结果。

我们如何判断异或不会遇到进位？根据两个数&的结果，如果有进位，&的结果一定不等于0，所以&的结果可以作为判断计算是否结束的条件。

参考地址：非常清楚
https://www.toutiao.com/i6649185274184073732/?tt_from=weixin&utm_campaign=client_share&wxshare_count=1&timestamp=1552287678&app=news_article&utm_source=weixin&iid=65405256203&utm_medium=toutiao_ios&group_id=6649185274184073732

'''


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b == 0:
            return a
        sum = a ^ b
        carry = (a & b) << 1
        return self.getSum(sum, carry)

    def test(self, a, b):
        if b == 0:
            return a
        sum = a ^ b
        carry = (a & b) << 1
        return self.test(sum, carry)


if __name__ == '__main__':
    s = Solution()
    print(s.getSum(-4, 9))
