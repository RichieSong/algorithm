# coding:utf-8
'''
有n*n个格子，每个格子里有正数或者0，从最左上角往最右下角走，只能向下和向右，一共走两次（即从左上角走到右下角走两趟），
把所有经过的格子的数加起来，求最大值SUM，且两次如果经过同一个格子，则最后总和SUM中该格子的计数只加一次。
dp[i][j]=max(dp[i-1][j],dp[i][j-1])+arr[i][j]

'''


def f(array):
    n = len(array)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + array[i][j]
    return dp


arrary = [
    [1, 2, 13, 45],
    [14, 3, 2, 5],
    [5, 32, 4, 53],
    [4, 2, 12, 3]
]

print(f(arrary))
res = [[1, 3, 6, 11],
       [5, 8, 10, 16],
       [10, 43, 47, 100],
       [55, 57, 69, 103]]
