from typing import List

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def area(ub, db, lb, rb): 
            u, d, l, r = m - 1, 0, n - 1, 0 
            for i in range(ub, db): 
                for j in range(lb, rb): 
                    if grid[i][j] == 1: 
                        u, d = min(u, i), max(d, i)
                        l, r = min(l, j), max(r, j)
            if d >= u and r >= l: 
                area = (d - u + 1) * (r - l + 1)
            else: 
                area = 0
            return area
        
        def two_rect_min_area(ub, db, lb, rb): 
            min_area = 900
            for i in range(ub, db - 1): 
                tmp = area(ub, i + 1, lb, rb) + area(i + 1, db, lb, rb)
                min_area = min(min_area, tmp)
            for i in range(lb, rb - 1): 
                tmp = area(ub, db, lb, i + 1) + area(ub, db, i + 1, rb)
                min_area = min(min_area, tmp)
            return min_area
        
        min_area = 900
        for i in range(m - 1): 
            tmp1 = two_rect_min_area(0, i + 1, 0, n) + area(i + 1, m, 0, n)
            tmp2 = area(0, i + 1, 0, n) + two_rect_min_area(i + 1, m, 0, n)
            # print(i, two_rect_min_area(0, i + 1, 0, n), area(i + 1, m, 0, n))
            min_area = min(min_area, tmp1, tmp2)
        # print(min_area)
        for i in range(n - 1): 
            tmp1 = two_rect_min_area(0, m, 0, i + 1) + area(0, m, i + 1, n)
            tmp2 = area(0, m, 0, i + 1) + two_rect_min_area(0, m, i + 1, n)
            min_area = min(min_area, tmp1, tmp2)
        return min_area
    
if __name__ == "__main__": 
    grid = [[1,0,1],[1,1,1]]
    grid = [[1,0,1,0],[0,1,0,1]]
    grid = [[0,0,0],[0,0,1],[0,0,0],[1,0,1]]
    ret = Solution().minimumSum(grid)
    print(ret)