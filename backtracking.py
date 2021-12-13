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

class Solution(object):
    #491
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
                dfs(start+1)
            if not path or path[-1] <= nums[start]:
                # choose and recurse
                path.append(nums[start])
                dfs(start+1)
                # need to pop, otherwise it will influence when backtrack to previous layer
                path.pop()

        dfs(0)
        return ans


if __name__ == '__main__':
    s=Solution()
    nums="23"
    print(s.subsetsWithDup([1,1]))
