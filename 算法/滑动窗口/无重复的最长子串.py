# -*- coding: utf-8 -*-

def f(s):
    """个数"""
    if not s: return 0
    window = {}
    l, r = 0, 0
    res = 0
    length = len(s)
    while r < length:
        if s[r] in window:
            l = window[s[r]] + 1
            for k, i in window.copy().items():
                if i < l:
                    window.pop(k)
        window[s[r]] = r
        res = max(res, r - l + 1)
        r += 1

    return res


if __name__ == '__main__':
    s = "abcbdefhgdgdfg"
    print(f(s))
