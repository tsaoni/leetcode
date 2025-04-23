from typing import List
from collections import defaultdict

class Solution: 
    def func(): 
        return 
    
    def uniqueXorTriplets1(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: 
            return 1 
        elif N == 2: 
            return 2 
        elif N == 3: 
            return 4 
        else: 
            d = 0 
            n = N
            while n > 0: 
                n //= 2 
                d += 1
            return 2 ** d

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        f, s, t = set(), set(), set()
        ret = set()
        for i, n in enumerate(nums): 
            if i == 0: 
                f.add(n)
                s.add(0)
                t.add(n)
            else: 
                for x in s: 
                    t.add(x ^ n)
                for x in f: 
                    s.add(x ^ n)
                f.add(n)

            ret = ret.union(t)
        # print(ret)
        return len(ret)

    def treeQueries1(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        class SegmentTree: 
            def __init__(self, T, pinfo): 
                self.n = len(T)
                self.tree = [0] * (4 * self.n)
                self.pinfo = pinfo 
            

            def set(self, u, v, w): 
                if self.pinfo[u][0] == v: 
                    delta = w - self.pinfo[u][1] 
                    self.pinfo[u][1] = w
                    r = self.pinfo[u][-1]
                else: 
                    delta = w - self.pinfo[v][1]
                    self.pinfo[v][1] = w
                    r = self.pinfo[v][-1]

                # print(r)
                # import pdb 
                # pdb.set_trace()
                def update(left, right, value, node=0, start=0, end=self.n - 1): 
                    if start >= left and end <= right: 
                        self.tree[node] += value
                    else:
                        # import pdb 
                        # pdb.set_trace()
                        mid = (start + end) // 2 
                        if left <= mid: 
                            update(left, right, value, 2 * node + 1, start, mid)
                        if right >= mid + 1: 
                            update(left, right, value, 2 * node + 2, mid + 1, end)
            

                update(r[0], r[1], delta)

            
            def get_max(self, x, node=0, start=0, end=None): 
                # TODO: add all in range
                end = self.n - 1 if end is None else end
                if start == end: 
                    return self.pinfo[x][2] + self.tree[node]
                else: 
                    idx = self.pinfo[x][-1][0]
                    mid = (start + end) // 2 
                    if idx <= mid: 
                        return self.get_max(x, 2 * node + 1, start, mid) + self.tree[node]
                    else: 
                        return self.get_max(x, 2 * node + 2, mid + 1, end) + self.tree[node]
              
            
        T = [[] for _ in range(n)] 
        for u, v, w in edges: 
            T[u - 1].append((v - 1, w))
            T[v - 1].append((u - 1, w))
        
        pinfo = [[-1, 0, 0, None]] + [None] * (n - 1) # parent id, weights, shortest path, range
        linear_T = [] # store indexes
        def dfs(u, pl): 
            start = len(linear_T)
            linear_T.append(u)
            for v, w in T[u]: 
                if v > 0 and pinfo[v] is None:
                    pinfo[v] = [u, w, pl + w, None]
                    dfs(v, pl + w)
            end = len(linear_T) - 1 
            pinfo[u][-1] = (start, end)
        
        dfs(0, 0) 

        ret = []
        st = SegmentTree(linear_T, pinfo)
        for query in queries: 
            # print(st.tree)
            if query[0] == 1: 
                u, v, w = query[1: ]
                st.set(u - 1, v - 1, w)
            else: 
                x = query[1]
                v = st.get_max(x - 1)
                ret.append(v)
        return ret

    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        """
        abort
        """
        # parent = [-1 for i in range(n)]
        T = [[] for i in range(n)]
        acc = 0
        pl = {1}
        while acc < n - 1:
            npl = set()
            for u, v, w in edges: 
                for p in pl: 
                    if p == u: 
                        T[p - 1].append((v - 1, w))
                        npl.add(v)
                        acc += 1
                    else: 
                        T[p - 1].append((u - 1, w))
                        npl.add(u)
                        acc += 1
            pl = npl

        ret = []
        def update(u, v, w): 
            if T[u - 1][0] == v - 1: 
                T[u - 1] = (v - 1, w)
            else: 
                T[v - 1] = (u - 1, w)
    
        
        def compute(x): 
            cur = 0 
            dist = 0
            while cur != x - 1: 
                cur, d = T[cur]
                d += dist 
            return dist
        
        for q in queries: 
            if q[0] == 1: 
                update(*q[1: ]) 
            else: 
                ret.append(compute(q[1]))
        return ret

if __name__ == "__main__": 
    # nums = [1,3]
    # nums = [6,7,8,9]
    # test_case = (nums, )
    # ret = Solution().uniqueXorTriplets(*test_case)
    
    n = 2
    edges = [[1,2,7]]
    queries = [[2,2],[1,1,2,4],[2,2]]

    # n = 3
    # edges = [[1,2,2],[1,3,4]]
    # queries = [[2,1],[2,3],[1,1,3,7],[2,2],[2,3]]

    # n = 4
    # edges = [[1,2,2],[2,3,1],[3,4,5]]
    # queries = [[2,4],[2,3],[1,2,3,3],[2,2],[2,3]]

    # n = 4 
    # edges = [[1,2,2],[2,3,3],[3,4,4]] 
    # queries = [[2,4],[1,2,3,10],[2,3],[1,2,3,1],[2,3]]

    # n = 10 
    # edges = [[1,2,3969],[4,9,3993],[2,4,9995],[5,6,7868],[1,5,9522],[7,8,4606],[2,3,5012],[2,10,5438],[2,7,1353]] 
    # queries = [[1,2,4,1086],[1,4,9,6913],[2,9],[2,10],[2,4]]

    test_case = (n, edges, queries)
    ret = Solution().treeQueries1(*test_case)
    print(ret)