import collections
import heapq
import math
from typing import List
import string

class Trie:

    def __init__(self):
        self.children = [None] * 10
        self.isEnd=False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            idx = ord(c) - ord('0')
            if cur.children[idx] is None:
                cur.children[idx] = Trie()
            cur = cur.children[idx]
        cur.isEnd=True

    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            idx = ord(c) - ord('0')
            if cur.children[idx] is None:
                return False
            else:
                cur = cur.children[idx]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            idx = ord(c) - ord('0')
            if cur.children[idx] is None:
                return False
            else:
                cur = cur.children[idx]
        return True

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # at most 31 bits
        BITS=31
        def getNum(num):
            num=str(bin(num))[2:]
            num="0"*(BITS-len(num))+num
            return num
        
        trie=Trie()
        for num in nums:
            trie.insert(getNum(num))

        ans=0
        for num in nums:
            num=getNum(num)
            p=trie
            maxBin=0
            for i in range(BITS):   
                maxBin<<=1
                if(p.children[int(num[i])^1]):
                    maxBin+=1
                    p=p.children[int(num[i])^1]
                else:
                    p=p.children[int(num[i])]
                
            ans=max(ans,maxBin)
        return ans

if __name__ == '__main__':
    solution = Solution()
    print(
        solution.findMaximumXOR([2147483647,2147483646,2147483645])
    )
