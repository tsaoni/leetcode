from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        _dp = [[float("inf")] * n for _ in range(m)]
        _dp[0][0] = 0
        # dp = [[float("inf")] * n for _ in range(m)]
        mp = []
        for i in range(m): 
            for j in range(n): 
                mp.append((grid[i][j], i, j))
        mp.sort()
        _mp = {}
        _mp1 = {}
        cur = m * n - 1
        for _i in range(m * n - 1, -1, -1): 
            v, i, j = mp[_i]
            if v < mp[cur][0]: 
                cur = _i
            _mp[i, j] = cur
            # if i + j == 0: 
            #     i0 = _i
            # _mp1[i, j] = _i
            # import pdb 
            # pdb.set_trace()

        # print(_mp)
        def compute(si, sj, _dp, v_updated):
            for i in range(si, m): 
                for j in range(sj, n): 
                    if i > 0: 
                        tmp = _dp[i - 1][j] + grid[i][j] 
                        if tmp < _dp[i][j]: 
                            _dp[i][j] = tmp
                            _i = _mp[i, j]
                            v_updated[_i] = min(tmp, v_updated[_i])
                    if j > 0: 
                        tmp = _dp[i][j - 1] + grid[i][j] 
                        if tmp < _dp[i][j]: 
                            _dp[i][j] = tmp
                            _i = _mp[i, j]
                            v_updated[_i] = min(tmp, v_updated[_i])

        v_updated = [float("inf")] * (m * n) 
        i0 = _mp[0, 0]
        v_updated[i0] = 0
        # print(i0)
        # print(mp)
        compute(0, 0, _dp, v_updated)
        # print(v_updated)
        
        for _ in range(k): 
            # for i in range(m): 
            #     for j in range(n): 
            #         if i > 0: 
            #             tmp = _dp[i - 1][j] + grid[i][j] 
            #             if tmp < dp[i][j]: 
            #                 dp[i][j] = tmp
            #                 _i = _mp[i, j]
            #                 v_updated[_i] = min(v_updated[_i], tmp)
            #         if j > 0: 
            #             tmp = _dp[i][j - 1] + grid[i][j] 
            #             if tmp < dp[i][j]: 
            #                 dp[i][j] = tmp
            #                 _i = _mp[i, j]
            #                 v_updated[_i] = min(v_updated[_i], tmp) 
            v = float("inf")
            for _i in range(m * n - 1, -1, -1): 
                _, i, j = mp[_i]
                _i = _mp[i, j]
                if v_updated[_i] < v:
                    v = v_updated[_i]
                # print(v, _dp)
                
                if v < _dp[i][j]: 
                    _dp[i][j] = v 
            compute(0, 0, _dp, v_updated)
                    
                    # import pdb 
                    # pdb.set_trace()
                # _, i, j = mp[_i]
                # dp[i][j] = min(_dp[i][j], v)
            # tmp = dp 
            # dp = _dp 
            # _dp = dp
            # print(v_updated)
            # import pdb 
            # pdb.set_trace()
        return _dp[-1][-1]
    
if __name__ == "__main__": 
    grid = [[1,3,3],[2,5,4],[4,3,5]]
    k = 2
    # grid = [[1,2],[2,3],[3,4]]
    # k = 1
    grid = [[3,1],[10,4]] 
    k = 7
    grid = [[16,6],[12,13]]
    k = 3
    grid = [[1,1,2],[1,1,1]] 
    k = 2
    ret = Solution().minCost(grid, k)
    print(ret)