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

    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        
        # (num_0.. num_r + k * i) * (cost_l + ... + cost_r)
        pivot = set()
        depth = 0
        
        def find_cost(l, r, idx): 
            nonlocal depth
            depth += 1
            if l == r: 
                depth -= 1
                return (sum(nums[: r + 1]) + k * idx) * cost[l], idx + 1
            
            min_c = (sum(nums[: r + 1]) + k * idx) * (sum(cost[l: r + 1]))
            tmp = -1
            new_idx = idx + 1
            for p in range(l, r): 
                # lc, lidx = find_cost(l, p, idx)
                lc = (sum(nums[: p + 1]) + k * idx) * (sum(cost[l: p + 1])) 
                lidx = idx + 1
                rc, ridx = find_cost(p + 1, r, lidx)
                if min_c > lc + rc: 
                    new_idx = ridx
                    tmp = p 
                min_c = min(lc + rc, min_c)

            # if depth == 2: 
            #     import pdb 
            #     pdb.set_trace()
            #     print(tmp)  
            # nonlocal pivot
            # pivot |= {tmp}
            # depth -= 1
            return min_c, new_idx
        
        
        ret = find_cost(0, len(nums) - 1, 1)[0]
        # print(pivot)
        return ret

if __name__ == "__main__": 
    # s = "01"
    # s = "0100"
    # s = "1000100"
    # s = "01010"
    # s = "0111"
    # s = "10110"
    # test_case = (s, )
    # ret = Solution().maxActiveSectionsAfterTrade(*test_case)
    
    nums = [3,1,4]
    cost = [4,6,6]
    k = 1
    nums = [4,8,5,1,14,2,2,12,1]
    cost = [7,2,8,4,2,2,1,1,2]
    k = 7
    test_case = (nums, cost, k)
    ret = Solution().minimumCost(*test_case)
    print(ret)