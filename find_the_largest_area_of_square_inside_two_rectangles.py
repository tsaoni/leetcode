from typing import List

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        # itvls = []
        N = len(bottomLeft)
        maxSide = 0
        for i in range(N): 
            for j in range(i + 1, N): 
                bi, ti = bottomLeft[i], topRight[i]
                bj, tj = bottomLeft[j], topRight[j]
                if bi[1] < bj[1]: 
                    _bi, _ti = bj, tj 
                else: 
                    bi, ti, _bi, _ti = bj, tj, bi, ti 

                if _bi[0] < ti[0] and _ti[0] > bi[0] and _bi[1] < ti[1]: 
                    xs, xe = sorted([bi[0], ti[0], _bi[0], _ti[0]])[1: 3]
                    ys, ye = sorted([bi[1], ti[1], _bi[1], _ti[1]])[1: 3]
                    w = xe - xs 
                    h = ye - ys 
                    maxSide = max(maxSide, min(w, h))
        

        return maxSide * maxSide
    
if __name__ == "__main__": 
    Solution().largestSquareArea