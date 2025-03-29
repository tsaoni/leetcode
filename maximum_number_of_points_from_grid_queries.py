from typing import List
import numpy as np
from collections import defaultdict

class Solution:
    def maxPoints1(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        disjoint set approach
        """
        n, m = len(grid), len(grid[0])
        Nq = len(queries)
        rank, parent = [0] * n * m, [-1] * n * m
        def find_parent(x): 
            # print("parent", x)
            return x if parent[x] == -1 else find_parent(parent[x])
        
        def joint_set(x1, x2): 
            # print(x1, x2)
            p1 = find_parent(x1)
            p2 = find_parent(x2)
            if p1 != p2:
                if rank[p1] > rank[p2]: 
                    rank[p1] += rank[p2]
                    parent[p2] = p1
                else: 
                    rank[p2] += rank[p1]
                    parent[p1] = p2
            
            return 

        def valid(i, j): 
            return i >= 0 and i < n and j >= 0 and j < m

        numbers = []
        for i in range(n): 
            for j in range(m): 
                idx = m * i + j
                numbers.append((grid[i][j], idx))
        numbers.sort(key=lambda x: x[0])
        
        qidxs = [0] * Nq
        s_queries = []
        for i, idx in enumerate(np.argsort(queries)): 
            qidxs[idx] = i
            s_queries += [queries[idx]]

        ret = [0] * Nq
        qidx, nidx = 0, 0
        while qidx < Nq:
            if s_queries[qidx] > grid[0][0]: 
                break 
            qidx += 1 

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while qidx < Nq: 
            while nidx < n * m: 
                gv, gidx = numbers[nidx]
                if gv >= s_queries[qidx]:
                    break
                r, c = gidx // m, gidx % m
                rank[gidx] = 1
                for di, dj in directions:
                    p = (r + di) * m + (c + dj)
                    if valid(r + di, c + dj) and rank[p] > 0 and grid[r + di][c + dj] <= grid[r][c]: 
                        joint_set(p, gidx)
        
                nidx += 1 
            p = find_parent(0)
            ret[qidx] = rank[p]
            qidx += 1
            # print(numbers)
            # print(parent)
            # print(rank)
            # print()
        
        ret = [ret[qidxs[i]] for i in range(Nq)]
        return ret
    
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        results in TLE
        """
        Nq = len(queries)
        n, m = len(grid), len(grid[0])
        qidxs = [0] * Nq
        s_queries = []
        for i, idx in enumerate(np.argsort(queries)): 
            qidxs[idx] = i
            s_queries += [queries[idx]]
        # print(qidxs)
        
        status = [[-1] * m for _ in range(n)]
        queue = defaultdict(list)
        queue[0, 0].append(0)
        # {(0, 0): [0]}
        def valid(i, j): 
            return i >= 0 and i < n and j >= 0 and j < m
        
        def bfs(queue): 
            if len(queue) > 0:
                n_queue = defaultdict(list)
                for (i, j), slst in queue.items():
                    # update status
                    s = min(slst)
                    while s < Nq: 
                        if grid[i][j] < s_queries[s]: 
                            break
                        s += 1
                    status[i][j] = s  #if status[i][j] == -1 else min(status[i][j], s)
                    # add to next queue
                    if s < Nq: 
                        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                        for di, dj in directions: 
                            if valid(i + di, j + dj): 
                                if s < status[i + di][j + dj] or status[i + di][j + dj] == -1:
                                    n_queue[i + di, j + dj].append(s)
                                # n_queue.append((s, (i + di, j + dj)))
                # print("len n_queue", len(n_queue))
                bfs(n_queue)

        bfs(queue)
        cnt = [0] * Nq
        for i in range(n):
            for j in range(m): 
                idx = status[i][j]
                if idx >= 0 and idx < Nq: 
                    cnt[idx] += 1 
        
        # accumulate
        # print(cnt)
        for i in range(1, Nq): 
            cnt[i] += cnt[i - 1]
        # print(cnt)
        ret = []
        for i in range(Nq): 
            ret.append(cnt[qidxs[i]])
        return ret
    
if __name__ == "__main__": 
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]

    grid = [[5,2,1],[1,1,2]]
    queries = [3]

    # a = set()
    # from itertools import chain
    # for x in chain(*grid): 
    #     a |= {x}
    # a = sorted(list(a))
    # for g in grid: 
    #     print([a.index(x) for x in g])
    # p = []
    # for q in queries: 
    #     r = len(a)
    #     for i, x in enumerate(a): 
    #         if q < x: 
    #             r = i
    #             break
    #     p += [r]
    # print()
    # print(p)
    # exit(-1)


    test_case = (grid, queries)
    ret = Solution().maxPoints(*test_case)
    print(ret)