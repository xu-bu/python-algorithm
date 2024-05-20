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


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def traverse(self):
        p = self
        while p != None:
            print(p.val, end="->")
            p = p.next


class Column:
    def __init__(self):
        pass


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        pre = []
        count = collections.Counter([grid[i][0] for i in range(rows)])
        for i in range(10):
            heapq.heappush(pre, (-count[i], i))
        for i in range(1, cols):
            cur = collections.Counter([grid[i][0] for i in range(rows)])
            firstOps, firstNum = heapq.heappop(pre)
            firstOps = -firstOps
            for i in range(10):
                if i == firstNum:
                    firstOps, firstNum = heapq.heappop(pre)
                    firstOps = -firstOps

        return dp[cols - 1].bestOps


if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    grid = [
        [2, 4, 4, 3, 3, 6],
        [5, 0, 3, 3, 1, 0],
        [0, 4, 6, 1, 9, 0],
        [5, 7, 7, 2, 1, 3],
        [0, 6, 9, 8, 1, 2],
        [9, 4, 2, 1, 7, 7],
    ]
    for each in grid:
        for each2 in each:
            print(each2, end=" ")
        print()
    print(solution.minimumOperations(grid))
