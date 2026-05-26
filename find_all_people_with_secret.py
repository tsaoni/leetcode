from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        import heapq
        G = [[] for _ in range(n)]
        G[0].append((firstPerson, 0))
        G[firstPerson].append((0, 0))
        A = [float("inf")] * n 
        A[0] = A[firstPerson] = 0
        meetings.sort(key=lambda x: x[2])
        for x, y, t in meetings: 
            G[x].append((y, t))
            G[y].append((x, t))

        q = [(0, 0), (0, firstPerson)]
        heapq.heapify(q)
        def bfs(q): 
            while len(q) > 0: 
                t, cur = heapq.heappop(q)
                if t > A[cur]: 
                    continue 
                for tgt, t in G[cur]: 
                    if t >= A[cur]:
                        if A[tgt] > t:
                            A[tgt] = t 
                            heapq.heappush(q, (t, tgt))
        
        bfs(q)
        return [i for i in range(n) if A[i] < float("inf")]
    
    def findAllPeople_1(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """
        Union Find / TLE
        """
        meetings.sort(key=lambda x: x[2])
        prev = -1
        # G = [-1] * n 
        # C = [1] * n
        G = set()
        G.add(firstPerson)
        # C[0] += 1
        # roots = set()
        def find(x, G): 
            cands = set()
            while x in G: 
                cands.add(x)
                x = G[x]
            for c in cands: # collapse
                G[c] = x
            return x if x not in G else find(G[x], G)
        _G = {}
        for x, y, t in meetings: 
            if t != prev: 
                if len(_G) > len(G): 
                    for c, p in _G.items(): 
                        if find(c, _G) == 0: 
                            G.add(c)
                # import pdb 
                # pdb.set_trace()
                _G = {x: 0 for x in G}
                # roots = set()
            if True: 
                px, py = find(x, _G), find(y, _G)
                # if px == 0 or py == 0: 
                    # _G[px] = _G[py] = 0 
                    # C[0] += sum([C[p] for p in [px, py] if p != 0])
                if True: 
                    p1, p2 = min(px, py), max(px, py)
                    if p1 != p2:
                        _G[p2] = p1 
                        if p2 == px:
                            find(x, _G)
                        else: 
                            find(y, _G)
                    # C[p1] += C[p2]
                    # roots.add(p1)
            prev = t 

        if len(_G) > len(G): 
            # print(_G)
            for c, p in _G.items(): 
                if find(c, _G) == 0: 
                    G.add(c)
        
        return [i for i in range(n) if i in G or i == 0] 

if __name__ == "__main__": 
    n = 6
    meetings = [[1,2,5],[2,3,8],[1,5,10]]
    firstPerson = 1

    n = 4
    meetings = [[3,1,3],[1,2,2],[0,3,3]]
    firstPerson = 3

    n = 5
    meetings = [[3,4,2],[1,2,1],[2,3,1]]
    firstPerson = 1

    # n = 5
    # meetings = [[1,4,3],[0,4,3]]
    # firstPerson = 3

    ret = Solution().findAllPeople(n, meetings, firstPerson)
    print(ret)