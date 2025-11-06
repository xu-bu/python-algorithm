import bisect
import collections
from functools import *
import heapq
import itertools
from heapq import *
import math
import string
from decimal import Decimal
from math import gcd
from sortedcontainers import SortedList
from typing import List, Union, Optional
import random
import copy
from math import inf

# 3669
MAX_NUM = 10**5 + 1
# get all divisors for all nums
divisors = [[] for _ in range(MAX_NUM)]
for num in range(MAX_NUM):
    for divisor in range(1, int(num**0.5) + 1):
        if num % divisor == 0:
            divisors[num].append(divisor)
            divisors[num].append(num // divisor)


class Solution(object):
    # 3669
    def minDifference(self, n: int, k: int) -> List[int]:
        maxDiff = inf
        ans = None

        # backtrack to iterate all possibilities of given number dividing
        def backtrack(i, num, path, maxInPath, minInPath):
            """
            i: index of path that we will set in this layer
            num: number we are going to divide
            path: divisors of num
            return: ans of given number
            """
            if i == k - 1:
                nonlocal maxDiff, ans
                # divided for k-1 times, the last one is the rest num itself
                maxInPath = max(maxInPath, num)
                minInPath = min(minInPath, num)
                currentDiff = maxInPath - minInPath
                if currentDiff < maxDiff:
                    path[i] = num
                    maxDiff = currentDiff
                    ans = path[:]
                return
            for divisor in divisors[num]:
                path[i] = divisor
                backtrack(
                    i + 1,
                    num // divisor,
                    path,
                    max(maxInPath, divisor),
                    min(minInPath, divisor),
                )

        backtrack(0, n, [0] * k, 0, inf)
        return ans

    # 491
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        ans = []

        def dfs(start):
            if start >= len(nums):
                if len(path) > 1:
                    ans.append(path[:])
                return
            # not choose then just recurse
            # only when this number is not used in path, we can recurse not choose
            if path and path[-1] != nums[start]:
                dfs(start + 1)
            if not path or path[-1] <= nums[start]:
                # choose and recurse
                path.append(nums[start])
                dfs(start + 1)
                # need to pop, otherwise it will influence when backtrack to previous layer
                path.pop()

        dfs(0)
        return ans


if __name__ == "__main__":
    s = Solution()
    nums = "23"
    print(s.minDifference(44, 3))
