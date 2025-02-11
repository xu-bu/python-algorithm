import bisect
import collections
import copy
import functools
from functools import *
import itertools
from heapq import *
import math
import string
from decimal import Decimal
from math import gcd
from typing import List, Union, Optional
from sortedcontainers import *
from pydash import *


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


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        dic={}
        maxVal=max(groups)
        for i in range(len(elements)):
            elm=elements[i]
            if elm in dic:
                continue
            multi=1
            while multi*elm<=maxVal:
                if multi*elm in dic:
                    multi += 1
                    continue
                dic[multi * elm] = i
                multi+=1
        for i in range(len(groups)):
            groups[i]=dic.get(groups[i],-1)
        return groups

if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    coins = [[-7,12,12,13],[-6,19,19,-6],[9,-2,-10,16],[-4,14,-10,-9]]
    print(solution.sortMatrix(grid = [[1,7,3],[9,8,2],[4,5,6]]))
