from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ret = 0
        for i in range(1, m + 1): 
            for j in range(1, n + 1): 
                _l = dp[i - 1][j - 1] + 1
                l = 0
                for k in range(_l): 
                    if matrix[i - k - 1][j - 1] == 1 and matrix[i - 1][j - k - 1] == 1: 
                        l += 1 
                    else: 
                        break
                dp[i][j] = l
                ret += l
        # print(dp)
        return ret
    
if __name__ == "__main__": 
    matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
    ret = Solution().countSquares(matrix)
    print(ret)