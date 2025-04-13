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

    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
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
    
    ret = Solution().treeQueries
    print(ret)