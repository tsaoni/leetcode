from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        ret = 0
        N = len(colors)
        G = [set() for _ in range(N)]
        rG = [set() for _ in range(N)]
        for u, v in edges: 
            G[u].add(v)
            rG[v].add(u)
        roots = []
        dp = [[0] * 26 for _ in range(N)]
        for i in range(N): 
            if len(rG[i]) == 0: 
                roots.append(i)
                idx = ord(colors[i]) - ord("a")
                dp[i][idx] += 1
                ret = max(ret, dp[i][idx])
        
        while len(roots) > 0: 
            nroots = []
            for u in roots: 
                for v in G[u]: 
                    rG[v] -= {u}
                    idx = ord(colors[v]) - ord("a")
                    for i in range(26):
                        if i == idx: 
                            dp[v][i] = max(dp[u][i] + 1, dp[v][i])
                        else:
                            dp[v][i] = max(dp[u][i], dp[v][i])
                        ret = max(ret, dp[v][i])
                    if len(rG[v]) == 0: 
                        nroots.append(v)
                
            roots = nroots
        for i in range(N): 
            if len(rG[i]) > 0: 
                return -1
        return ret
    
if __name__ == "__main__": 
    colors = "abaca"
    edges = [[0,1],[0,2],[2,3],[3,4]]
    colors = "a"
    edges = [[0,0]]
    ret = Solution().largestPathValue(colors, edges)
    print(ret)