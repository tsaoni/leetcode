from typing import List
import heapq

class Heap: 
    """a very inefficient heap operation :')"""
    def __init__(self, cur): 
        self.record = {}
        self.heap = []
        for idx, (i, j, v) in enumerate(cur): 
            self.record[i, j] = idx 
            self.heap.append((v, i, j))
    
    def add(self, v, i, j): 
        # implement both add and update
        if (i, j) in self.record: 
            idx = self.record[i, j]
            # print(self.heap, self.record, idx)
            self.heap[idx] = (v, i, j)
        else: 
            self.heap.append((v, i, j))
            idx = len(self.heap) - 1 
        while idx > 0: 
            p = (idx - 1) // 2
            if self.heap[p][0] > self.heap[idx][0]: 
                tv, ti, tj = self.heap[p] 
                self.record[ti, tj] = idx
                self.heap[idx] = self.heap[p]
                idx = p
            else: 
                break
        
        self.heap[idx] = (v, i, j)

        self.record[i, j] = idx

    
    def pop(self): 
        rv, ri, rj = self.heap[0]
        del self.record[ri, rj]

        v, i, j = self.heap.pop(-1)
        p, idx = 0, 1
        N = len(self.heap) - 1
        # print(self.heap)
        # print(self.record)
        # import pdb 
        # pdb.set_trace()
        while idx < N: 
            if idx + 1 < N and self.heap[idx][0] > self.heap[idx + 1][0]: 
                idx = idx + 1
            if self.heap[p] <= self.heap[idx]: 
                break
            tv, ti, tj = self.heap[idx]
            self.record[ti, tj] = p
            self.heap[p] = (tv, ti, tj)
            p = idx
            idx = idx * 2 + 1 

        if len(self.heap):
            self.heap[p] = (v, i, j)
            self.record[i, j] = p
        # if (i, j) not in self.record: 
        #     print(self.heap)
        #     print(self.record)
        
        return rv, ri, rj

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        cur = {(0, 0)}
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * m for _ in range(n)]
        dp[0][0] = 0#moveTime[0][0]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while len(cur) > 0: 
            ncur = set()
            for i, j in cur:
                for di, dj in d:
                    if i + di >= 0 and i + di < n and j + dj >= 0 and j + dj < m:
                        t = max(dp[i][j] + 1, moveTime[i + di][j + dj] + 1)
                        if dp[i + di][j + dj] > t: 
                            dp[i + di][j + dj] = t
                            ncur.add((i + di, j + dj))
            cur = ncur
        return dp[-1][-1]
    
    def minTimeToReach_1(self, moveTime: List[List[int]]) -> int:
        """
        results in TLE
        """
        import heapq
        # cur = [(0, 0)] 
        heap = Heap([(0, 0, 0)])
        n, m = len(moveTime), len(moveTime[0])
        dp = [[float("inf")] * m for _ in range(n)]
        states = [[-1] * m for _ in range(n)]
        states[0][0] = 0
        dp[0][0] = 0#moveTime[0][0]
        d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while len(heap.heap) > 0: 
            # ncur = set()
            # print(heap.heap)
            # print(heap.record)
            # print()
            v, i, j = heapq.heappop(heap.heap)
            # v, i, j = heap.pop()
            if v >= dp[-1][-1]: 
                continue
            if i == n - 1 and j == m - 1: 
                return dp[-1][-1]
            # for i, j in cur:
            for di, dj in d:
                if i + di >= 0 and i + di < n and j + dj >= 0 and j + dj < m:
                    dt = states[i][j] + 1
                    t = max(v + dt, moveTime[i + di][j + dj] + dt)
                    if dp[i + di][j + dj] > t: 
                        dp[i + di][j + dj] = t
                        states[i + di][j + dj] = (states[i][j] + 1) % 2
                        # heap.add(t, i + di, j + dj)
                        heapq.heappush(heap.heap, (t, i + di, j + dj))
                        # ncur.a((i + di, j + dj))
            # if i == n - 1 and j == m - 1: 
            #     return dp[-1][-1]
            # cur = ncur
    
        return dp[-1][-1]


if __name__ == "__main__": 
    moveTime = [[0,4],[4,4]]
    moveTime = [[0,0,0],[0,0,0]]
    moveTime = [[0,0,0,0],[0,0,0,0]]
    # moveTime = [[0,1],[1,2]]
    # moveTime = [[56,93],[3,38]]
    moveTime = [[12,71,74],[72,77,75]]
    moveTime = [[49,20,98],[19,87,96],[70,41,77]]
    moveTime = [[47,49,14],[79,47,5],[1,70,67]]
    ret = Solution().minTimeToReach_1(moveTime)
    print(ret)