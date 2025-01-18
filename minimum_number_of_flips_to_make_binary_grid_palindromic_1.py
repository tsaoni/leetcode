from typing import List

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n_row_flip, n_col_flip = 0, 0
        for row in grid: 
            mid = int(len(row) / 2)
            for i in range(mid): 
                n_row_flip += row[i] ^ row[len(row) - 1 - i]
        for j in range(len(grid[0])): 
            col = [row[j] for row in grid]
            mid = int(len(col) / 2)
            for i in range(mid): 
                n_col_flip += col[i] ^ col[len(col) - 1 - i]
        
        return min(n_row_flip, n_col_flip)
    
if __name__ == "__main__": 
    test_case = [[1],[0]]
    ret = Solution().minFlips(test_case)
    print(ret)