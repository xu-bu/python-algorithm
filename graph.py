import collections
import functools
from typing import List
from heapq import *

class Solution(object):
    #200图中搜索岛屿数量
    def numIslands(self, grid: list[list[str]]) -> int:
        #dfs整体结构：
        #dfs先写出口，对四个不同方向for循环，满足条件就开始搜索
        #主函数两轮循环遍历，满足条件则开始搜索，搜完岛屿数量加一
        rows, columns = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            #递归出口，如果不是1，说明要么是0，没有岛屿，要么是.，已经被搜索过了
            if grid[i][j] != '1':
                return
            grid[i][j] = '.'
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                #不要用range去判断，很慢
                if 0 <= x < rows and 0 <= y < columns:
                    dfs(x, y)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    #一轮搜索可以搜完一整个孤岛，再开启下一次搜索的时候已经是下一个岛了
                    dfs(i, j)
                    ans += 1
        return ans

    #210 bfs拓扑排序
    def findOrder(self, numCourses, prerequisites):
        degrees=[0 for _ in range(numCourses)]
        dic=collections.defaultdict(list)
        for pre,course in prerequisites:
            degrees[course-1]+=1
            dic[pre-1].append(course-1)
        queue=collections.deque(key for key,val in enumerate(degrees) if val==0)
        order=[]
        while queue:
            cur=queue.popleft()
            order.append(cur)
            for each in dic[cur]:
                degrees[each]-=1
                if(degrees[each]==0):
                    queue.append(each)
        return order if len(order)==numCourses else []

    #2267
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        columns, rows = len(grid[0]), len(grid)
        if (columns + rows - 1) % 2 != 0 or grid[0][0] == ')' or grid[rows - 1][columns - 1] == '(':
            return False

        # condition记录平衡度，遇到左括号+1，遇到右括号-1，必须一直保持>=0
        # dfs函数表示从x,y位置开始，能否完成找到一条成功的路径
        @functools.cache
        def dfs(x, y, condition):
            # 路径长度是rows+columns-1,所以剩下的括号数量为rows+columns-1-x-y，c不能超过这个值
            if condition < 0 or condition > rows + columns - 1 - x - y:
                return False
            condition += 1 if grid[x][y] == '(' else -1
            if x == rows - 1 and y == columns - 1 and condition == 0:
                return True
            # 往左走完成，或者往右走完成
            return (x + 1 < rows and dfs(x + 1, y, condition)) or (y + 1 < columns and dfs(x, y + 1, condition))

        return dfs(0, 0, 0)
    
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
