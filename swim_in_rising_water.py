from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1: 
            return grid[0][0]
        pos = [[] for _ in range(n ** 2)] 
        for i in range(n): 
            for j in range(n): 
                h = grid[i][j]
                pos[h].append((i, j))
        
        def find(x): 
            return x if T[x] == -1 else find(T[x])
        
        def merge(p1, p2): 
            T[p2] = p1
            
        T = [-1] * (n ** 2)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for h in range(n ** 2): 
            for i, j in pos[h]: 
                p = -1
                cur = i * n + j
                if T[cur] == -1:
                    for di, dj in dirs: 
                        _i, _j = i + di, j + dj 
                        if _i >= 0 and _i < n and _j >= 0 and _j < n: 
                            if grid[_i][_j] <= h: 
                                _p = find(_i * n + _j)
                                if not p == _p: 
                                    if p > -1: 
                                        merge(p, _p)
                                    else: 
                                        p = _p
                    merge(p, cur)
            if T[0] > -1 or T[-1] > -1: 
                ps, pd = find(0), find(n ** 2 - 1)
                if ps > -1 and ps == pd: 
                    return h
        
    
if __name__ == "__main__": 
    grid = [[0,2],[1,3]]
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    ret = Solution().swimInWater(grid)
    print(ret)