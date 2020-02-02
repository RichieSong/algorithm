# coding:utf-8
'''
三步翻转法：

对于这个问题，换一个角度思考一下。

将一个字符串分成X和Y两个部分，在每部分字符串上定义反转操作，如X^T，即把X的所有字符反转（如，X="abc"，那么X^T="cba"），那么就得到下面的结论：(X^TY^T)^T=YX，显然就解决了字符串的反转问题。

例如，字符串 abcdef ，若要让def翻转到abc的前头，只要按照下述3个步骤操作即可：

首先将原字符串分为两个部分，即X:abc，Y:def；
将X反转，X->X^T，即得：abc->cba；将Y反转，Y->Y^T，即得：def->fed。
反转上述步骤得到的结果字符串X^TY^T，即反转字符串cbafed的两部分（cba和fed）给予反转，cbafed得到defabc，形式化表示为(X^TY^T)^T=YX，这就实现了整个反转。

'''


def ReverseString(s, f, t):
    '''
    :param s: list[str]
    :param f: from: start point
    :param t: to: end point
    :return:
    '''

    while f < t:
        s[f], s[t] = s[t], s[f]
        f += 1  #
        t -= 1
    return s


if __name__ == '__main__':
    s = ["a", "b", "c", "d", "e", "f"]
    print(ReverseString(s, 0, len(s) - 1))
