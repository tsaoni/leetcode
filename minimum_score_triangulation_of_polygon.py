from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        N = len(values)
        dp = [[0] * N for _ in range(N)]
        def triangulation(src, dest): 
            if dest - src < 2: 
                return 0 
            elif dest - src == 2: 
                dp[src][dest] = values[src] * values[src + 1] * values[dest]
                return dp[src][dest]
            else:
                if dp[src][dest] > 0: 
                    return dp[src][dest]
        
                tmp = float("inf")
                for k in range(src + 1, dest): 
                    v = triangulation(src, k) + triangulation(k, dest)
                    v += values[src] * values[k] * values[dest]
                    tmp = min(tmp, v)
                dp[src][dest] = tmp
                # print(dp)
                return dp[src][dest]
        triangulation(0, N - 1)
        return dp[0][N - 1]
    
if __name__ == "__main__": 
    values = [1,2,3]
    values = [3,7,4,5]
    values = [1,3,1,4,1,5]
    ret = Solution().minScoreTriangulation(values)
    print(ret)