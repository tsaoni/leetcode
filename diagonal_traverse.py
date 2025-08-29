from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ret = []
        for id_sum in range(m + n - 1): 
            if id_sum & 1 == 0: 
                i = min(id_sum, m - 1)
                j = id_sum - i 
                while i >= 0 and j < n: 
                    ret.append(mat[i][j])
                    i -= 1 
                    j += 1 
            else: 
                j = min(id_sum, n - 1)
                i = id_sum - j 
                while j >= 0 and i < m: 
                    ret.append(mat[i][j])
                    j -= 1 
                    i += 1
        return ret
    
if __name__ == "__main__": 
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    ret = Solution().findDiagonalOrder(mat)
    print(ret)