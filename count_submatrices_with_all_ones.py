from typing import List

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        h = [0] * n
        ret = 0
        for i in range(m): 
            cur = 0
            stack = []
            for j in range(n): 
                h[j] = h[j] + 1 if mat[i][j] == 1 else 0
                end = j 
                while len(stack) > 0 and stack[-1][0] >= h[j]: 
                    _h, start = stack.pop(-1)
                    cur -= (end - start) * _h
                    end = start
                stack.append((h[j], end))
                cur += (j - end + 1) * h[j]
                ret += cur
                # print(stack, cur)
            # print(h)
        return ret
    
if __name__ == "__main__": 
    mat = [[1,0,1],[1,1,0],[1,1,0]]
    mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
    ret = Solution().numSubmat(mat)
    print(ret)