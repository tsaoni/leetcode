from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        import heapq
        G = defaultdict(list)
        _G = defaultdict(list)
        for u, v, w in edges: 
            G[u].append((v, w))
            _G[v].append((u, w))
        dist = [float("inf") for _ in range(n)]
        dist[0] = 0 
        pos = [-1] * n 
        q = [(0, 0)]
        def hmod(q, v, v_updated): 
            if pos[v] < 0: 
                # heapq.heappush(q, (v_updated, v))
                q.append((v_updated, v))
                pos[v] = len(q) - 1
            else:
                # import pdb 
                # pdb.set_trace()
                cur = pos[v]
                q[cur] = (v_updated, v)
            cur = pos[v]
            while cur > 0: 
                # print(len(q), cur, pos)
                p = (cur - 1) // 2 
                if q[p][0] < q[cur][0]: 
                    break 
                else: 
                    pos[q[p][1]] = cur 
                    pos[q[cur][1]] = p 
                    tmp = q[p]
                    q[p] = q[cur]
                    q[cur] = tmp 
                    cur = p 
            

        while len(q) > 0: 
            # import pdb 
            # pdb.set_trace()
            d, u = q[0]
            if u == n - 1: 
                return d 
            if len(q) > 1: 
                ld, lu = q.pop(-1)
                q[0] = (ld, lu)
                cur = 0
                pos[lu] = cur
                while cur < len(q): 
                    l, r = cur * 2 + 1, cur * 2 + 2 
                    nxt = cur 
                    if l < len(q) and q[l][0] < q[nxt][0]: 
                        nxt = l 
                    if r < len(q) and q[r][0] < q[nxt][0]: 
                        nxt = r 
                    if nxt > cur: 
                        # import pdb 
                        # pdb.set_trace()
                        pos[q[nxt][1]] = cur 
                        pos[q[cur][1]] = nxt 
                        tmp = q[cur]
                        q[cur] = q[nxt]
                        q[nxt] = tmp 
                        cur = nxt 
                        # import pdb 
                        # pdb.set_trace()
                    else: 
                        break 
                # import pdb 
                # pdb.set_trace()
            else: 
                q = []
            # print(u, q)
            pos[u] = -1 
            for v, w in G[u]: 
                if d + w < dist[v]:
                    dist[v] = d + w
                    hmod(q, v, dist[v])
                    
            for v, w in _G[u]: 
                if d + 2 * w < dist[v]:
                    dist[v] = d + 2 * w 
                    hmod(q, v, dist[v])
            # print(q)
        return -1
    
if __name__ == "__main__": 
    n = 4
    edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]
    n = 4
    edges = [[0,2,1],[2,1,1],[1,3,1],[2,3,3]]
    n = 4 
    edges = [[0,2,2],[0,1,24],[3,1,8],[1,0,15],[3,0,23],[2,0,24]]
    ret = Solution().minCost(n, edges)
    print(ret)