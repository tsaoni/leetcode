from typing import List

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        T = [[] for _ in range(n)]
        for v1, v2 in edges: 
            T[v1].append(v2)
            T[v2].append(v1)
        visited = [False] * n
        def dfs(v): 
            visited[v] = True
            cur = values[v]
            ccnt = 1
            for v2 in T[v]: 
                if not visited[v2]: 
                    val, cnt = dfs(v2)
                    if val % k > 0: 
                        cur = (cur + val) % k
                        ccnt += (cnt - 1) 
                    else: 
                        ccnt += cnt 

            return cur, ccnt
        
        ret = 0
        for i in range(n): 
            if not visited[i]: 
                _, cnt = dfs(i)
                ret += cnt
        return ret
    
if __name__ == "__main__": 
    n = 5
    edges = [[0,2],[1,2],[1,3],[2,4]]
    values = [1,8,1,4,4]
    k = 6
    n = 7
    edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
    values = [3,0,6,1,5,2,1]
    k = 3
    ret = Solution().maxKDivisibleComponents(n, edges, values, k)
    print(ret)