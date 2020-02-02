#coding:utf-8
def f():
    for i in range(10):
        print(i)
        yield
if __name__ == '__main__':
    f = f()
    f.next()
    f.next()
    f.next()
    f.next()
    f.next()
    f.next()
    f.next()

# 斐波拉契数列
def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

for index, x in enumerate(fib()):
    if index == 10:
        break
    print("%s" % x),




