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
from operator import *


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
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        xorDict:dict[tuple[int],int] = {}
        curXor = 0
        ans = 0
        oddEvenSum = 0
        for end, num in enumerate(nums):
            oddEvenSum +=1 if num % 2 == 0 else -1
            curXor ^= num
            if curXor == 0 and end % 2 == 1 and oddEvenSum == 0:
                # maybe nums[:end+1] is a balanced subarray
                ans = max(ans, end + 1)
            if (curXor, -oddEvenSum) in xorDict:
                start=xorDict[(curXor, -oddEvenSum)]
                size = end - start+1
                if size % 4 == 0 and oddEvenSum == 0:
                    ans = max(ans, size)
            if (curXor, oddEvenSum) not in xorDict:
                xorDict[(curXor, oddEvenSum)] = end
        return ans


if __name__ == "__main__":
    solution = Solution()
    target = 11
    print(solution.maxBalancedSubarray([3, 1, 3, 2, 0]))
