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
    # 3835
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxDeque = deque()
        minDeque = deque()
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            while maxDeque and nums[maxDeque[-1]] < num:
                maxDeque.pop()
            maxDeque.append(r)
            while minDeque and nums[minDeque[-1]] > num:
                minDeque.pop()
            minDeque.append(r)
            while (nums[maxDeque[0]] - nums[minDeque[0]]) * (r - l + 1) > k:
                l += 1
                if maxDeque[0] < l:
                    maxDeque.popleft()
                if minDeque[0] < l:
                    minDeque.popleft()
            ans += r - l + 1
        return ans


if __name__ == '__main__':
    solution=Solution()
    s = "abcabcabcabc"
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution.maxSlidingWindow(nums,k))
