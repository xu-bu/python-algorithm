
import bisect
from collections import *
from functools import *
import heapq
import itertools
from heapq import *
from math import *
import string
from decimal import Decimal
from math import gcd
from sortedcontainers import SortedList
from typing import List, Union, Optional
import random
import copy

# general questions that can be solved by mono stack:
# keep max/min value when do window sliding
# to know next greater/smaller element for each element
class Solution:

    # 3578
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # ans for nums[:i]
        # dp[i+1]=sum(dp[start:i+1])
        dp = [0] * (n+1)
        # dp[0] should be 1 then we are able to calculate dp[1]=1
        dp[0]=1
        # sum of dp[start:i+1]
        preSum=1
        maxDeque = deque()
        minDeque = deque()
        start = 0
        MOD= (10**9 + 7)
        # i starts from 0 since we're calculating dp[i+1]
        for i in range(n):
            # keep the max and min at the start of the mono deque
            while maxDeque and nums[i] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[i])
            while minDeque and nums[i] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[i])
            while maxDeque and minDeque and maxDeque[0] - minDeque[0] > k:
                if nums[start] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[start] == minDeque[0]:
                    minDeque.popleft()
                preSum-= dp[start]
                start += 1
            dp[i+1] = (preSum) %MOD
            preSum += dp[i+1]
            preSum%= MOD
        return dp[-1]

if __name__ == '__main__':
    solution=Solution()
    s = "abcabcabcabc"
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution.maxSlidingWindow(nums,k))