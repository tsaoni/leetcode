from typing import List

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        import copy 
        N, M = len(grid), len(grid[0])
        ret = 1

        rsum, csum, d1sum, d2sum = [copy.deepcopy(grid) for _ in range(4)]
        for l in range(2, min(N, M) + 1): 
            # print(l, min(N, M))
            for i in range(N): 
                for j in range(M - l + 1): 
                    rsum[i][j] += grid[i][j + l - 1]
            for i in range(N - l + 1): 
                for j in range(M): 
                    csum[i][j] += grid[i + l - 1][j]
            for i in range(N - l + 1): 
                for j in range(M - l + 1): 
                    d1sum[i][j] += grid[i + l - 1][j + l - 1]
                    d2sum[i + l - 1][j] += grid[i][j + l - 1]
            # if l == 3: 
            #     print(rsum)
            #     print(csum)
            #     print(d1sum)
            #     print(d2sum)
            
            
            for j in range(M - l + 1): 
                rcnt = 1
                for i in range(N - 1): 
                    if rsum[i + 1][j] == rsum[i][j]: 
                        x = rsum[i][j]
                        rcnt += 1 
                        if rcnt == l: 
                            r = i - l + 2
                            c = j 
                            ccnt = 1
                            for _c in range(c, c + l - 1): 
                                if csum[r][_c + 1] == csum[r][_c]: 
                                    ccnt += 1 
                                else: 
                                    break 
                            # import pdb 
                            # pdb.set_trace()
                            if ccnt == l: 
                                if d1sum[r][c] == x and d2sum[i + 1][j] == x: 
                                    ret = l 
                                
                    else: 
                        rcnt = 1
                    if ret == l: 
                        break 
                if ret == l: 
                    break 
            # import pdb 
            # pdb.set_trace()
        return ret 
    
if __name__ == "__main__": 
    grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
    grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
    grid = [[8,1,6],[3,5,7],[4,9,2],[7,10,9]]
    grid = [[6,9,10,5,6,5,6],[9,8,1,6,2,6,8],[9,3,5,7,6,5,3],[6,4,9,2,7,8,5]]
    ret = Solution().largestMagicSquare(grid)
    print(ret)