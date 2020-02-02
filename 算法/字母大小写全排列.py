# coding:utf-8
'''
输入字符串： s=1a2b
输出 [1A2b 1a2b 1a2B 1A2B]
'''


def f(str):
    res = [""]
    for i in str:
        if i.isdigit():
            res = [c + i for c in res]
        else:
            res = [j + c for c in [i.lower(), i.upper()] for j in res]
    return res


if __name__ == '__main__':
    s = "s12bc"
    print(f(s))
