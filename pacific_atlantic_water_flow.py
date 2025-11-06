from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from itertools import chain
        m, n = len(heights), len(heights[0])
        dp = [[0] * n for _ in range(m)]
        h_values = sorted(set(chain(*heights)))
        pb, ab = set(), set() # 1, 2 
        def bfs(lst, h, label): 
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)] 
            while True: 
                add = set()
                d = set()
                for i, j in lst: 
                    is_del = label
                    for di, dj in dirs: 
                        if i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n: 
                            if dp[i + di][j + dj] & label == 0 and heights[i + di][j + dj] == h: 
                                add.add((i + di, j + dj))
                                dp[i + di][j + dj] |= label 
                            is_del &= (dp[i + di][j + dj] & label)
                    if is_del: 
                        d.add((i, j))     
                lst -= d
                if len(add) == 0: 
                    break 
                lst |= add
            
        for h in h_values: 
            for i in range(m): 
                if heights[i][0] == h: 
                    pb.add((i, 0))
                    dp[i][0] |= 1
                if heights[i][n - 1] == h: 
                    ab.add((i, n - 1))
                    dp[i][n - 1] |= 2
            for i in range(n): 
                if heights[0][i] == h: 
                    pb.add((0, i))
                    dp[0][i] |= 1
                if heights[m - 1][i] == h: 
                    ab.add((m - 1, i))
                    dp[m - 1][i] |= 2
            
            bfs(pb, h, 1)
            bfs(ab, h, 2)
        ret = []
        for i in range(m): 
            for j in range(n): 
                if dp[i][j] == 3: 
                    ret.append([i, j])
        return ret
    
if __name__ == "__main__": 
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    heights = [[1]]
    ret = Solution().pacificAtlantic(heights)
    print(ret)