from typing import List
from functools import *
# 背包问题中需要根据不同判重标准，需要考虑先遍历物品还是先遍历背包容量以及正向遍历背包容量还是反向
#518

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