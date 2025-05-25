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


class Trie:
    def __init__(self) -> None:
        self.children = [None for _ in range(2)]
        self.end = False
        self.HIGH_BITS = 30

    def insert(self, num):
        for i in reversed(range(self.HIGH_BITS)):
            bit = (num>>i) & 1
            if bit == 0:
                if not self.children[0]:
                    self.children[0] = Trie()
                self = self.children[0]
            else:
                if not self.children[1]:
                    self.children[1] = Trie()
                self = self.children[1]
        self.end = True

    # def ifStartWith(self, num):
    #     mask = pow(2, self.HIGH_BITS-1)
    #     for i in range(self.HIGH_BITS):
    #         bit = num & mask
    #         if self.children[bit] == False:
    #             return False
    #         mask >>= 1
    #     return True

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        grid=[]
        for [parent,child] in hierarchy:
            if len(grid) <= parent:
                grid.extend([[] for _ in range(parent - len(grid) + 1)])
            grid[parent].append(child)
        @cache
        def dfs(i, budget,isHalf):
            if i == n:
                return 0
            ans = dfs(i + 1, budget)
            if budget >= present[i]:
                ans = max(ans, future[i] + dfs(i + 1, budget - present[i]))
            return ans
        
if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    print(solution.minMoves(["A..",".A.","..."]))
