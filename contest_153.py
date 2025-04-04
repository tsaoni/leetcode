import string
from typing import List

class Solution: 
    def func(): 
        return 
    
    def reverseDegree(self, s: str) -> int:
        chs = string.ascii_lowercase
        ret = 0
        for i, c in enumerate(s): 
            cidx = chs.index(c)
            cidx = 26 - cidx
            ret += (i + 1) * cidx
        return ret

    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        zcnt = [0, 0]
        max_inc = 0
        n_act = 0
        lock = False
        nact_c = 0
        s = "1" + s + "1"
        N = len(s)
        # print(s)
        for i in range(N): 
            c = s[i]
            if c == '0': 
                lock = True
                zcnt[1] += 1 
            else: # 1
                if lock: 
                    nact_c += 1
                    # print("nactc", nact_c)
                    
                if lock and nact_c > 1: #zcnt[0] > 0: 
                    max_inc = max(max_inc, sum(zcnt))
                    # print(zcnt)
                
                    
                if lock: 
                    zcnt[0] = zcnt[1]
                    zcnt[1] = 0
                    lock = False

                n_act += 1

        if nact_c > 1: #zcnt[0] > 0 and zcnt[1] > 0: 
            max_inc = max(max_inc, sum(zcnt))
        # print(nact_c)
        # print(zcnt)
        return n_act + max_inc - 2

    def minimumCost2(self, A: List[int], C: List[int], K: int) -> int:
        from itertools import accumulate
        from functools import cache
        from math import inf
        PA = list(accumulate(A, initial=0))
        PC = list(accumulate(C, initial=0))
        N = len(A)
        pivot = []
        a = []

        @cache
        def dp(i):
            nonlocal pivot, a
            if i == N:
                return 0

            ans = inf
            p = None
            for j in range(i, N):
                cand = PA[j + 1] * (PC[j + 1] - PC[i])
                cand += K * (PC[-1] - PC[i])
                cand += dp(j + 1)
                ans = min(ans, cand)
                if ans == cand: 
                    p = j + 1
            # pivot.insert(0, p)
            # a.insert(0, ans)
            return ans

        
        ret = dp(0)
        # print(pivot, a) 
        return ret

    def minimumCost1(self, nums: List[int], cost: List[int], k: int) -> int:
        """
        a wrong greedy approach
        """

        pivots = {}
        N = len(nums)
        root = -1
        while True: 
            dec = float("-inf")
            pidx = -1
            pnidx = -1
            ppidx = -1
            for nidx in range(1, N): 
                if nidx in pivots: 
                    pidx = nidx
                else: # if the pivot is set
                    if pidx >= 0: 
                        lb = pidx 
                        rb = pivots[pidx] - 1 if pivots[pidx] >= 0 else N - 1
                    else: 
                        lb = 0
                        rb = root - 1 if root >= 0 else N - 1
    
                    print(nums[nidx: rb + 1], cost[lb: nidx])
                    # import pdb 
                    # pdb.set_trace()
                    tmp = sum(nums[nidx: rb + 1]) * sum(cost[lb: nidx])
                    tmp -= k * sum(cost[nidx: N])
                    print("tmp", tmp)
                    if tmp >= dec: 
                        dec = tmp 
                        pnidx = nidx
                        ppidx = pidx
            if dec < 0: 
                break      
            
            if ppidx >= 0: 
                print(ppidx, pnidx, pivots[ppidx])
                pivots[pnidx] = pivots[ppidx]
                pivots[ppidx] = pnidx
            else: 
                print(pnidx, root)
                pivots[pnidx] = root
                root = pnidx #if root < 0 else min(root, pnidx)
            # import pdb 
            # pdb.set_trace()
        print(pivots)
        pivots = {5: 8, 8: 9, 4: 8, 9: -1}
        root = 4

        prev, end = 0, root - 1 if root >= 0 else N - 1
        idx = 1
        ret = 0
        while True: 
            # if idx > 1 and pivots[prev] == -1: 
            #     break 
            # else: 
            print(prev, end)
            print(nums[: end + 1], cost[prev: end + 1])
            # print(idx)
            ret += (sum(nums[: end + 1]) + k * idx) * (sum(cost[prev: end + 1]))
            # print(ret)
            if end == N - 1: 
                break
            prev = end + 1
            end = pivots[end + 1] - 1 if pivots[end + 1] >= 0 else N - 1
            idx += 1
        return ret

    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        """
        results in TLE :'(
        """
        from itertools import accumulate
        from functools import cache
        # (num_0.. num_r + k * i) * (cost_l + ... + cost_r)
        # pivot = set()
        # depth = 0
        acc_n = list(accumulate(nums, initial=0))
        acc_c = list(accumulate(cost, initial=0))
        N = len(nums) 
        
        @cache
        def find_cost(l, idx): 
            # nonlocal depth, pivot
            # depth += 1
            if l == N - 1: 
                # depth -= 1
                # return (sum(nums[: r + 1]) + k * idx) * cost[l], idx + 1
                return (acc_n[N] + k * idx) * cost[l] #, idx + 1
            
            # min_c = (sum(nums[: r + 1]) + k * idx) * (sum(cost[l: r + 1]))
            min_c = (acc_n[N] + k * idx) * (acc_c[N] - acc_c[l])
            # tmp = -1
            # new_idx = idx + 1
            for p in range(l, N - 1): 
                # lc, lidx = find_cost(l, p, idx)
                # lc = (sum(nums[: p + 1]) + k * idx) * (sum(cost[l: p + 1])) 
                lc = (acc_n[p + 1] + k * idx) * (acc_c[p + 1] - acc_c[l]) 
                lidx = idx + 1
                rc = find_cost(p + 1, lidx)
                # if min_c > lc + rc: 
                #     new_idx = ridx
                #     tmp = p 
                min_c = min(lc + rc, min_c)

            # if depth == 2: 
            #     print(depth)
            #     print(min_c)
            #     import pdb 
            #     pdb.set_trace()
            #     print(tmp)  
            # nonlocal pivot
            # pivot |= {tmp}
            # depth -= 1
            # if new_idx == 5: 
            #     print(pivot, min_c, l, r)
            return min_c #, new_idx
        
        
        ret = find_cost(0, 1)
        # print(pivot)
        return ret

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        
        return 

if __name__ == "__main__": 
    # s = "01"
    # s = "0100"
    # s = "1000100"
    # s = "01010"
    # s = "0111"
    # s = "10110"
    # test_case = (s, )
    # ret = Solution().maxActiveSectionsAfterTrade(*test_case)
    
    # nums = [3,1,4]
    # cost = [4,6,6]
    # k = 1
    # nums = [4,8,5,1,14,2,2,12,1]
    # cost = [7,2,8,4,2,2,1,1,2]
    # k = 7
    # nums = [5,14,42,38,48,32,26,9,35,21] 
    # cost = [8,18,5,43,28,8,29,34,17,13]
    # k = 20
    # test_case = (nums, cost, k)
    # ret = Solution().minimumCost2(*test_case)
    

    ret = Solution().maxActiveSectionsAfterTrade()
    print(ret)