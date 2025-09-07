from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find(x, y, board=board): 
            for i in range(x, 9): 
                if i == x: 
                    for j in range(y, 9): 
                        if board[i][j] == ".": 
                            return (i, j)
                else: 
                    for j in range(9): 
                        if board[i][j] == ".": 
                            return (i, j)
            return None
        
        row, col, grid = [0] * 9, [0] * 9, [0] * 9
        def setMask(i, j, board=board, row=row, col=col, grid=grid): 
            tmp = 1 << (int(board[i][j]) - 1)
            row[i] |= tmp
            col[j] |= tmp
            idx = i // 3 * 3 + j // 3 % 3
            grid[idx] |= tmp

        def unMask(i, j, board=board, row=row, col=col, grid=grid): 
            tmp = 1 << (int(board[i][j]) - 1)
            row[i] ^= tmp
            col[j] ^= tmp
            idx = i // 3 * 3 + j // 3 % 3
            grid[idx] ^= tmp

        for i in range(9): 
            for j in range(9): 
                if board[i][j] != ".": 
                    setMask(i, j)

        def bit_check(x, y, board=board, row=row, col=col, grid=grid): 
            tmp = 1 << (int(board[x][y]) - 1)
            idx = x // 3 * 3 + y // 3 % 3
            return not(row[x] & tmp or col[y] & tmp or grid[idx] & tmp)
            
        
        def check(x, y): 
            pivot_fn = lambda x: x // 3 * 3 
            g_x, g_y = pivot_fn(x), pivot_fn(y)
            for i in range(9): 
                if i != x and board[i][y] == board[x][y]: 
                    return False 
                if i != y and board[x][i] == board[x][y]: 
                    return False 
                if g_x + i // 3 != x and g_y + i % 3 != y and board[g_x + i // 3][g_y + i % 3] == board[x][y]: 
                    return False
            return True

        pos = []
        for i in range(9): 
            for j in range(9): 
                if board[i][j] == ".": 
                    pos.append((i, j))
        pos.append(None)
        def solve(cur, board=board, pos=pos): 
            # _cur = find(*cur)
            # print(cur)
            _cur = pos[cur]
            if _cur is not None:
                is_solve = False
                x, y = _cur
                for i in map(str, range(1, 10)):
                    board[x][y] = i
                    if bit_check(x, y): 
                        # print(x, y, i, board[x][y])
                        # import pdb 
                        # pdb.set_trace()
                        setMask(x, y)
                        is_solve = solve(cur + 1)
                        if is_solve: 
                            return True 
                        unMask(x, y)
                    
                board[x][y] = "."
                return False
            else: 
                return True
        
        solve(0)
        

if __name__ == "__main__": 
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
    Solution().solveSudoku(board)
    for x in board: 
        print(x)