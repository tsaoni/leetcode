from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from itertools import chain
        N = len(board)
        table = list(chain(*[board[N - i - 1] if i & 1 == 0 else list(reversed(board[N - i - 1])) for i in range(N)]))
        visited = [False] * len(table)
        # print(table)
        curr = {1}
        # table[0] = -2
        step = 0
        while len(curr) > 0: 
            ncurr = set()
            for cidx in curr: 
                if cidx == N * N: 
                    return step
                for ncidx in range(cidx + 1, min(N * N + 1, cidx + 7)): 
                    tmp = ncidx
                    for i in range(2):
                        if ncidx >= 0: 
                            prev = ncidx
                            ncidx = table[ncidx - 1]
                            # if i == 0:
                            #     table[prev - 1] = -2
                    
                    # table[tmp - 1] = -2
                    # if ncidx >= -1: 
                    if not visited[prev - 1]:
                        ncurr.add(prev)
                visited[cidx - 1] = True
                # table[cidx - 1] = -2
            # print(table)
            # print(ncurr)
            step += 1
            curr = ncurr

        return -1
    
if __name__ == "__main__": 
    board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
    board = [[-1,-1],[-1,3]]
    # board = [[-1,4,-1],[6,2,6],[-1,3,-1]]
    # board = [[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]
    board = [[-1,-1,-1,46,47,-1,-1,-1],[51,-1,-1,63,-1,31,21,-1],[-1,-1,26,-1,-1,38,-1,-1],[-1,-1,11,-1,14,23,56,57],[11,-1,-1,-1,49,36,-1,48],[-1,-1,-1,33,56,-1,57,21],[-1,-1,-1,-1,-1,-1,2,-1],[-1,-1,-1,8,3,-1,6,56]]

    ret = Solution().snakesAndLadders(board)
    print(ret)