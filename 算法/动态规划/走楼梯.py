# coding:utf-8
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

# from functools import lru_cache
from timeit import timeit


# class Solution:
# @lru_cache()  # 加了次装饰器速度会非常快，但是迭代次数过多会导致内存溢出
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    # 递归(回溯) 缺点：重复计算
    """
    return n if n <= 2 else climbStairs(n - 1) + climbStairs(n - 2)


def climbStairs1(n):
    """
    :type n: int
    :rtype: int
    # # 动态规划 (回溯+记忆化)
    """
    x, y = 1, 1
    for _ in range(1, n):
        x, y = y, x + y
    return y


#######################爬楼梯变种 ###################
# 1,每次可以走1，2，3步
# f(n)=f(n-1)+f(n-2)+f(n-3)

def climStairs(n):
    if n <= 2: return n
    if n == 3: return 4
    return climbStairs(n - 1) + climbStairs(n - 2) + climbStairs(n - 3)


def climStairs1(n):
    x, y, z = 1, 1, 2
    for _ in range(2,n):
        x, y, z = y, x + y, x + y + z
    return z


# 2、每次走1，2，3步，但不能有相邻相同的步伐

def climbStairs2(n):
    pass


if __name__ == '__main__':
    # s = Solution()
    # t = timeit('climStairs(1)', 'from __main__ import climStairs', number=1)
    # t = timeit('climbStairs(135)', 'from __main__ import climbStairs', number=1000)
    # tt = timeit('climbStairs1(135)', 'from __main__ import climbStairs1', number=1000)
    # print(t)
    # print(tt)
    print()
