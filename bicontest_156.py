from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 
    
    def maxFreqSum(self, s: str) -> int:
        import string 
        string.ascii_lowercase 
        vcnt, ccnt = Counter(), Counter()
        vowels = ['a', 'e', 'i', 'o', 'u']
        for c in s: 
            if c in vowels: 
                vcnt[c] += 1 
            else: 
                ccnt[c] += 1 
        if len(vcnt) > 0:
            vc = max(vcnt, key=lambda x: vcnt[x])
            vc = vcnt[vc]
        else: 
            vc = 0 
        if len(ccnt) > 0:
            cc = max(ccnt, key=lambda x: ccnt[x])
            cc = ccnt[cc]
        else: 
            cc = 0

        return vc + cc

    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ret = 0
        for n in nums: 
            if len(stack) == 0: 
                stack.append(n) 
            else: 
                while len(stack) > 0 and stack[-1] >= n: 
                    tmp = stack.pop(-1) 
                    if tmp > n:
                        ret += 1 
                stack.append(n)
        if len(stack) > 0 and stack[0] == 0: 
            stack.pop(0)
        ret += len(stack)
        return ret

    def maxWeight2(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        """
        use dp
        """
        if k == 0: 
            return 0
        G = [[] for _ in range(n)]
        nonroot = set()
        for u, v, w in edges: 
            G[u].append((v, w))
            nonroot.add(v)
        roots = set([i for i in range(n)]) - nonroot 

        visited = [False] * n
        dp = [[0] * (k + 1) for _ in range(n)]
        def dfs(u): 
            for v, w in G[u]: 
                if not visited[v]:
                    dfs(v)
                for i in range(k): 
                    if i > 0 and dp[u][i] == 0: 
                        break
                    if dp[u][i] + w < t:
                        dp[u][i + 1] = max(dp[u][i] + w, dp[v][i + 1])
            
        
        ret = -1
        for r in roots: 
            dfs(r)
        print(dp)
        for i in range(n):
            if dp[i][k] > 0:
                ret = max(ret, dp[i][k])
        return ret

    def maxWeight1(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        """
        still result in TLE
        """
        G = [[] for _ in range(n)]
        nonroot = set()
        for u, v, w in edges: 
            G[u].append((v, w))
            nonroot.add(v)
        roots = set([i for i in range(n)]) - nonroot 
        
        if k == 0: 
            return 0
        finished = [False] * n
        def dfs(r, edges): 
            tmp = -1
            ret = -1
    
            if len(edges) > k and edges[-k - 1][1] >= 0 and finished[edges[-k - 1][1]]: 
                return ret
            
            # if len(edges) == k: 
            #     val = edges[-1]
            #     # val = sum(edges)
            #     if val < t:
            #         ret = val
            for v, w in G[r]: 
                tmp = -1
                edges.append((edges[-1][0] + w, v))
                # edges.append(w)
                # if len(edges) > k: 
                #     tmp = edges.pop(0)
    
                ret = max(ret, dfs(v, edges))
                if len(edges) > k: 
                    tmp = edges[-1][0] - edges[-k - 1][0]
                    if tmp < t:
                        ret = max(ret, tmp)

                edges.pop(-1)
                # if tmp > 0: 
                #     edges.insert(0, tmp)
        
            finished[r] = True
            return ret
        
        ret = -1
        for r in roots: 
            ret = max(ret, dfs(r, [(0, -1)]))
        return ret

    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        A = [[0] * n for _ in range(n)]
        for u, v, w in edges: 
            A[u][v] = w 
        ret = -1 
        if k == 0: 
            return 0
        elif k == 1: 
            for u in range(n): 
                for v in range(n): 
                    if A[u][v] > 0 and A[u][v] < t: 
                        ret = max(ret, A[u][v])
        else:
            for idx in range(k - 1): 
                A_ = [[0] * n for _ in range(n)]
                for u in range(n): 
                    for v in range(n): 
                        tmp = A[u][v]
                        for p in range(n):
                            if u != v and p != u and p != v: 
                                val = A[u][p] + A[p][v] 
                                if val < t:
                                    tmp = max(tmp, val)
                        if tmp > A[u][v]: 
                            if idx == k - 2:
                                # print(tmp, A[u][v])
                                ret = max(ret, tmp)
                            
                        A_[u][v] = tmp
                A = A_
                # print(A)
        return ret

if __name__ == "__main__": 
    
    # nums = [1,2,1,2,1,2]
    # nums = [0,2]
    # nums = [3,1,2,1]
    # ret = Solution().minOperations(nums)
    # print(ret)

    n = 3
    edges = [[0,1,1],[1,2,2]]
    k = 2
    t = 4

    n = 3
    edges = [[0,1,2],[0,2,3]]
    k = 1
    t = 3

    n = 3
    edges = [[0,1,6],[1,2,8]]
    k = 1
    t = 6

    # n = 2 
    # edges = [[0,1,9]] 
    # k = 2 
    # t = 206

    # n = 24 
    # edges = [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[0,5,1],[0,6,1],[0,7,1],[0,8,1],[0,9,1],[0,10,1],[0,11,1],[0,12,1],[0,13,1],[0,14,1],[0,15,1],[0,16,1],[0,17,1],[0,18,1],[0,19,1],[0,20,1],[0,21,1],[0,22,1],[0,23,1],[1,2,1],[1,3,1],[1,4,1],[1,5,1],[1,6,1],[1,7,1],[1,8,1],[1,9,1],[1,10,1],[1,11,1],[1,12,1],[1,13,1],[1,14,1],[1,15,1],[1,16,1],[1,17,1],[1,18,1],[1,19,1],[1,20,1],[1,21,1],[1,22,1],[1,23,1],[2,3,1],[2,4,1],[2,5,1],[2,6,1],[2,7,1],[2,8,1],[2,9,1],[2,10,1],[2,11,1],[2,12,1],[2,13,1],[2,14,1],[2,15,1],[2,16,1],[2,17,1],[2,18,1],[2,19,1],[2,20,1],[2,21,1],[2,22,1],[2,23,1],[3,4,1],[3,5,1],[3,6,1],[3,7,1],[3,8,1],[3,9,1],[3,10,1],[3,11,1],[3,12,1],[3,13,1],[3,14,1],[3,15,1],[3,16,1],[3,17,1],[3,18,1],[3,19,1],[3,20,1],[3,21,1],[3,22,1],[3,23,1],[4,5,1],[4,6,1],[4,7,1],[4,8,1],[4,9,1],[4,10,1],[4,11,1],[4,12,1],[4,13,1],[4,14,1],[4,15,1],[4,16,1],[4,17,1],[4,18,1],[4,19,1],[4,20,1],[4,21,1],[4,22,1],[4,23,1],[5,6,1],[5,7,1],[5,8,1],[5,9,1],[5,10,1],[5,11,1],[5,12,1],[5,13,1],[5,14,1],[5,15,1],[5,16,1],[5,17,1],[5,18,1],[5,19,1],[5,20,1],[5,21,1],[5,22,1],[5,23,1],[6,7,1],[6,8,1],[6,9,1],[6,10,1],[6,11,1],[6,12,1],[6,13,1],[6,14,1],[6,15,1],[6,16,1],[6,17,1],[6,18,1],[6,19,1],[6,20,1],[6,21,1],[6,22,1],[6,23,1],[7,8,1],[7,9,1],[7,10,1],[7,11,1],[7,12,1],[7,13,1],[7,14,1],[7,15,1],[7,16,1],[7,17,1],[7,18,1],[7,19,1],[7,20,1],[7,21,1],[7,22,1],[7,23,1],[8,9,1],[8,10,1],[8,11,1],[8,12,1],[8,13,1],[8,14,1],[8,15,1],[8,16,1],[8,17,1],[8,18,1],[8,19,1],[8,20,1],[8,21,1],[8,22,1],[8,23,1],[9,10,1],[9,11,1],[9,12,1],[9,13,1],[9,14,1],[9,15,1],[9,16,1],[9,17,1],[9,18,1],[9,19,1],[9,20,1],[9,21,1],[9,22,1],[9,23,1],[10,11,1],[10,12,1],[10,13,1],[10,14,1],[10,15,1],[10,16,1],[10,17,1],[10,18,1],[10,19,1],[10,20,1],[10,21,1],[10,22,1],[10,23,1],[11,12,1],[11,13,1],[11,14,1],[11,15,1],[11,16,1],[11,17,1],[11,18,1],[11,19,1],[11,20,1],[11,21,1],[11,22,1],[11,23,1],[12,13,1],[12,14,1],[12,15,1],[12,16,1],[12,17,1],[12,18,1],[12,19,1],[12,20,1],[12,21,1],[12,22,1],[12,23,1],[13,14,1],[13,15,1],[13,16,1],[13,17,1],[13,18,1],[13,19,1],[13,20,1],[13,21,1],[13,22,1],[13,23,1],[14,15,1],[14,16,1],[14,17,1],[14,18,1],[14,19,1],[14,20,1],[14,21,1],[14,22,1],[14,23,1],[15,16,1],[15,17,1],[15,18,1],[15,19,1],[15,20,1],[15,21,1],[15,22,1],[15,23,1],[16,17,1],[16,18,1],[16,19,1],[16,20,1],[16,21,1],[16,22,1],[16,23,1],[17,18,1],[17,19,1],[17,20,1],[17,21,1],[17,22,1],[17,23,1],[18,19,1],[18,20,1],[18,21,1],[18,22,1],[18,23,1],[19,20,1],[19,21,1],[19,22,1],[19,23,1],[20,21,1],[20,22,1],[20,23,1],[21,22,1],[21,23,1],[22,23,1]]
    # k = 12 
    # t = 600

    # n = 5
    # edges = [[0,1,3],[0,4,10],[2,3,8],[3,4,5],[0,2,9],[1,3,3],[0,3,2],[2,4,2]]
    # k = 2 
    # t = 5

    # n = 3
    # edges = [[0,1,8],[0,2,8],[1,2,9]]
    # k = 1 
    # t = 511

    # n = 6
    # edges = [[0,5,7],[1,2,10],[2,5,5],[0,3,4],[1,5,7],[0,4,4],[1,3,4],[2,3,5],[0,2,6],[2,4,10],[3,4,2],[1,4,2],[0,1,1]]
    # k = 2 
    # t = 451

    n = 7
    edges = [[5,6,9],[0,6,2],[3,4,10],[4,5,1],[1,3,1],[2,5,6],[3,6,2],[2,4,3],[0,1,2],[4,6,7],[2,6,8],[0,2,8],[1,5,5],[1,4,8]]
    k = 1 
    t = 414

    n = 4 
    edges = [[0,1,4],[0,2,3],[1,2,9],[2,3,5],[0,3,5]] 
    k = 2 
    t = 11

    ret = Solution().maxWeight2(n, edges, k, t)
    print(ret)