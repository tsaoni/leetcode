from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        N, M = len(mat), len(mat[0])
        MAXL = max(N, M)
        ps = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N): 
            for j in range(M): 
                ps[i + 1][j + 1] = ps[i + 1][j] + ps[i][j + 1] + mat[i][j] - ps[i][j]
    
        # print(ps)
        def is_satisfy(l): 
            for i in range(l, N + 1): 
                for j in range(l, M + 1): 
                    a = ps[i][j] - ps[i - l][j] - ps[i][j - l] + ps[i - l][j - l]
                    if a <= threshold: 
                        return True 
            return False
        l, r = 0, MAXL 
        while l < r: 
            mid = (l + r + 1) // 2 
            if is_satisfy(mid): 
                l = mid 
            else: 
                r = mid - 1

        return l
    
if __name__ == "__main__": 
    mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
    threshold = 4
    mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
    threshold = 2
    ret = Solution().maxSideLength(mat, threshold)
    print(ret)