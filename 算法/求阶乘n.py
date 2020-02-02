# coding:utf-8
def f(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
if __name__ == '__main__':
    print(f(2))
    print(f(3))
    print(f(4))
    print(f(5))