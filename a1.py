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
    def countPartitions(self, nums: List[int], k: int) -> int:
        n=len(nums)
        dp= [0] * n
        preSum = [0] * n
        dp[0]=1
        preSum[0] = 1
        maxDeque= deque([nums[0]])
        minDeque= deque([nums[0]])
        start=0
        for i in range(1, n):
            # keep the max and min at the left side of the deque
            if  len(maxDeque)==0 or nums[i] >= maxDeque[-1]:
                maxDeque.appendleft(nums[i])
            else:
                maxDeque.append(nums[i])
            if  len(minDeque)==0 or nums[i] <= minDeque[-1]:
                minDeque.appendleft(nums[i])
            else:
                minDeque.append(nums[i])
            
            while len(maxDeque) and len(minDeque)  and maxDeque[-1] - minDeque[-1] >= k:
                if nums[start] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[start] == minDeque[0]:
                    minDeque.popleft()
                start += 1
            dp[i] = (dp[i-1] + preSum[i-1])
            preSum[i] = (preSum[i-1] + dp[i])
        return dp[-1] % (10**9 + 7)
            
        
if __name__ == "__main__":
    solution = Solution()
    nums = [3,3,4]
    k = 0
    print(solution.countPartitions(nums, k)) 