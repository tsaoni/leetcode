from typing import List
import functools
import time

class Solution: 
    def func(): 
        return 
    

    def maxSum(self, nums: List[int]) -> int:
        arr = []
        for num in nums: 
            if num > 0 and num not in arr: 
                arr += [num]
        if len(arr) == 0: 
            arr += [max(nums)]
        return sum(arr)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dist = [-1] * len(nums) #{}
        idx_dict = {}
        for i in range(2 * len(nums)): 
            # print(i)
            idx = i % len(nums)
            tmp = nums[idx]
            if tmp not in idx_dict: 
                idx_dict[tmp] = (None, i)
            else: 
                if idx_dict[tmp][0] == None: 
                    dist[idx] = i - idx_dict[tmp][1]
                    idx_dict[tmp] = (idx_dict[tmp][1], i)
                    
                else:
                    if dist[idx] == -1:
                        dist[idx] = i - idx_dict[tmp][1] #min(i - idx_dict[tmp][1], idx_dict[tmp][1] - idx_dict[tmp][0])
                    else: 
                        dist[idx] = min(i - idx_dict[tmp][1], dist[idx])
                    dist[idx_dict[tmp][1] % len(nums)] = min(
                        i - idx_dict[tmp][1], idx_dict[tmp][1] - idx_dict[tmp][0])
                    idx_dict[tmp] = (idx_dict[tmp][1], i)
            # print(dist)
        
                # if dist[tmp][1] == None: 
                #     dist[tmp] = (dist[tmp][0], idx)
                # else: 
                #     if i - dist[tmp][1] < dist[tmp][1] - dist[tmp][0]: 
                #         dist[tmp] = (dist[tmp][1], i)

            # if tmp not in dist: 
            #     dist[tmp] = (idx, None) 
            # else: 
            #     if dist[tmp][1] == None: 
            #         dist[tmp] = (dist[tmp][0], idx)
            #     else: 
            #         if i - dist[tmp][1] < dist[tmp][1] - dist[tmp][0]: 
            #             dist[tmp] = (dist[tmp][1], i)

        # for i in range(len(nums)): 
        #     tmp = nums[i]
        #     if tmp in idx_dict:
        #         idx_dict[tmp] += [i]
        #     else: 
        #         idx_dict[tmp] = [i]

        # print(dist)
        # print(idx_dict)
        # print(nums)
        # print(queries)
        # return
        ret = []
        for q in queries: 
            if dist[q] == len(nums): 
                ret += [-1] 
            else: ret += [dist[q]]
            # num = nums[q]
            # idxs = idx_dict[num]
            # if len(idxs) == 1: 
            #     ret += [-1]
            # else: 
            #     idx = idxs.index(q)
            #     prev = (idx - 1 + len(idxs)) % len(idxs)
            #     next = (idx + 1) % len(idxs)
            #     dist_fn = lambda p, n: n - p if n - p >= 0 else (n - p + len(nums))
            #     tmp = min(dist_fn(idxs[prev], idxs[idx]), dist_fn(idxs[idx], idxs[next]))
            #     ret += [tmp]
                # import pdb 
                # pdb.set_trace()
            
            # d = dist[num][1] - dist[num][0]
            # if d == 0: 
            #     ret += [-1] 
            # else: ret += [d]
        return ret

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0: 
            return 0
        cnt = [False] * len(nums)
        vals = []
        for i, x in enumerate(nums): 
            if x == 0: 
                cnt[i] = True
            vals += [{x}]
        k = 0
        for l, r, val in queries: 
            for i in range(l, r + 1): 
                if not cnt[i]:
                    s = set()
                    for v in vals[i]: 
                        if v == val: 
                            cnt[i] = True 
                        elif v > val: 
                            s |= {v - val}
                    vals[i] |= s
            k += 1
            if sum(cnt) == len(nums): 
                return k
        return -1

    def beautifulNumbers2(self, l: int, r: int) -> int:
        start_time = time.time()
        def get_digits(num): 
            d = []
            while num > 0: 
                d = [num % 10] + d
                num = num // 10 
            
            return [0] * (9 - len(d)) + d
        dl = get_digits(l - 1)
        dr = get_digits(r)
        # print(dl, dr)
        
        @functools.lru_cache(None)
        def count(cnt, leadzero, num, mult, sumt, tight): 
            ub = get_digits(num)
            if cnt == 9:    
                # print(cur)
                if leadzero: 
                    return 0
                return 0 if mult % sumt > 0 else 1
            ret = 0
            if tight: #(len(cur) == 0 and cnt > 0 and ub[cnt - 1] > 0 or len(cur) > 0 and cur[-1] < ub[cnt - 1]): 
                maxd = ub[cnt] + 1
            else: maxd = 10
            for i in range(0, maxd): 
                n_mult = 1
                # a = False
                if i == 0 and not leadzero and not tight: 
                    # a = True
                    ret += 10 ** (8 - cnt)
                    continue
                # if i == 0 and leadzero: # leading zero check
                #     pass
                # else: 
                #     cur += [i]
                
                if i == 0 and leadzero: 
                    n_mult = mult
                else: 
                    n_mult = mult * i
                n_sumt = sumt + i
                n_leadzero = leadzero and (i == 0)
                n_tight = tight and (i == maxd - 1)
                ret += count(cnt + 1, n_leadzero, num, n_mult, n_sumt, n_tight)
                # if a: 
                #     if ret != 10 ** (8 - cnt): 
                #         import pdb 
                #         pdb.set_trace()
                #         print(10 ** (8 - cnt))
                #         print(ret)
                #         print()
            return ret

        rr = count(0, True, r, 1, 0, True) 
        # print()
        lr = count(0, True, l - 1, 1, 0, True)
        # print(rr, lr)
        # print("time: ", time.time() - start_time)
        return rr - lr

    def beautifulNumbers1(self, l: int, r: int) -> int:
        start_time = time.time()
        @functools.lru_cache(None)
        def dp(
            s: str,
            i: int,
            tight: bool,
            isLeadingZero: bool,
            hasZero: bool,
            sum: int,
            prod: int,
        ) -> int:
            if i == len(s):
                if isLeadingZero:
                    return 0
                return 1 if hasZero or prod % sum == 0 else 0
            if not isLeadingZero and hasZero and not tight:
                return 10 ** (len(s) - i)

            res = 0
            maxDigit = int(s[i]) if tight else 9

            for d in range(maxDigit + 1):
                nextTight = tight and (d == maxDigit)
                nextIsLeadingZero = isLeadingZero and d == 0
                nextHasZero = not nextIsLeadingZero and d == 0
                nextProd = 1 if nextIsLeadingZero else prod * d
                res += dp(s, i + 1, nextTight, nextIsLeadingZero,
                        nextHasZero, sum + d, nextProd)

            return res

        ret = (dp(str(r), 0, tight=True, isLeadingZero=True, hasZero=False, sum=0, prod=1) -
                dp(str(l - 1), 0, tight=True, isLeadingZero=True, hasZero=False, sum=0, prod=1))
        
        print("time: ", time.time() - start_time)
        return ret

    def beautifulNumbers(self, l: int, r: int) -> int:
        start_time = time.time()
        def get_digits(num): 
            d = []
            while num > 0: 
                d = [num % 10] + d
                num = num // 10 
            
            return [0] * (9 - len(d)) + d
        dl = get_digits(l - 1)
        dr = get_digits(r)
        # print(dl, dr)
        
        # @functools.lru_cache(None)
        def count(cnt, cur, ub, mult, sumt, tight): 
            if cnt == 9:    
                # print(cur)
                if len(cur) == 0: 
                    return 0
                return 0 if mult % sumt > 0 else 1
            ret = 0
            if tight: #(len(cur) == 0 and cnt > 0 and ub[cnt - 1] > 0 or len(cur) > 0 and cur[-1] < ub[cnt - 1]): 
                maxd = ub[cnt] + 1
            else: maxd = 10
            for i in range(0, maxd): 
                n_mult = 1
                # a = False
                if i == 0 and len(cur) > 0 and not tight: 
                    # a = True
                    ret += 10 ** (8 - cnt)
                    continue
                if i == 0 and len(cur) == 0: # leading zero check
                    pass
                    # tmp = cur + []
                else: 
                    cur += [i]
                    # tmp = cur + [i]
                
                if i == 0 and len(cur) == 0: 
                    n_mult = mult
                else: 
                    n_mult = mult * i
                n_sumt = sumt + i
                n_tight = tight and (i == maxd - 1)
                ret += count(cnt + 1, cur, ub, n_mult, n_sumt, n_tight)
                if not(i == 0 and len(cur) == 0):
                    cur.pop(-1)
                # if a: 
                #     if ret != 10 ** (8 - cnt): 
                #         import pdb 
                #         pdb.set_trace()
                #         print(10 ** (8 - cnt))
                #         print(ret)
                #         print()
            return ret

        rr = count(0, [], dr, 1, 0, True) 
        # print()
        lr = count(0, [], dl, 1, 0, True)
        # print(rr, lr)
        print("time: ", time.time() - start_time)
        return rr - lr


if __name__ == "__main__": 
    
    # nums = [1,3,1,4,1,3,2]
    # queries = [0,3,5]
    # nums = [1,2,3,4]
    # queries = [0,1,2,3]
    # nums = [14,14,4,2,19,19,14,19,14]
    # queries = [2,4,8,6,3]
    # test_case = (nums, queries)
    # ret = Solution().solveQueries(*test_case)
    # print(ret)

    # nums = [2,0,2]
    # queries = [[0,2,1],[0,2,1],[1,1,3]]
    # test_case = (nums, queries)
    # ret = Solution().minZeroArray(*test_case)
    # print(ret)


    l = 10
    r = 20
    # l = 1
    # r = 15
    # l = 776 
    # r = 776
    # l = 629 
    # r = 708
    # l = 5940 
    # r = 79658243

    test_case = (l, r)

    ret = Solution().beautifulNumbers2(*test_case)
    print(ret)