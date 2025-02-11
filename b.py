import bisect
import collections
import copy
import functools
from functools import *
import heapq
import itertools
from heapq import *
import math
import string
from decimal import Decimal
from math import gcd
from typing import List, Union, Optional
from sortedcontainers import SortedList


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
    def __init__(self):
        self.children = [None] * 26

    def insert(self,word: str):
        for each in word:
            if self.children[ord(each) - ord('a')] == None:
                self.children[ord(each) - ord('a')] = Trie()
            self=self.children[ord(each) - ord('a')]

    def startsWith(self,prefix):
        lens=[]
        i=1
        # 在查询的过程中可以记录能查到哪一步
        # 比如如果前缀是abcd，查到ab可行，但是从c开始不行了,则c以后的肯定也不行
        # 就返回一个[1,2]的数组表示当前prefix中可行的长度
        for each in prefix:
            if self.children[ord(each) - ord('a')] == None:
                break
            self=self.children[ord(each) - ord('a')]
            lens.append(i)
            i+=1
        return lens
    
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count1,count2=collections.Counter(word1),collections.Counter(word2)
        for each in count2:
            if count1.get(each,0)<count2[each]:
                return 0
        checkList=[0]*26
        def isValid():
            for each in checkList:
                if each<0:
                    return False
            return True
        
        n=len(word1)
        for each in word2:
            checkList[ord(each)-ord('a')]-=1
        defaultList=copy.deepcopy(checkList)
        start,end=0,0
        ans=0
        while start<n:
            checkList[ord(word1[end])-ord('a')]+=1
            end+=1
            while isValid():
                ans+=n-end+1
                checkList[ord(word1[start])-ord('a')]-=1
                start+=1
            if end==n:
                start+=1
                end=start
                checkList=copy.deepcopy(defaultList)
        return ans
    
if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, 0, 0, 2]
    k = 4
    grid = [[9, 5, 7, 3], [8, 9, 6, 1], [6, 7, 14, 3], [2, 5, 3, 1]]
    print(solution.validSubstringCount(word1 = "abcabc", word2 = "aaabc"))
