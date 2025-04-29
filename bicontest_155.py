from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(): 
        return 
    
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnt = Counter()
        for resp in responses: 
            for r in set(resp): 
                cnt[r] += 1 
        ret, maxv = None, -1
        for k, v in cnt.items(): 
            if not ret: 
                ret = k
                maxv = v 
            else: 
                if v > maxv: 
                    ret = k
                    maxv = v
                elif v == maxv: 
                    if k < ret:
                        ret = k
        return ret #max(cnt, key=lambda x: cnt[x])

    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        N = len(conversions) + 1
        parents = [-1] * N
        fs = [1] + [-1] * (N - 1)
        modulo = 10 ** 9 + 7
        for s, t, f in conversions: 
            fs[t] = f
            # parents[t] = s
            p = s
            while parents[p] != -1: 
                np = parents[p]
                fs[s] *= fs[np]
                fs[s] %= modulo
                fs[t] *= fs[p]
                fs[t] %= modulo
                p = np
            if parents[p] != -1: 
                parents[s] = p
            parents[t] = p

        ret = [1]
        for i in range(1, N): 
            tmp = i
            f = 1
            while parents[tmp] != -1: 
                f *= fs[tmp]
                f %= modulo
                tmp = parents[tmp]
            ret.append(f)
        return ret

    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        # import numpy as np
        nr, nc = len(grid), len(grid[0])
        hs = "".join(["".join(x) for x in grid])
        vs = "".join(["".join([grid[j][i] for j in range(nr)]) for i in range(nc)])
        # print(hs)
        # print(vs)
        
        hidx_fn = lambda idx: (idx // nc, idx % nc) #lambda r, c: nr * r + c 
        vidx_fn = lambda idx: (idx % nc, idx // nc) #lambda r, c: nc * c + r
        hbm, vbm = [0] * nr * nc, [0] * nr * nc
    
        def match(s, bitmap): 
            idx = 0
            ret = []
            N = len(pattern)
            while idx <= nr * nc: 
                start = max(0, idx - N)
                if s[start: idx] == pattern: 
                    bitmap[start: idx] = [1] * N
                    # ret.extend([x for x in range(start, idx)])
                    # for i in range(start, idx): 
                    #     bitmap[i] = 1 
                    # idx += N
            
                idx += 1
            # return set(ret) 
        
        match(hs, hbm)
        match(vs, vbm)
        # print(hbm)
        # print(vbm)
        ret = 0
        for i in range(nr * nc): 
        # i = 0 
        # while i < nr * nc: 

            if hbm[i] == 1: 
                r, c = hidx_fn(i)
                vidx = nr * c + r 
                # print(r, c, vidx, vbm[vidx])
        
                ret += vbm[vidx]

        return ret
    
    def countCells1(self, grid: List[List[str]], pattern: str) -> int:
        # import numpy as np
        from itertools import chain
        
        nr, nc = len(grid), len(grid[0])
        
        hs = "".join(chain(*grid))
        vs = "".join(["".join([grid[j][i] for j in range(nr)]) for i in range(nc)])
        # print(hs)
        # print(vs)
        
        hidx_fn = lambda idx: (idx // nc, idx % nc) #lambda r, c: nr * r + c 
        vidx_fn = lambda idx: (idx % nr, idx // nr) #lambda r, c: nc * c + r
        hbm, vbm = [0] * nr * nc, [0] * nr * nc
    
        def kmp(s): 
            idxs = [-1] + [0] * len(s)
            pos, cnd = 2, 0 
            while pos < len(s) + 1: 
                if s[pos - 1] == s[cnd]: 
                    cnd += 1 
                    idxs[pos] = cnd 
                    pos += 1
                   
                elif cnd > 0: 
                    cnd = idxs[cnd]
                else: 
                    idxs[pos] = 0
                    pos += 1 
           
            return idxs

        # ret = kmp(pattern)

        def match(s, bitmap): 
            sidx, pidx = 0, 0
            ret = []
            N = len(pattern)
            idxs = kmp(pattern)
            while sidx <= nr * nc: 
                
                if pidx == N or s[sidx] != pattern[pidx]: 
                    kmp
                if s[sidx] == pattern[pidx]: 
                    sidx += 1 
                    pidx += 1
                # this will cost more time.. 
                # tmp = s[idx:].index(pattern) if pattern in s[idx:] else -1
                # if tmp < 0: 
                #     break
                # nidx = tmp + idx
                # bitmap[nidx: nidx + N] = [1] * N
                # idx = nidx + 1
                
                    # ret.extend([x for x in range(start, idx)])
                    # for i in range(start, idx): 
                    #     bitmap[i] = 1 
                    # idx += N
                # if idx == nidx: 
                #     idx += 1
                # else: 
                #     idx = nidx
                
                # print(idx, nidx)
            # return set(ret) 
        
        match(hs, hbm)
        match(vs, vbm)
        # print(hbm)
        # print(vbm)
        ret = 0
        # for i in range(nr * nc): 
        i = 0 
        while i < nr * nc: 
            tmp = hbm[i:].index(1) if 1 in hbm[i:] else -1 
            if tmp < 0: 
                break 
            ni = tmp + i
            # if hbm[ni] == 1: 
            r, c = hidx_fn(ni)
            vidx = nr * c + r 
            # print(r, c, vidx, vbm[vidx])
            ret += vbm[vidx]
            i = ni + 1

        return ret

if __name__ == "__main__": 
    # responses = [["good","ok","good","ok"],["ok","bad","good","ok","ok"],["good"],["bad"]]
    # # responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
    # ret = Solution().findCommonResponse(responses)
    # print(ret)

    # conversions = [[0,1,2],[1,2,3]]
    # conversions = [[0,1,2],[0,2,3],[1,3,4],[1,4,5],[2,5,2],[4,6,3],[5,7,4]]
    # ret = Solution().baseUnitConversions(conversions)
    # print(ret)
    
    grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","c","c"]]
    pattern = "abaca"
    # grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]]
    # pattern = "aba"

    # grid = [["x","e"],["e","t"],["e","c"],["y","e"],["n","c"]]
    # pattern = "e"

    # grid = [["h","h","y"],["y","y","n"],["s","y","y"],["y","y","n"],["n","n","x"],["i","l","x"]]
    # pattern = "yn"

    test_case = (grid, pattern)
    ret = Solution().countCells1(*test_case)
    print(ret)
