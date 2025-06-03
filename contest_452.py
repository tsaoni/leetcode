from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(self): 
        return  
    
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        import math
        maxp = 1 
        for n in nums: 
            maxp *= n
        if math.sqrt(maxp) != target: 
            return False
        # products = [1] + [0] * (target - 1) 
        cands = {0}
        for num in nums: 
            ncands = set()
            for i in cands: #range(target - 1, -1, -1): 
                p = i + 1 
                #if p % num == 0: 
                if p * num <= target:
                    # if products[p - 1]: 
                    # products[p * num - 1] = 1
                    ncands.add(p * num - 1)
    
                if p * num == target: 
                    return True
            cands = cands.union(ncands) 
            # d = []
            # for i in range(target): 
            #     if products[i]: 
            #         d.append(i + 1)
            # products[num - 1] = 1
            # print(d)
        return False

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ret = [[-1] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1): 
            for j in range(n - k + 1): 
                arr = set()
                for ik in range(i, i + k): 
                    for jk in range(j, j + k): 
                        arr.add(grid[ik][jk])
                arr = list(arr)
                arr.sort()
                if len(arr) == 1: 
                    ret[i][j] = 0 
                else:
                    tmp = ret[i][j]
                    for idx in range(1, len(arr)): 
                        tmp = min(tmp, arr[idx] - arr[idx - 1]) if tmp >= 0 else arr[idx] - arr[idx - 1]
                    ret[i][j] = tmp 

        return ret

    def minMoves(self, classroom: List[str], energy: int) -> int:
        
        return 0

if __name__ == "__main__": 
    nums = [3,1,6,8,4]
    target = 24
    # nums = [2,5,3,7]
    # target = 15
    # nums = [20,14,18,15,7,12]
    # target = 2520
    # ret = Solution().checkEqualPartitions(nums, target)
    # print(ret)

    grid = [[1,8],[3,-2]]
    k = 2
    # grid = [[3,-1]]
    # k = 1
    grid = [[1,-2,3],[2,3,5]]
    k = 2
    ret = Solution().minAbsDiff(grid, k)
    print(ret)