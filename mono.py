
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

#239 维护能输出最大值的队列
#这里实现的单调队列并不是把窗口中单调递减的值拿出来组成一个新队列，而是保证新入队的元素一直是单调队列中最小的值。同时这个队列没有维护窗口中的所有元素，因为没有必要
#1.pop(value)：如果窗口移除的元素value等于单调队列的出口元素，那么队列弹出元素，否则不用任何操作
#2.push(value)：如果push的元素value大于入口元素的数值，那么就将队列后端的元素弹出，直到push元素的数值小于等于队列入口元素的数值为止
class myQueue:
    def __init__(self):
        self.queue=collections.deque()

    def pop(self,val):
        if self.queue and val==self.queue[0]:
            self.queue.popleft()

    def push(self,val):
        while self.queue and val>self.queue[-1]:
            self.queue.pop()
        self.queue.append(val)



    def getMax(self):
        return self.queue[0]

class Solution:
    #496 单调栈，O（n)复杂度解决寻找数组中每个数的下一个比它 大/小 的 数/其下标
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mono = []
        dic = {}
        #单调栈构造方式（存数的情况）
        for each in nums2:
            while len(mono)>0 and mono[-1]<each:
                dic[mono.pop()]=each
            mono.append(each)

        ans = []
        for each in nums1:
            ans.append(dic.get(each, -1))
        return ans



    #739 栈存下标的情况
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        #栈存下标，元素单调递减
        mono = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(mono)>0 and temperatures[i]>temperatures[mono[-1]]:
                index=mono.pop()
                ans[index]=i-index
            mono.append(i)
        return ans

    #239
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        if k==1:
            return nums

        monoQ=myQueue()
        for i in range(k):
            monoQ.push(nums[i])

        ans=[monoQ.getMax()]
        for i in range(k,len(nums)):
            willPop,willPush=nums[i-k],nums[i]
            monoQ.pop(willPop)
            monoQ.push(willPush)
            ans.append(monoQ.getMax())
        return ans

    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # ans for nums[:i]
        # dp[i+1]=sum(dp[start:i+1])
        dp = [0] * (n+1)
        # dp[0] should be 1 then we are able to calculate dp[1]=1
        dp[0]=1
        # sum of dp[start:i+1]
        preSum=1
        maxDeque = deque()
        minDeque = deque()
        start = 0
        MOD= (10**9 + 7)
        # i starts from 0 since we're calculating dp[i+1]
        for i in range(n):
            # keep the max and min at the start of the mono deque
            while maxDeque and nums[i] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[i])
            while minDeque and nums[i] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[i])
            while maxDeque and minDeque and maxDeque[0] - minDeque[0] > k:
                if nums[start] == maxDeque[0]:
                    maxDeque.popleft()
                if nums[start] == minDeque[0]:
                    minDeque.popleft()
                preSum-= dp[start]
                start += 1
            dp[i+1] = (preSum) %MOD
            preSum += dp[i+1]
            preSum%= MOD
        return dp[-1]

if __name__ == '__main__':
    solution=Solution()
    s = "abcabcabcabc"
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(solution.maxSlidingWindow(nums,k))