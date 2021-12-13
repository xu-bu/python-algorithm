from typing import List
from functools import *

#518
def test_1D_bag_problem():
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bag_weight = 4
    # 初始化: 全为0
    dp = [0] * (bag_weight + 1)
    #二维版本初始化
    # dp[i][j] 表示从下标为[0-i]的物品里任意取，放进容量为j的背包，价值总和最大是多少。
    # rows=len(weight)
    # dp=[[0 for i in range(bag_weight+1)]for j in range(rows)]
    # 当背包容量大于weight[0]时，必须把0号物品放进去，这样才能保证利益最大化
    # for j in range(1,bag_weight+1):
    #     if j>=weight[0]:
    #         dp[0][j]=value[0]
    #一维版本则不需要这个初始化

    # 二维版本
    # 根据状态转移公式决定i和j的遍历，因为要用到i-1，所以i必须从1开始,i为0的情况在初始化时已经考虑过了
    # for i in range(1,len(weight)):
    #     for j in reversed(range(bag_weight+1)):
    #         if (j - weight[i] >= 0):
    #             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
    #         else:
    #             dp[i][j] = dp[i - 1][j]


    # 必须先遍历物品, 再遍历背包容量
    for i in range(len(weight)):
        #必须反着遍历背包容量，下界是weight[i] - 1，因为目前是用容量为j的背包在[0,i]件物品之间选，如果容量j比物品i的重量小，那和在[0,i-1]之间选物品时的结果是一样的
        #如果是完全背包问题，则应该从小到大for j in range(weight[i],bag_weight+1)，因为每个物品可以拾取无数次
        for j in range(bag_weight, weight[i] - 1, -1):

            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    print(dp)


class Solution:
    #518
    # 不同组合算作不同结果的01完全背包问题
    def change(self, amount: int, coins: list[int]) -> int:
        #表示装满大小为amount的背包有多少种方式
        dp=[0 for _ in range(amount+1)]
        dp[0]=1
        # 必须是先遍历物品再遍历背包容积
        for each in coins:
            # 和01背包唯一的不同就是是正过来遍历j的
            for j in range(each,amount+1):
                # 目的为装满背包时的状态转移公式
                dp[j]+=dp[j-each]
        return dp[amount]

    #377
    # 不同排列算作不同结果的01完全背包问题
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp=[0 for _ in range(target+1)]
        dp[0]=1
        #和上面相反，必须是先遍历容量再遍历物品
        for i in range(target+1):
            for each in nums:
                if i>=each:
                    dp[i]+=dp[i-each]
        return dp[target]

if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1,1]
    target = 3
    print(solution.findTargetSumWays(nums,target))