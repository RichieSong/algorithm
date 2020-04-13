# coding:utf-8
'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的。
1、暴力破解
2、贪心算法： 不合适
3、DP： 类比走楼梯 O(i*j)
    状态： dp[i] 走到i台阶的最小步数 即最少零钱数 i表示总金额amount
    方程： dp[i] = min(dp[i],dp[i-coins[j]]+1) j就是coins的每个零钱面值
'''


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)  # 存储min
        dp[0] = 0  # 初始化
        for i in range(1, amount + 1):
            for j in coins:
                if j <= i:  # 判断能否构成兑换条件，只要总额比面值大就可以
                    dp[i] = min(dp[i], dp[i - j] + 1)
                    print(str(i) + " * " + str(j) + " = " + str(dp))
        return -1 if dp[amount] != float('inf') else dp[amount]  # dp[amount]就是结果

    def test(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                if i >= j:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


class Solution1:
    def coinChange(self):
        """
        float('inf') 代表无穷大

        :return:
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    coins = [2, 6, 7]
    amount = 16
    # 此方法不一定一定等于amount
    print(s.coinChange(coins, amount))
