from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        cur = {(0, 0)}
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = 0#moveTime[0][0]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while len(cur) > 0: 
            ncur = set()
            for i, j in cur:
                for di, dj in d:
                    if i + di >= 0 and i + di < n and j + dj >= 0 and j + dj < m:
                        t = max(dp[i][j] + 1, moveTime[i + di][j + dj] + 1)
                        if dp[i + di][j + dj] > t: 
                            dp[i + di][j + dj] = t
                            ncur.add((i + di, j + dj))
            cur = ncur
        return dp[-1][-1]
    
if __name__ == "__main__": 
    moveTime = [[0,4],[4,4]]
    # moveTime = [[0,0,0],[0,0,0]]
    moveTime = [[56,93],[3,38]]
    ret = Solution().minTimeToReach(moveTime)
    print(ret)