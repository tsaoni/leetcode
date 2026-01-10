from typing import List

class Solution:

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        N = len(cells)
        l, r = 0, N - 1 
        ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def cross(d): 
            dp = [[0] * col for _ in range(row)] 
            for i in range(d): 
                r, c = cells[i] 
                dp[r - 1][c - 1] = 1
            cur = set()
            # for i in range(d + 1): 
            while True: 
                if len(cur) == 0: 
                    for i in range(col): 
                        if dp[0][i] == 0:
                            cur.add((0, i))
                            dp[0][i] = 1
                else: 
                    _cur = set()
                    for r, c in cur: 
                        for dr, dc in ds: 
                            _r, _c = r + dr, c + dc 
                            if _r >= 0 and _r < row and _c >= 0 and _c < col: 
                                if dp[_r][_c] == 0: 
                                    _cur.add((_r, _c))
                                    dp[_r][_c] = 1
                                    if _r == row - 1: 
                                        return True
                    cur = _cur
                if len(cur) == 0: 
                    break 
            return False
        # import pdb 
        # pdb.set_trace()
        while l < r: 
            mid = (l + r + 1) // 2 
            if cross(mid): 
                l = mid 
            else: 
                r = mid - 1
        return l 

    def latestDayToCross_error2(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        wrong approach... 
        """
        N = len(cells)
        dp = [[N - 1] * col for _ in range(row)] 
        rec = {}
        for i in range(N): 
            r, c = cells[i]
            rec[(r - 1, c - 1)] = i 
            # dp[r - 1][c - 1] = i 

        d = N - 1
        cur = set()
        ds = [(-1, 1), (0, 1), (1, 1)]
        while True: 
            if len(cur) == 0: 
                for i in range(row): 
                    if (i, 0) in rec: 
                        cur.add((i, 0))
                        dp[i][0] = rec[(i, 0)]
            else: 
                _cur = set()
                for r, c in cur: 
                    x = dp[r][c]
                    for dr, dc in ds: 
                        _r, _c = r + dr, c + dc
                        if _r >= 0 and _r < row and _c < col: 
                            if (_r, _c) in rec: 
                                _d = max(x, rec[(_r, _c)])
                                dp[_r][_c] = min(dp[_r][_c], _d)
                                _cur.add((_r, _c))
                                if _c == col - 1: 
                                    d = min(d, dp[_r][_c])
                
                cur = _cur 
            # print(dp)
            if len(cur) == 0: 
                break 
        print(dp)
        print([dp[i][-1] for i in range(col)])
        return d 
    

    def latestDayToCross_error(self, row: int, col: int, cells: List[List[int]]) -> int:
        """
        wrong intent... 
        """
        mp = [[0] * col for _ in range(row)]
        cur = set()
        d = 0 
        arr = False
        ds = [(0, 1), (0, -1), (1, 0)]
        while not arr: 
            if d < len(cells): 
                r, c = cells[d]
                mp[r - 1][c - 1] = 1 
            if len(cur) == 0: 
                for i in range(col): 
                    if mp[0][i] == 0: 
                        cur.add((0, i))
            else:
                _cur = set()
                for r, c in cur: 
                    for dr, dc in ds: 
                        if r + dr < row and c + dc >= 0 and c + dc < col: 
                            if mp[r + dr][c + dc] == 0: 
                                mp[r + dr][c + dc] = 1 
                                _cur.add((r + dr, c + dc))
                                if r + dr == row - 1: 
                                    arr = True 
                cur = _cur 
            d += 1 

        return d 
    
if __name__ == "__main__": 
    row = 2
    col = 2
    cells = [[1,1],[2,1],[1,2],[2,2]]

    # row = 2
    # col = 2
    # cells = [[1,1],[1,2],[2,1],[2,2]]

    row = 3
    col = 3
    cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]

    row = 13 
    col = 9
    cells = [[12,6],[3,4],[2,9],[9,4],[9,2],[6,4],[4,4],[8,6],[4,9],[5,6],[7,5],[12,4],[11,8],[3,7],[2,6],[9,8],[3,5],[13,4],[1,3],[10,2],[8,9],[6,6],[11,7],[11,1],[13,9],[12,7],[10,7],[8,2],[1,8],[7,3],[6,5],[2,1],[10,6],[4,8],[4,2],[9,7],[6,2],[3,6],[12,2],[10,3],[10,5],[9,5],[8,8],[8,7],[3,2],[13,6],[3,1],[5,1],[2,7],[8,3],[12,5],[11,2],[6,3],[1,4],[13,3],[4,1],[9,9],[7,7],[4,3],[12,1],[2,2],[7,6],[4,6],[7,9],[7,2],[3,8],[1,6],[11,3],[11,4],[5,9],[13,8],[1,9],[10,1],[9,1],[6,1],[10,9],[12,9],[11,5],[8,1],[13,5],[9,6],[13,2],[6,8],[2,8],[5,3],[3,3],[13,1],[11,9],[9,3],[2,4],[5,2],[8,5],[13,7],[12,8],[5,5],[7,1],[7,4],[2,5],[6,9],[4,7],[5,8],[1,5],[10,8],[8,4],[1,1],[3,9],[1,2],[7,8],[1,7],[6,7],[11,6],[4,5],[5,7],[2,3],[10,4],[5,4],[12,3]]
    
    # row = 6 
    # col = 2
    # cells = [[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]] 
    ret = Solution().latestDayToCross(row, col, cells)
    print(ret)