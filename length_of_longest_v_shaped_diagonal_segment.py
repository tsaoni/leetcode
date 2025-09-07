from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[[-1, -1] for _ in range(4)] for _ in range(n)] for _ in range(m)]
        ds = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        def dfs(x, y, cur, dir_id, is_turn): 
            # print(x, y)
            ans = 1
            turn_id = 1 if is_turn else 0
            # if x == 1 and y == 2: 
            #     import pdb 
            #     pdb.set_trace()
            if dp[x][y][dir_id][turn_id] > 0: 
                return 
            # if x == 3 and y == 2: 
            #     import pdb 
            #     pdb.set_trace()
            if grid[x][y] == cur:
                dp[x][y][dir_id][turn_id] = 1
                dx, dy = ds[dir_id]
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                    _cur = 2 if cur in [0, 1] else 0
                    dfs(x + dx, y + dy, _cur, dir_id, is_turn)
                
                # turn in current position
                if cur != 1 and not is_turn: 
                    turns = [(dir_id + 1) % 4] #, (dir_id + 3) % 4]
                    for idx in turns: 
                        dx, dy = ds[idx]
                        if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n:
                            _cur = 2 if cur in [0, 1] else 0
                            dfs(x + dx, y + dy, _cur, idx, True)
                
                dx, dy = ds[dir_id]
                if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and grid[x + dx][y + dy] != 1:
                    # start = 1 if is_turn else 0
                    for turn_id in range(2):
                        if not(x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n):
                            tmp = 0
                        elif dp[x + dx][y + dy][dir_id][turn_id] == -1: 
                            tmp = 1 
                        else: 
                            tmp = dp[x + dx][y + dy][dir_id][turn_id] + 1 
                        dp[x][y][dir_id][turn_id] = max(tmp, dp[x][y][dir_id][turn_id])
                        print(x, y, dp[x][y][dir_id], dir_id, dx, dy)
                    
                # if x == 2 and y == 0: 
                #     import pdb 
                #     pdb.set_trace()
                
                if cur != 1 and not is_turn:
                    # turns = [dir_id]
                    for idx in turns:
                        dx, dy = ds[idx]
                        if x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n and grid[x + dx][y + dy] != 1:
                            for turn_id in [1]: 
                                if not(x + dx >= 0 and x + dx < m and y + dy >= 0 and y + dy < n):
                                    tmp = 0
                                elif dp[x + dx][y + dy][idx][turn_id] == -1: 
                                    tmp = 1 
                                else: 
                                    tmp = dp[x + dx][y + dy][idx][turn_id] + 1
                                dp[x][y][dir_id][turn_id] = max(tmp, dp[x][y][dir_id][turn_id])
                            print(x, y, dp[x][y][dir_id])
                            # if x == 2 and y == 0: 
                            #     import pdb 
                            #     pdb.set_trace()
        # dfs(2, 3, 1, 1, False)  
        # print(dp[2][3][1])
        # return 0
        ret = 0
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 1: 
                    for didx in range(4):
                        # dp = [[[[-1, -1] for _ in range(4)] for _ in range(n)] for _ in range(m)]
                        # dp[i][j][didx] = [-1, -1] 
                        dfs(i, j, 1, didx, False)
                        ret = max(ret, *dp[i][j][didx])
                        # print(i, j, didx)
                        # print(i, j, ret, didx)
        return ret
    
if __name__ == "__main__": 
    grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    grid = [[2,2,2,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
    grid = [[1,2,2,2,2],[2,2,2,2,0],[2,0,0,0,0],[0,0,2,2,2],[2,0,0,2,0]]
    grid = [[1]]
    grid = [[1,2,2],[1,0,2]]
    grid = [[1,1,1,2,0,0],[0,0,0,0,1,2]]
    grid = [[1,0,1,2,2,1,2],[0,1,2,1,2,0,0],[1,0,1,1,0,0,2]]
    grid = [[2,0,2,0],[1,1,2,2],[2,2,2,1],[1,1,2,0]]
    grid = [[1,1,0,1,1,1,0,2,1,2],[0,1,0,0,2,1,2,1,2,0],[2,0,2,0,2,1,0,2,0,1],[2,2,2,0,2,0,2,0,1,0],[1,0,1,0,1,0,1,0,1,1]]
    ret = Solution().lenOfVDiagonal(grid)
    print(ret)