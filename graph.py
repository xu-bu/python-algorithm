import collections
import functools
from typing import List
from heapq import *
from math import *

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

    # 3552 BFS
    # 仅能向右向左移动的题目才能用dfs，这种上下左右都可以走的题目要用bfs
    # BFS的思想是，模拟移动的过程中维护到每个点的最短距离表，有时可以用visited判断是否入队，本题使用距离判断
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == '#':
            return -1
        rows,cols= len(matrix), len(matrix[0])
        # record portal
        portal = collections.defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j].isupper():
                    portal[matrix[i][j]].append((i,j))
        # BFS
        distanceGrid = [[inf]*cols for _ in range(rows)]
        distanceGrid[0][0] = 0
        queue = collections.deque([(0,0)])
        DIR=[(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            i,j= queue.popleft()
            curDistance=distanceGrid[i][j]
            if i== rows-1 and j == cols-1:
                return curDistance
            c=matrix[i][j]
            if c in portal:
                for x,y in portal[c]:
                    distanceGrid[x][y] = min(distanceGrid[x][y], curDistance)
                    # must use portal first then normal move
                    # since we don't need to move when transport and first cell could be portal 
                    queue.appendleft((x,y))
                del portal[c]
            for [dx,dy] in DIR:
                x,y = i+dx, j+dy
                if 0<=x<rows and 0<=y<cols and matrix[x][y] != '#' and distanceGrid[x][y] > curDistance+1:
                    distanceGrid[x][y] = curDistance+1
                    queue.append((x,y))
        return -1

if __name__ == '__main__':
    n=8
    row=[[1, 2], [7, 3], [4, 3], [5, 8], [7, 8], [8, 2], [5, 8], [3, 2], [1, 3], [7, 6], [4, 3], [7, 4], [4, 8], [7, 3],
     [7, 5]]
    col=[[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]]

    solution=Solution()
    print(solution.buildMatrix(n,row,col))
