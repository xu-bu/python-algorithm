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
from token import COLON

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
    def minMoves(self, matrix: List[str]) -> int:
        portalDic=collections.defaultdict(list)
        rows,cols=len(matrix),len(matrix[0])
        visited=[[False for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                c=matrix[i][j]
                if c!='.' and c!='#':
                    portalDic[c].append((i,j))
        @cache
        def dfs(i,j,mask):
            candidates=[]
            visited[i][j]=True
            for [x,y] in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                if 0<=x<rows and 0<=y<cols :
                    if visited[x][y]:
                        continue
                    c = matrix[x][y]
                    if c=='#':
                        continue
                    candidates.append(dfs(x,y,mask))
                    if c!='.' and not mask&(1 >> (ord(c) - ord('A'))):
                        mask = mask | (1 >> (ord(c) - ord('A')))
                        candidates+=[dfs(px,py,mask) for [px,py] in portalDic[c]]
            if len(candidates)==0:
                return float('inf')
            return 1+min(candidates)
        return dfs(0,0,0)



if __name__ == "__main__":
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    print(solution.minSwaps( [268835996,65052660,415128775]))
