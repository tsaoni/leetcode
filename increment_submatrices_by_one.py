from typing import List

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        ps = [[0] * (n + 2) for _ in range(n)]
        for ti, tj, bi, bj in queries: 
            for i in range(ti, bi + 1): 
                ps[i][(bj + 1) + 1] -= 1 
                ps[i][(tj + 1)] += 1 

        ret = [[0] * n for _ in range(n)]
        for i in range(n): 
            for j in range(n): 
                ps[i][j + 1] += ps[i][j]
                ret[i][j] = ps[i][j + 1]
        return ret
    
if __name__ == "__main__": 
    n = 3
    queries = [[1,1,2,2],[0,0,1,1]]
    n = 2
    queries = [[0,0,1,1]]
    ret = Solution().rangeAddQueries(n, queries)
    print(ret)