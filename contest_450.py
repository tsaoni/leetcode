from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 

    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)): 
            d = 0 
            tmp = nums[i] 
            while tmp > 0:
                d += tmp % 10 
                tmp //= 10
            if i == d: 
                return i
        return -1
    
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n): 
            d = 0 
            tmp = n
            while tmp > 0:
                d += tmp % 10 
                tmp //= 10
            return d
        ref = sorted([(get_digit_sum(n), n, i) for i, n in enumerate(nums)])
        ret = 0
        # print(ref)
        
        visit = [0] * len(nums) 
        for i in range(len(nums)): 
            idx = i
            while visit[idx] != 1: 
                visit[idx] = 1 
                idx = ref[idx][-1]
                if visit[idx] == 0: 
                    ret += 1
            
        # for n1, (_, n2) in zip(nums, ref): 
        #     if n1 != n2: 
        #         ret += 1
        return ret 

    def minMoves(self, matrix: List[str]) -> int:
        from collections import defaultdict
        import heapq
        m, n = len(matrix), len(matrix[0])
        # grid = [[c for c in m] for m in matrix]
        dest = [[-1] * n for _ in range(m)]
        dest[0][0] = 0
        paths = [(0, 0)] 
        port = defaultdict(list)
        for i in range(m): 
            for j in range(n): 
                if not matrix[i][j] in [".", "#"]: 
                    port[matrix[i][j]].append((i, j))
        
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while len(paths) > 0: 
            npaths = []
            for i, j in paths: 
                dst = dest[i][j]
                for di, dj in d:
                    if i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n:
                        if (dest[i + di][j + dj] == -1 or dest[i + di][j + dj] > dst + 1)  and matrix[i + di][j + dj] != "#": 
                            dest[i + di][j + dj] = dst + 1
                            npaths.append((i + di, j + dj))
                
                if matrix[i][j] != ".": 
                    for ti, tj in port[matrix[i][j]]: 
                        if dest[ti][tj] == -1 or dest[ti][tj] > dst: 
                            npaths.append((ti, tj))
                            dest[ti][tj] = dst 
                    
            paths = npaths
            
        return dest[-1][-1]
        

if __name__ == "__main__": 
    nums = [37,100]
    # nums = [22,14,33,7]
    # nums = [18,43,34,16]
    # ret = Solution().minSwaps(nums)
    # print(ret)

    matrix = ["A..",".A.","..."]
    matrix = [".#...",".#.#.",".#.#.","...#."]
    ret = Solution().minMoves(matrix)
    print(ret)
    