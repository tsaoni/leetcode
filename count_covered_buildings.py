from typing import List

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        ilim = [None] * n 
        jlim = [None] * n 
        ret = 0
        def check_inc(bidx, item, idx):
            if item is None or (item is not None and item[idx] != bidx): 
                return True 
            else: 
                return False
        for idx, (i, j) in enumerate(buildings): 
            add = True
            if ilim[i - 1] is None: 
                ilim[i - 1] = (j, j, idx, idx)
                add = False
            elif ilim[i - 1][0] > j: 
                x = ilim[i - 1][2]
                _i, _j = buildings[x]
                # if ilim[i - 1][3] != x and jlim[_j - 1][2] != x and jlim[_j - 1][3] != x: 
                if check_inc(x, ilim[i - 1], 3) and check_inc(x, jlim[_j - 1], 2) and check_inc(x, jlim[_j - 1], 3):
                    ret += 1 
                ilim[i - 1] = (j, ilim[i - 1][1], idx, ilim[i - 1][3])
                add = False
            elif ilim[i - 1][1] < j: 
                x = ilim[i - 1][3]
                _i, _j = buildings[x]
                if check_inc(x, ilim[i - 1], 2) and check_inc(x, jlim[_j - 1], 2) and check_inc(x, jlim[_j - 1], 3):
                    ret += 1 
                ilim[i - 1] = (ilim[i - 1][0], j, ilim[i - 1][2], idx)
                add = False
           
            if jlim[j - 1] is None: 
                jlim[j - 1] = (i, i, idx, idx)
                add = False
            elif jlim[j - 1][0] > i: 
                x = jlim[j - 1][2]
                _i, _j = buildings[x]
                # if ilim[i - 1][3] != x and jlim[_j - 1][2] != x and jlim[_j - 1][3] != x: 
                if check_inc(x, jlim[j - 1], 3) and check_inc(x, ilim[_i - 1], 2) and check_inc(x, ilim[_i - 1], 3):
                    ret += 1 
                jlim[j - 1] = (i, jlim[j - 1][1], idx, jlim[j - 1][3])
                add = False
            elif jlim[j - 1][1] < i: 
                x = jlim[j - 1][3]
                _i, _j = buildings[x]
                if check_inc(x, jlim[j - 1], 2) and check_inc(x, ilim[_i - 1], 2) and check_inc(x, ilim[_i - 1], 3):
                    ret += 1 
                jlim[j - 1] = (jlim[j - 1][0], i, jlim[j - 1][2], idx)
                add = False
            
            if add: 
                ret += 1
            # print(ret, buildings[idx], add)
            # print(ilim)
            # print(jlim)
        return ret 
    
if __name__ == "__main__": 
    n = 3
    buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
    # n = 3
    # buildings = [[1,1],[1,2],[2,1],[2,2]]
    # n = 5
    # buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
    # n = 4 
    # buildings = [[2,4],[1,2],[4,3],[3,1],[1,1],[2,3],[3,2],[1,3]]
    ret = Solution().countCoveredBuildings(n, buildings)
    print(ret)