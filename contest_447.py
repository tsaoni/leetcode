from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 
    
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(n)]
        hr = [[] for _ in range(n)]
        vr = [[] for _ in range(n)]
        # hbl = set()
        # vbl = set()
        for x, y in buildings: 
            if len(hr[x - 1]) < 2: 
                hr[x - 1].append(y - 1)
                hr[x - 1].sort()
            if len(hr[x - 1]) == 2: 
                # hbl.add(x - 1)
                if hr[x - 1][0] > y - 1: 
                    hr[x - 1][0] = y - 1 
                if hr[x - 1][1] < y - 1: 
                    hr[x - 1][1] = y - 1 
             
            if len(vr[y - 1]) < 2: 
                vr[y - 1].append(x - 1)
                vr[y - 1].sort()
            if len(vr[y - 1]) == 2: 
                # vbl.add(y - 1)
                if vr[y - 1][0] > x - 1: 
                    vr[y - 1][0] = x - 1 
                if vr[y - 1][1] < x - 1: 
                    vr[y - 1][1] = x - 1 

        # for h in hbl: 
        for h in range(n): 
            if len(hr[h]) == 2:
                for idx in range(hr[h][0] + 1, hr[h][1]):
                    grid[h][idx] = 1 
        
        # for v in vbl: 
        for v in range(n): 
            if len(vr[v]) == 2:
                for idx in range(vr[v][0] + 1, vr[v][1]):
                    if grid[idx][v] == 1: 
                        grid[idx][v] = 2 
                

        ret = 0
        for x, y in buildings: 
            ret += (grid[x - 1][y - 1] == 2)

        return ret
    
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        parents = [-1] * n 
        p = 0
        for i in range(1, n): 
            if nums[i] - nums[i - 1] > maxDiff: 
                p = i 
            else:
                parents[i] = p
        
        # for i in range(n):
        #     for j in range(i): 
        #         if abs(nums[i] - nums[j]) <= maxDiff: 
        #             tmp = j
        #             while parents[tmp] != -1: 
        #                 tmp = parents[tmp]
        #             parents[i] = tmp
    

        ret = []
        # print(parents)
        for n1, n2 in queries: 
            if parents[n1] == -1: 
                p1 = n1 
            else: 
                p1 = parents[n1]
            
            if parents[n2] == -1: 
                p2 = n2 
            else: 
                p2 = parents[n2]

            
            ret.append(p1 == p2)
        return ret
    
if __name__ == "__main__": 
    # n = 3
    # buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
    # n = 3
    # buildings = [[1,1],[1,2],[2,1],[2,2]]

    # n = 5
    # buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

    # n = 3
    # buildings = [[2,3],[3,3],[1,3]]

    # test_case = (n, buildings)
    # ret = Solution().countCoveredBuildings(*test_case)
    # print(ret)

    n = 2
    nums = [1,3]
    maxDiff = 1
    queries = [[0,0],[0,1]] 

    # n = 4
    # nums = [2,5,6,8]
    # maxDiff = 2
    # queries = [[0,1],[0,2],[1,3],[2,3]]

    test_case = (n, nums, maxDiff, queries)
    ret = Solution().pathExistenceQueries(*test_case)
    print(ret)