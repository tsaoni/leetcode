from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_row, n_col = len(obstacleGrid), len(obstacleGrid[0])
        table = [[0] * n_col for _ in range(n_row)]

        for i in range(n_row): 
            if obstacleGrid[i][0] == 0:
                table[i][0] = 1 
            else: break
        for i in range(n_col): 
            if obstacleGrid[0][i] == 0:
                table[0][i] = 1 
            else: break
        for r in range(1, n_row): 
            for c in range(1, n_col): 
                # u = 0 if obstacleGrid[r - 1][c] else table[r - 1][c]
                # l = 0 if obstacleGrid[r][c - 1] else table[r][c - 1]
                if obstacleGrid[r][c] == 0:
                    table[r][c] = table[r - 1][c] + table[r][c - 1]
        
        return table[n_row - 1][n_col - 1]
    
if __name__ == "__main__": 
    test_case = [[0,1],[0,0]]
    ret = Solution().uniquePathsWithObstacles(test_case)
    print(ret)