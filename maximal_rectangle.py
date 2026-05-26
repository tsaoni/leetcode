from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N, M = len(matrix), len(matrix[0])
        h = [0] * M
        ret = 0 
        for row in matrix: 
            ms = []
            for i in range(M): 
                h[i] = h[i] + 1 if row[i] == "1" else 0 
                while len(ms) > 0 and h[ms[-1]] > h[i]: 
                    idx = ms.pop(-1)
                    l = 0 if len(ms) == 0 else ms[-1] + 1
                    r = i - 1
                    w = r - l + 1 
                    ret = max(ret, h[idx] * w)  

                ms.append(i)
            
            while len(ms) > 0: 
                idx = ms.pop(-1)
                l = 0 if len(ms) == 0 else ms[-1] + 1
                r = M - 1
                w = r - l + 1 
                ret = max(ret, h[idx] * w)  
            # print(h)
                
        return ret 
    
if __name__ == "__main__": 
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    matrix = [["0"]]
    matrix = [["1"]]
    ret = Solution().maximalRectangle(matrix)
    print(ret)