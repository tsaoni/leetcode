from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0: 
            digits.append(n % 10) 
            n //= 10 
        digits.sort()
        return digits[-1] * digits[-2]

    def specialGrid(self, N: int) -> List[List[int]]:
        import numpy as np
        from copy import deepcopy
        grid = [[0]]
        def add(grid, d): 
            return (np.array(grid) + d).tolist()
        
        def rconnect(g1, g2): 
            return g1 + g2 
        def cconnect(g1, g2): 
            ng = []
            for c1, c2 in zip(g1, g2): 
                ng.append(c1 + c2)
            return ng
        for i in range(N): 
            d = 4 ** i

            gridbr = add(deepcopy(grid), d)
            gridbl = add(deepcopy(grid), 2 * d)
            gridtl = add(deepcopy(grid), 3 * d)
            # import pdb 
            # pdb.set_trace()
            gr = rconnect(grid, gridbr)
            gl = rconnect(gridtl, gridbl)
            grid = cconnect(gl, gr)
                
        return grid


    def minTravelTime1(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        """
        should use DP and recursive
        time complexity: O((n * k) ** 2)
        """
        from itertools import accumulate
        acc_time = list(accumulate(time))
        # print(acc_time)

        dp = [[[float("inf")] * n for _ in range(n)] for _ in range(k + 1)]
        for ck in range(k + 1): 
            for ci in range(1, n): 
                for j in range(min(ck + 1, ci)):
                    if True: #ci - j >= 0:
                        tmp = float("inf")
                        d = position[ci] - position[ci - j - 1]
                        if ci - j - 1 == 0: 
                            if ck == j:
                                t = time[0]
                                tmp = t * d
                                # print(tmp, ck, j)
                        else:
                            for w in range(max(ci - ck - 1, 1), ci - j):#ci - j): 
                                t = acc_time[ci - j - 1] - acc_time[w - 1]
                                tmp = min(tmp, dp[ck - j][ci - j - 1][w] + t * d)
                                # if tmp == 15: 

                                # import pdb 
                                # pdb.set_trace()
                        
                        dp[ck][ci][ci - j] = tmp
        
        # print(dp[k][n - 1])
        # print(dp)
        
        return min(dp[k][n - 1])

    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        """
        a wrong approach
        """
        def dist(i):
            if i == 0 or i == n - 1: 
                return None
            t = (position[i + 1] - position[i]) * (time[i - 1] - time[i])
            if i + 2 < n: 
                t += (position[i + 2] - position[i + 1]) * time[i]
            return t
        
        d = []
        for i in range(n): 
            t = dist(i)
            d.append(t)
    
        for _ in range(k): 
            idx = d.index(min(d[1: -1])) 

            # print(d, d[1: -1], idx)
            n -= 1
            position.pop(idx)
            time[idx + 1] += time[idx]
            time.pop(idx)
            d.pop(idx)
            d[idx - 1] = dist(idx - 1)
            d[idx] = dist(idx)
        
        # print(position)
        # print(time)
        return sum([time[i] * (position[i + 1] - position[i]) for i in range(n - 1)])

if __name__ == "__main__": 
    # ret = Solution().specialGrid(2)
    # for r in ret:
    #     print(r)
    l = 10
    n = 4
    k = 1
    position = [0,3,8,10]
    time = [5,8,3,6]

    l = 5
    n = 5
    k = 1
    position = [0,1,2,3,5]
    time = [8,3,9,3,3]

    l = 4
    n = 3
    k = 1
    position = [0,3,4]
    time = [1,2,2]

    l = 5
    n = 5
    k = 2
    position = [0,2,3,4,5]
    time = [1,1,3,2,1]
    # print(Solution().minTravelTime(l, n, 1, position, time))
    ret = Solution().minTravelTime1(l, n, k, position, time)
    print(ret)