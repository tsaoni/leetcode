from typing import List

class Solution:
    def minimumCost1(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        DFS
        """
        G = [[] for _ in range(n)] 
        for v1, v2, c in edges: 
            G[v1] += [[v2, c]]
            G[v2] += [[v1, c]]

        def bitwise_and(x1, x2): 
            ret = 0
            mul = 1
            # if x1 < 0: 
            #     return x2
            while x1 > 0 and x2 > 0: 
                b1, b2 = x1 % 2, x2 % 2
                ret += (b1 & b2) * mul 
                x1 //= 2 
                x2 //= 2
                mul *= 2
            return ret

        max_val = 2 ** 17 - 1
        vals = {}
        sets = [-1] * n
        set_idx = 0
        def dfs(v): 
            sets[v] = set_idx
            val = max_val
            for v2, c in G[v]: 
                val = bitwise_and(val, c)
                if sets[v2] < 0: 
                    tmp = dfs(v2)
                    val = bitwise_and(val, tmp)
            return val

        for i in range(n): 
            if sets[i] < 0:
                vals[set_idx] = dfs(i)   
                set_idx += 1   
            # print(sets)  
            # print(vals)
    
        ret = []
        for v1, v2 in query: 
            if sets[v1] == sets[v2]: 
                set_idx = sets[v1]
                ret += [vals[set_idx]] 
            else: 
                ret += [-1]
        return ret

    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        """
        use disjoint set (TLE)
        """
        roots = [-1] * n 
        vals = [-1] * n
        def bitwise_and(x1, x2): 
            ret = 0
            mul = 1
            if x1 < 0: 
                return x2
            while x1 > 0 and x2 > 0: 
                b1, b2 = x1 % 2, x2 % 2
                ret += (b1 & b2) * mul 
                x1 //= 2 
                x2 //= 2
                mul *= 2
            return ret

        def find_parent(v): 
            h = 0
            while roots[v] != -1: 
                v = roots[v]
                h += 1
            return v, h

        def collapse(v, p): 
            for i, x in enumerate(roots): 
                if x == v: 
                    roots[i] = p

        for v1, v2, c in edges: 
            p1, h1 = find_parent(v1)
            p2, h2 = find_parent(v2)
            if p1 == p2: 
                vals[p1] = bitwise_and(vals[p1], c)
                # print(p1, c, vals[p1])
            else: 
                if True: #h1 > h2: 
                    roots[p2] = p1
                    tmp = bitwise_and(vals[p2], bitwise_and(vals[p1], c))
                    vals[p1] = tmp
                    collapse(p2, p1)
                    # print(p1, c, vals[p1])
                else: 
                    roots[p1] = p2
                    tmp = bitwise_and(vals[p1], bitwise_and(vals[p2], c))
                    vals[p2] = tmp
                    # print(p2, c, vals[p2])
        
        ret = []
        for v1, v2 in query: 
            p1, _ = find_parent(v1)
            p2, _ = find_parent(v2)
            if p1 == p2: 
                ret += [vals[p1]]
            else: 
                ret += [-1]
        # print(roots)
        # print(vals)
        return ret
    



if __name__ == "__main__": 
    n = 5
    edges = [[0,1,7],[1,3,7],[1,2,1]]
    query = [[0,3],[3,4]]
    
    n = 3
    edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]
    query = [[1,2]]

    n = 4
    edges = [[2,3,1],[1,3,5],[1,2,6],[3,0,7],[1,3,7],[0,2,5],[0,1,7]]
    query = [[2,1],[1,2],[0,1],[2,0],[0,2],[1,2],[3,2],[0,3],[2,1],[1,2]]

    # n = 9
    # edges = [[8,2,0],[4,7,3],[5,8,1],[1,3,5]] 
    # query = [[1,6],[1,0],[4,1],[5,3],[0,4],[3,4],[2,3],[0,8]]

    test_case = (n, edges, query)
    ret = Solution().minimumCost1(*test_case)
    print(ret)