import collections
import functools
from typing import List


class Trie:
    def __init__(self) -> None:
        self.isEnd=False
        self.children=[None for _ in range(26)]

    def insert(self,word):
        node=self
        for each in word:
            idx=ord(each)-ord("a")
            if node.children[idx] is None:
                node.children[idx]=Trie()
            node=node.children[idx]
        node.isEnd=True
    
    def search(self,word):
        node=self
        for each in word:
            idx=ord(each)-ord("a")
            if(node.children[idx]==None):
                return False
            node=node.children[idx]
        return True
    
    def startsWith(self,prefix):
        node=self
        for each in prefix:
            idx=ord(each)-ord("a")
            if(node.isEnd==False):
                return False
            node=node.children[idx]
        return True
                
    def canInsert(self,word):
        node=self
        for each in word:
            if(not node):
                return False
            idx=ord(each)-ord("a")
            node=node.children[idx]
        self.insert(word)
        return True

class Solution:
    #720
    def longestWord(self, words: List[str]) -> str:
        trie=Trie()
        words.sort(key=lambda item:len(item))
        ans=""
        for each in words:
            if(trie.canInsert(each)):
                if len(each)>len(ans):
                    ans=each
                else:
                    ans=max(ans,each)
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(solution.longestWord(words))
