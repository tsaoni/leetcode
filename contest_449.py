from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 
    def minDeletion(self, s: str, k: int) -> int:
        from collections import defaultdict, Counter
        d = Counter()
        for c in s: 
            d[c] += 1 
        
        return sum(sorted([v for k, v in d.items()])[: -k])

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        from itertools import chain 
        total = sum(list(chain(*grid)))
        if total % 2 == 1: 
            return False 
        else: 
            acc = 0
            limit = total // 2
            for g in grid: 
                acc += sum(g) 
                if acc == limit: 
                    return True 
                if acc > limit: 
                    break 
            
            acc = 0
            for g in zip(*grid): 
                acc += sum(g) 
                if acc == limit: 
                    return True 
                if acc > limit: 
                    break 
        return False

    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        n_ev = {}
        G = {}
        for u, v in edges: 
            if u in G and v in G: 
                if G[u] == v: 
                    v1, _ = n_ev[tuple(sorted([u, v]))] 
                    n_ev[tuple(sorted([u, v]))] = (v1, v1)
                else: 
                    G[G[u]] = G[v]
                    G[G[v]] = G[u]
                    v1, _ = n_ev[tuple(sorted([u, G[u]]))] 
                    v2, _ = n_ev[tuple(sorted([v, G[v]]))] 
                    n_ev[tuple(sorted([G[u], G[v]]))] = (v1 + v2, v1 + v2 - 1)

                    del n_ev[tuple(sorted([u, G[u]]))]
                    del n_ev[tuple(sorted([v, G[v]]))]

                del G[u]
                del G[v]
            elif u not in G and v in G: 
                G[u] = G[v]
                G[G[v]] = u 
                v1, _ = n_ev[tuple(sorted([v, G[v]]))] 
                n_ev[tuple(sorted([u, G[u]]))] = (v1 + 1, v1)
                del n_ev[tuple(sorted([v, G[v]]))] 
                del G[v]

            elif u in G and v not in G: 
                G[v] = G[u]
                G[G[u]] = v
                v1, _ = n_ev[tuple(sorted([u, G[u]]))] 
                n_ev[tuple(sorted([v, G[v]]))] = (v1 + 1, v1)
                del n_ev[tuple(sorted([u, G[u]]))] 
                del G[u]

            else: 
                G[u] = v 
                G[v] = u 
                n_ev[tuple(sorted([u, v]))] = (2, 1)

        # print(G, n_ev)
        ret = 0
        lines, cycles = [], []
        for v, e in n_ev.values(): 
            if v == e: 
                cycles.append(v)
            else: 
                lines.append(v)
        
        # print(cycles, lines)
        ret = 0
        start = 1
        for v in sorted(lines): 
            end = start + v - 1 
            if v == 2: 
                ret += start * (start + 1)
            else:
                ret += start * (start + 2)
                ret += (start + 1) * end
                ret += sum([i * (i + 1) for i in range(start + 2, end)])
            start += v 
        
        # print(start)
        for v in sorted(cycles): 
            end = start + v - 1 
            ret += sum([i * (i + 1) for i in range(start, end)])
            ret += start * end
            start += v 

        return ret

if __name__ == "__main__": 
    # ret = Solution().minDeletion("abc", 2)
    # grid = [[1,2],[4,3]]
    # ret = Solution().canPartitionGrid(grid)
    n = 7
    edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6]]
    n = 6
    edges = [[0,3],[4,5],[2,0],[1,3],[2,4],[1,5]]
    ret = Solution().maxScore(n, edges)
    print(ret)