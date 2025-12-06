from typing import List

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        modulo = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(k)] for _ in range(n + 1)]
        for i in range(m): 
            if i & 1 == 0:
                src, tgt = 0, 1 
            else: 
                src, tgt = 1, 0
            for j in range(n): 
                num = grid[i][j] % k 
                if i == 0 and j == 0: 
                    dp[j + 1][num][tgt] = 1 
                else:
                    for _k in range(k): 
                        idx = (num + _k) % k
                        if i == 0: 
                            dp[j + 1][idx][tgt] = dp[j][_k][tgt]
                        elif j == 0: 
                            dp[j + 1][idx][tgt] = dp[j + 1][_k][src]
                        else:
                            dp[j + 1][idx][tgt] = dp[j + 1][_k][src] + dp[j][_k][tgt]
                        dp[j + 1][idx][tgt] %= modulo
                    
            # print(dp)
                        
        return dp[-1][0][tgt]
    
if __name__ == "__main__": 
    grid = [[5,2,4],[3,0,5],[0,7,2]]
    k = 3
    # grid = [[0,0]]
    # k = 5
    # grid = [[7,3,4,9],[2,3,6,2],[2,3,7,0]]
    # k = 1
    # grid = [[1,5,3,7,3,2,3,5]] 
    # k = 29
    ret = Solution().numberOfPaths(grid, k)
    print(ret)