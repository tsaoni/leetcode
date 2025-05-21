from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        set_first_row_zero, set_first_col_zero = 0, 0
        for i in range(m): 
            for j in range(n): 
                if matrix[i][j] == 0: 
                    matrix[i][0] = 0 
                    matrix[0][j] = 0 
                    if i == 0: 
                        set_first_row_zero = 1
                    if j == 0: 
                        set_first_col_zero = 1
        # print(matrix)
        for i in range(1, m): 
            if matrix[i][0] == 0: 
                for j in range(1, n): 
                    matrix[i][j] = 0 
        # print(matrix)
        for j in range(1, n): 
            if matrix[0][j] == 0: 
                for i in range(1, m): 
                    matrix[i][j] = 0 
        if set_first_row_zero == 1: 
            for j in range(n): 
                matrix[0][j] = 0 
        if set_first_col_zero == 1: 
            for i in range(m): 
                matrix[i][0] = 0

if __name__ == "__main__": 
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    print(matrix)