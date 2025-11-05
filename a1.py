import bisect
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
    def maxValue(self, nums: List[int]) -> List[int]:
        preMax,sufMin=list(accumulate(nums, max)) ,list(accumulate(nums[::-1], min))[::-1]
        n=len(nums)
        ans=[]
        ans=[0]*n
        ans[-1]=preMax[-1]
        for i in range(n-2,-1,-1):
            if preMax[i]>sufMin[i+1]:
                ans[i]=ans[i+1]
            else:
                ans[i]=preMax[i]
        return ans

if __name__ == "__main__":
    solution = Solution()
    nums = [3,1,4,1,5]
    k = 3
    print(solution.maxValue([2,1,3]))
