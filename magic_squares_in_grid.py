from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        sm = 15 
        tgt = int("1" * 9, 2)
        N, M = len(grid), len(grid[0])
        ret = 0
        set_bit = lambda x, sft, b: x & (7 - (b << sft))
        for i in range(2, N): 
            is_col_magic = 7
            s3 = [0] * 3
            for j in range(2, M): 
                is_row_magic = True 
                if j == 2:
                    for k in range(3): 
                        # print(i, j, k)
                        s3[k] = sum(grid[i - k][j - 2: j + 1])
                        x = sum([grid[i - idx][k] for idx in range(3)])
                        # print(is_col_magic, k, x)
                        is_col_magic &= set_bit(is_col_magic, k, not (x == 15)) #((x == 15) << k)
                        # print(is_col_magic, k, x)
                        is_row_magic &= (s3[k] == 15)
                else: 
                    for k in range(3): 
                        s3[k] += grid[i - k][j]
                        s3[k] -= grid[i - k][j - 3]
                        is_row_magic &= (s3[k] == 15) 
                    is_col_magic >>= 1
                    is_col_magic |= 4
                    x = sum([grid[i - idx][j] for idx in range(3)]) 
                    is_col_magic &= set_bit(is_col_magic, 2, not (x == 15)) #((x == 15) << 2)
                
                
                x1 = sum([grid[i - k][j - k] for k in range(3)])
                x2 = sum([grid[i - 2 + k][j - k] for k in range(3)])
                is_dia_magic = (x1 == 15) & (x2 == 15) 

                st = 0 
                for dr in range(3): 
                    for dc in range(3): 
                        x = grid[i - dr][j - dc]
                        if x > 0 and x <= 9: 
                            st |= (1 << (x - 1))
                        else: 
                            break

                # if i == 4 and j == 2: #is_row_magic | (is_col_magic == 7): 
                #     import pdb 
                #     pdb.set_trace()
                if is_row_magic & (is_col_magic == 7) & is_dia_magic & (st == tgt): 
                    ret += 1
                    # print(i, j)
                # print(is_col_magic, [grid[i - k][j] for k in range(3)])
                # print(s3, is_row_magic, is_col_magic)
                # import pdb 
                # pdb.set_trace()

        return ret 
    
if __name__ == "__main__": 
    grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
    grid = [[8]]
    grid = [[5,5,5],[5,5,5],[5,5,5]]
    grid = [[10,3,5],[1,6,11],[7,9,2]]
    grid = [[7,0,5],[2,4,6],[3,8,1]]
    grid = [[3,2,1,6],[5,9,6,8],[1,5,1,2],[3,7,3,4]]
    grid = [[3,10,2,3,4],[4,5,6,8,1],[8,8,1,6,8],[1,3,5,7,1],[9,4,9,2,9]]
    ret = Solution().numMagicSquaresInside(grid)
    print(ret)