from typing import List

class Solution:
    def minimumCost2_1(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        S = set(original + changed)
        M = len(S)
        mp = {}
        for i, s in enumerate(S): 
            mp[s] = i 

        G = [[float("inf")] * M for _ in range(M)]
        for ori, ch, ct in zip(original, changed, cost): 
            G[mp[ori]][mp[ch]] = min(G[mp[ori]][mp[ch]], ct)
        for i in range(M): 
            G[i][i] = 0 
        
        for p in range(M): 
            for src in range(M): 
                if G[src][p] == float("inf"): continue # the most important part to avoid TLD ==
                for tgt in range(M): 
                    G[src][tgt] = min(G[src][tgt], G[src][p] + G[p][tgt])

        N = len(source)
        # tries = {}
        def make_tries(lst):
            tries = {}
            for idx, s in enumerate(lst): 
                cur = tries
                for i in range(len(s) - 1, -1, -1): 
                    if s[i] not in cur:
                        cur[s[i]] = {} 
                    cur = cur[s[i]]
                # if None not in cur: 
                #     cur[None] = []
                # cur[None].append((mp[s], len(s)))
                # if None not in cur: 
                #     l = set()
                # else: 
                #     l = cur[None][-1]
                cur[None] = mp[s] #(mp[s], len(s), ) #l | {idx})
            return tries
        
        otr = make_tries(original)
        ctr = make_tries(changed)
        # print(otr)
        # print(ctr)

        dp = [float("inf")] * (N + 1)
        dp[0] = 0 
        for i in range(1, N + 1): 
            c, _c = source[i - 1], target[i - 1]
            if c == _c: 
                dp[i] = dp[i - 1]
            ox, cx = otr, ctr 
            l = 0
            j = i - 1
            while j >= 0: 
                c, _c = source[j], target[j]
                if c in ox and _c in cx: 
                    ox, cx = ox[c], cx[_c]
                    l += 1 
                    if None in ox and None in cx: 
                        ogidx, cgidx = ox[None], cx[None]
                        dp[i] = min(dp[i], G[ogidx][cgidx] + dp[i - l]) 
                else: 
                    break 
                j -= 1 
        # print(dp)
        return dp[-1] if dp[-1] < float("inf") else -1
    
    def minimumCost2(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        S = set(original + changed)
        M = len(S)
        mp = {}
        for i, s in enumerate(S): 
            mp[s] = i 

        G = [[float("inf")] * M for _ in range(M)]
        for ori, ch, ct in zip(original, changed, cost): 
            G[mp[ori]][mp[ch]] = min(G[mp[ori]][mp[ch]], ct)
        for i in range(M): 
            G[i][i] = 0 
        
        for p in range(M): 
            for src in range(M): 
                for tgt in range(M): 
                    G[src][tgt] = min(G[src][tgt], G[src][p] + G[p][tgt])

        N = len(source)
        # tries = {}
        def make_tries(lst):
            tries = {}
            for idx, s in enumerate(lst): 
                cur = tries
                for i in range(len(s)): 
                    if s[i] not in cur:
                        cur[s[i]] = {} 
                    cur = cur[s[i]]
                # if None not in cur: 
                #     cur[None] = []
                # cur[None].append((mp[s], len(s)))
                # if None not in cur: 
                #     l = set()
                # else: 
                #     l = cur[None][-1]
                cur[None] = (mp[s], len(s), ) #l | {idx})
            return tries
        
        otr = make_tries(original)
        ctr = make_tries(changed)
        # print(otr)
        # print(ctr)

        dp = [float("inf")] * (N + 1)
        dp[0] = 0 
        cur = [(otr, ctr)]
        for i in range(1, N + 1): 
            _cur = [(otr, ctr)]
            c, _c = source[i - 1], target[i - 1]
            mp = True
            if c == _c: 
                dp[i] = dp[i - 1]
                mp = True
            for ox, cx in cur:
                if c in ox and _c in cx: 
                    ox, cx = ox[c], cx[_c]
                    _cur.append((ox, cx))
                    if None in ox and None in cx: 
                        ogidx, ol,  = ox[None]
                        cgidx, cl,  = cx[None]
                        if True:
                            # tgt = target[i - l: i]
                            # print(tgt)
                            # if tgt in mp: 
                                # import pdb 
                                # pdb.set_trace()
                            dp[i] = min(dp[i], G[ogidx][cgidx] + dp[i - ol])
                            mp = True
            if not mp: 
                return -1
            cur = _cur 

        # print(dp)
        return dp[-1] if dp[-1] < float("inf") else -1

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        chrs = set()
        for c in source + target: 
            chrs.add(c)
        for c in original + changed: 
            chrs.add(c)

        mp = {}
        idx = 0 
        for c in sorted(chrs): 
            mp[c] = idx 
            idx += 1 

        N = len(chrs)
        get_idx = lambda c: mp[c] #ord(c) - ord('a')
        _G = [[float("inf")] * N for _ in range(N)]
        # G = [[float("inf")] * N for _ in range(N)]
        for ori, ch, ct in zip(original, changed, cost): 
            # if ori not in mp or ch not in mp: 
            #     continue 
            oi, ci = get_idx(ori), get_idx(ch)
            _G[oi][ci] = min(_G[oi][ci], ct)
        for i in range(N): 
            _G[i][i] = 0
        # print(_G)
        for p in range(N): 
            for src in range(N): 
                for tgt in range(N): 
                    # if _G[src][p] != float("inf") and  _G[p][tgt] != float("inf"):
                    _G[src][tgt] = min(_G[src][p] + _G[p][tgt], _G[src][tgt])
            # tmp = G
            # G = _G 
            # _G = tmp 

        ret = 0
        # print(G)
        for src, tgt in zip(source, target): 
            si, ti = get_idx(src), get_idx(tgt)
            if _G[si][ti] == float("inf"): 
                # import pdb 
                # pdb.set_trace()
                return -1  
            ret += _G[si][ti]
        return ret 
    
    

if __name__ == "__main__": 
    source = "abcd"
    target = "acbe"
    original = ["a","b","c","c","e","d"]
    changed = ["b","c","b","e","b","e"]
    cost = [2,5,5,1,2,20]

    source = "abcdefgh"
    target = "acdeeghh"
    original = ["bcd","fgh","thh"]
    changed = ["cde","thh","ghh"]
    cost = [1,3,5]

    source = "abcdefgh"
    target = "addddddd"
    original = ["bcd","defgh"]
    changed = ["ddd","ddddd"]
    cost = [100,1578]
    ret = Solution().minimumCost2_1(source, target, original, changed, cost)
    print(ret)