import collections
import functools
from typing import List
from heapq import *

class Solution(object):
    # 3387 dijkstra but multi to calculate cost and need to calculate both highCost and lowCost
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        # in dijkstra, we check neighbors, so need to store graph as {node: [(neighbor1, cost1), (neighbor2, cost2) ...]}
        graph1,graph2=collections.defaultdict(list),collections.defaultdict(list)
        for i,[currency1, currency2] in enumerate(pairs1):
            graph1[currency1].append([currency2,rates1[i]])
            graph1[currency2].append([currency1,1/rates1[i]])
        for i,[currency1, currency2] in enumerate(pairs2):
            graph2[currency1].append([currency2,rates2[i]])
            graph2[currency2].append([currency1,1/rates2[i]])
        
        # use dict then it's fine to use currency name rather than index
        highCost = {initialCurrency:1}
        # be careful when calculate highCost, initiate it as -1 rather than 1
        heap=[(-1,initialCurrency)]
        visited={}
        while heap:
            [curMoney, curCurrency] = heappop(heap)
            if curCurrency in visited:
                continue
            curMoney=-curMoney
            for [nextCurrency,rate] in graph1[curCurrency]:
                if curMoney*rate > highCost.get(nextCurrency,0):
                    highCost[nextCurrency] = curMoney*rate
                    heappush(heap, [-highCost[nextCurrency], nextCurrency])
            visited[curCurrency] = True
        
        lowCost = {initialCurrency:1}
        heap=[(1,initialCurrency)]
        visited={}
        while heap:
            [curMoney, curCurrency] = heappop(heap)
            if curCurrency in visited:
                continue
            for [nextCurrency,rate] in graph2[curCurrency]:
                if curMoney*rate < lowCost.get(nextCurrency,float('inf')):
                    lowCost[nextCurrency] = curMoney*rate
                    heappush(heap, [lowCost[nextCurrency], nextCurrency])
            visited[curCurrency] = True
        
        ans=0
        for k,v in highCost.items():
            if k in lowCost:
                ans=max(ans,v/lowCost[k])
        return ans


if __name__ == '__main__':
    n=8
    row=[[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [5, 8], [3, 2], [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3],
     [7, 5]]
    col=[[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]]

    solution=Solution()
    print(solution.buildMatrix(n,row,col))
