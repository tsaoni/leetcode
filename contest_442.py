import time
from typing import List
from collections import defaultdict

class Solution: 
    def func(): 
        return 
    
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n ** 2, maxWeight // w)
    
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def intersect(p, graph): 
            cnt = defaultdict(int)
            for x in p: 
                if x in graph: 
                    for idx in graph[x]: 
                        cnt[idx] += 1 
                        if cnt[idx] >= k: 
                            return True
            return False
        
        def merge(g1, g2): 
            g = defaultdict(set)
            idxs = [k for k, _ in g1.items()] + [k for k, _ in g2.items()]
            idxs = sorted(list(set(idxs)))
            for idx in idxs: 
                g[idx] = set()
                if idx in g1: 
                    g[idx] |= g1[idx] 
                if idx in g2: 
                    g[idx] |= g2[idx]
            return g

        pG = []
        for pid, property in enumerate(properties): 
            property = set(property)
            G = []
            merged = []
            for g in pG: 
                if intersect(property, g): 
                    merged += [g]
                else: 
                    G += [g]
            if len(merged) > 0: 
                tmp = merged[0]
                for idx in range(1, len(merged)):
                    tmp = merge(tmp, merged[idx])
                for x in property: 
                    tmp[x] |= {pid}
                G += [tmp]
            else: # no match
                tmp = defaultdict(set)
                for x in property: 
                    tmp[x] |= {pid} 
                G += [tmp]
            pG = G
        return len(G)

    def minTime(self, skill: List[int], mana: List[int]) -> int:
        timeline = []
        acc = 0 
        Ns = len(skill)
        for s in skill: 
            acc += s * mana[0]
            timeline += [acc]
        # [mana[0] * s for s in skill] 
        # start = timeline[0]
        # print(timeline)
        for m in mana[1: ]: 
            # duration = [s * m for s in skill]
            acc = 0
            duration = []
            for s in skill: 
                acc += s * m
                duration += [acc]
            starts = [timeline[i + 1] - duration[i] for i in range(Ns - 1)]
            start = max(starts + [timeline[0]])
            # tmpf = timeline[0] #+ 1
            # tmpb = timeline[-1] - duration[-2] #sum(duration[: -1])
            # start = max(tmpf, tmpb)
            # print(start)
            timeline = [t + start for t in duration]
            # print(timeline)
            # import pdb 
            # pdb.set_trace()

        return timeline[-1]

    def minOperations(self, queries: List[List[int]]) -> int:
        def count(): 
            
            return 
        ret = 0
        for l, r in queries: 
            ret += count(r) - count(l)
        return ret

if __name__ == "__main__": 
    # properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]]
    # k = 1
    # properties = [[1,2,3],[2,3,4],[4,3,5]]
    # k = 2
    # properties = [[1,1],[1,1]]
    # k = 2
    # test_case = (properties, k)
    # ret = Solution().numberOfComponents(*test_case)

    # skill = [1,5,2,4]
    # mana = [5,1,4,2]

    # skill = [1,1,1]
    # mana = [1,1,1]

    # skill = [1,2,3,4]
    # mana = [1,2]

    # skill = [3,5,3,9] 
    # mana = [1,10,7,3]

    # test_case = (skill, mana)

    # ret = Solution().minTime(*test_case)
    

    ret = Solution().minOperations(*test_case)
    print(ret)