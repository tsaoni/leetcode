from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mp = [[0] * n for _ in range(m)]
        for i, j in guards: 
            mp[i][j] = 2 
        for i, j in walls: 
            mp[i][j] = 3 
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n_guarded = 0
        for i, j in guards: 
            for di, dj in d:
                stp = 1
                while True:
                    _i, _j = i + stp * di, j + stp * dj
                    if _i >= 0 and _i < m and _j >= 0 and _j < n: 
                        if mp[_i][_j] & 2 > 0: 
                            break 
                        else: 
                            if mp[_i][_j] == 0: 
                                mp[_i][_j] = 1 
                                n_guarded += 1 
                            # else: 
                            #     break 
                    else: 
                        break 
                    stp += 1

        # print(n_guarded)
        ret = m * n - len(guards) - len(walls) - n_guarded
        return ret
    
if __name__ == "__main__": 
    m = 4
    n = 6
    guards = [[0,0],[1,1],[2,3]]
    walls = [[0,1],[2,2],[1,4]]
    m = 3
    n = 3
    guards = [[1,1]]
    walls = [[0,1],[1,0],[2,1],[1,2]]
    ret = Solution().countUnguarded(m, n, guards, walls)
    print(ret)