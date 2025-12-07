from bisect import *
from collections import *
from functools import *
from heapq import *
from math import *
import string
from decimal import Decimal
from math import *
from sortedcontainers import SortedList
from typing import List, Union, Optional
import random
import copy
from itertools import *


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
            bit = (num >> i) & 1
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
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        combineList = [damage[i] + requirement[i] for i in range(n)]
        start, end = n - 1, n - 1
        healthRequirement = 0
        score = 0
        while start >= 0:
            if start == n - 1:
                healthRequirement = combineList[start]
            else:
                healthRequirement = damage[start] + max(
                    healthRequirement, requirement[start]
                )
            while hp < healthRequirement:
                if end==0: return score
                if requirement[end - 1] >= combineList[end]:
                    end -= 1
                else:
                    healthRequirement -= combineList[end] - requirement[end - 1]
                    end -= 1
            score += max(end - start + 1, 0)
            start -= 1
        return score


if __name__ == "__main__":
    solution = Solution()
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    print(solution.totalScore(2, [1,1], [1,1]))
