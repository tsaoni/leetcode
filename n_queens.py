from copy import deepcopy

def print_table(idxs): 
    for idx in idxs: 
        l = [0 for x in range(len(idxs))]
        l[idx] = 1
        tmp = " ".join([str(x) for x in l])
        print(tmp, "\n")
    print("\n")
class Solution:
    def set_flag(self, row, col, n, mode=0): 
        # enable: -1, disable: 1
        x, y = row, col 
        # left, down
        while x + 1 < n and y - 1 >= 0: 
            self.table[x + 1][y - 1] += mode
            x = x + 1
            y = y - 1
        x, y = row, col 
    
        # down
        while x + 1 < n: 
            self.table[x + 1][y] += mode
            x = x + 1
        x, y = row, col 
    
        # right, down 
        while x + 1 < n and y + 1 < n: 
            self.table[x + 1][y + 1] += mode
            x = x + 1
            y = y + 1

    def totalNQueens(self, n: int) -> int:
        self.table = [deepcopy([0] * n) for _ in range(n)] 
        idxs = [-1] * n 
        row_idx = 0
        n_valid = 0
        while True: 
            if idxs[row_idx] >= 0:
                self.set_flag(row_idx, idxs[row_idx], n, mode=-1)
            idxs[row_idx] += 1
            if idxs[row_idx] == n:
                if row_idx == 0: # terminate
                    break 
                else: # move up
                    idxs[row_idx] = -1
                    row_idx -= 1 
            else:
                is_valid = True
                while self.table[row_idx][idxs[row_idx]] > 0: 
                    idxs[row_idx] += 1
                    if idxs[row_idx] == n: # invalid 
                        is_valid = False
                        break
                if not is_valid: # move up
                    idxs[row_idx] = -1
                    row_idx -= 1
                elif row_idx == n - 1: # get a valid sol
                    # print_table(idxs)
                    n_valid += 1
                    idxs[row_idx] = -1
                    row_idx -= 1
                else: # set and move down
                    self.set_flag(row_idx, idxs[row_idx], n, mode=1)
                    row_idx += 1
    
        return n_valid
    

if __name__ == "__main__": 
    test_case = 4
    ret = Solution().totalNQueens(test_case)
    print(ret)