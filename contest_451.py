from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(self): 
        return 
    
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        cost = 0
        while n > k: 
            cost += (n - k) * k
            n -= k
        while m > k: 
            cost += (m - k) * k 
            m -= k
        return cost

    def resultingString(self, s: str) -> str:
        ret = ""
        def isAdjacent(a, b): 
            if abs(ord(a) - ord(b)) in [1, 25]: 
                return True 
            else: 
                return False
        for c in s: 
            if len(ret) > 0 and isAdjacent(ret[-1], c): 
                ret = ret[: -1]
            else: 
                ret += c
        return ret

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        """
        wrong implementation
        """
        # max_cost = sum([f - p // 2 for f, p in zip(future, present)])
        dp = [[[0, 0], *[[None, None] for _ in range(budget)]] for _ in range(n)]
        T = [[] for _ in range(n)]
        for b, e in hierarchy: 
            T[b - 1].append(e - 1)
        
        ret = 0
        def None2Zero(x): 
            return x if x is not None else 0
        if present[0] <= budget: 
            dp[0][present[0]][1] = future[0] - present[0]
            ret = dp[0][present[0]][1]
        def dfs(b): 
            maxp = 0
            for e in T[b]: 
                for i in range(1, budget + 1): 
                    if not (dp[b][i][0] is None and dp[b][i][1] is None): 
                        dp[e][i][0] = None2Zero(dp[b][i][0])  + None2Zero(dp[b][i][1])
                    p1, p2 = 0, 0
                    if i - present[e] // 2 > 0:
                        if dp[b][i - present[e] // 2][1] != None:
                            p1 = dp[b][i - present[e] // 2][1] + future[e] - present[e] // 2
                    if i - present[e] >= 0:
                        if dp[b][i - present[e]][0] != None:
                            p2 = dp[b][i - present[e]][0] + future[e] - present[e] 
                    dp[e][i][1] = max(p1, p2)
                    if dp[e][i][0] is None:
                        maxp = max(dp[e][i][1], maxp)
                    else:
                        maxp = max(*dp[e][i], maxp)
                    
                maxp = max(dfs(e), maxp)
                
            return maxp
        # ret = max(dfs(0), ret)

        def bfs(): 
            return 
        print(dp[2])
        return ret

    def maxProfit1(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        """
        use tree DP
        """
        T = [[] for _ in range(n)]
        for b, e in hierarchy: 
            T[b - 1].append(e - 1)
        dp = [[[0, 0] for _ in range(budget + 1)] for _ in range(n)]
        def dfs(boss, prev): 
            for epr in T[boss]: 
                prev = dfs(epr, prev)

                dp[prev]
                prev = epr 

                
            return boss
        
        dfs(0, -1)
        return 0

if __name__ == "__main__": 
    s = "adcb"
    # ret = Solution().resultingString(s)
    # print(ret)

    n = 2
    present = [3,4]
    future = [5,8]
    hierarchy = [[1,2]]
    budget = 4

    n = 2
    present = [1,2]
    future = [4,3]
    hierarchy = [[1,2]]
    budget = 3

    n = 2 
    present = [6,11]
    future = [5,48]
    hierarchy = [[1,2]]
    budget = 142

    n = 3
    present = [6,4,23]
    future = [50,48,17] 
    hierarchy = [[1,3],[1,2]] 
    budget = 28
    ret = Solution().maxProfit(n, present, future, hierarchy, budget)
    print(ret)