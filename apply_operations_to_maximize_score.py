from typing import List
import math
import numpy as np
import functools

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        @functools.lru_cache()
        def prime_score(num): 
            ret = 0
            remain = num
            if num == 1: 
                return 0
            for i in range(2, math.floor(math.sqrt(num) + 1)): 
                add = 0
                while remain % i == 0: 
                    remain //= i 
                    add = 1 
                ret += add  
            if remain > 1: 
                ret += 1
            return ret if ret > 0 else 1
        
        @functools.lru_cache()
        def fast_exp(x, n, mod): 
            remain = n
            base = x
            res = 1
            while remain > 0: 
                if remain % 2 > 0: 
                    res *= base 
                    res = res % mod
                base = base * base % mod
                remain //= 2
            return res
        
        N = len(nums)
        scores = [prime_score(num) for num in nums]
        # scores = [3, 1, 4, 4, 3, 5]
        # print(scores)
        
        left, right = [0] * N, [N - 1] * N
        """old implementation"""
        # idx = 0
        # for i in range(1, N): 
        #     if scores[i] <= scores[i - 1]: 
        #         idx = i 
        #         tmp = idx
        #     else: 
        #         tmp = idx
        #         while tmp > 0: 
        #             if scores[tmp - 1] < scores[i]: 
        #                 tmp = left[tmp - 1]
        #             else: 
        #                 break
        #     left[i] = tmp

        # for i in range(N - 2, -1, -1): 
        #     if scores[i] < scores[i + 1]: 
        #         idx = i 
        #         tmp = idx
        #     else: 
        #         tmp = idx
        #         while tmp < N - 1: 
        #             if scores[tmp + 1] <= scores[i]: 
        #                 tmp = right[tmp + 1]
        #             else: 
        #                 break
        #     right[i] = tmp

        """use monotonic stack"""
        dec_stack = []
        for i in range(N): 
            while len(dec_stack) > 0: 
                idx = dec_stack[-1]
                if scores[idx] < scores[i]: 
                    pidx = dec_stack.pop(-1)
                    right[pidx] = i - 1
                else: 
                    break 
            left[i] = dec_stack[-1] + 1 if len(dec_stack) > 0 else 0
            dec_stack.append(i)

        ret = 1
        n_idxs = np.argsort(-np.array(nums))
        # nums.sort(key=lambda x: -x)
        remain = k 
        nidx = 0
        # print(scores)
        # print(nums)
        # print(left, right)
        mod = 10 ** 9 + 7
        while remain > 0 and nidx < N: 
            idx = n_idxs[nidx]
            r = (idx - left[idx] + 1) * (right[idx] - idx + 1)
            ret *= fast_exp(nums[idx], min(remain, r), mod)
            ret = ret % mod
            # ret *= (nums[idx] ** min(remain, r))
            remain -= r
            nidx += 1
        return ret #% (10 ** 9 + 7)
    
if __name__ == "__main__": 
    nums = [8,3,9,3,8]
    k = 2
    nums = [19,12,14,6,10,18]
    k = 3
    nums = [1,7,11,1,5] 
    k = 14
    test_case = (nums, k)
    ret = Solution().maximumScore(*test_case)
    print(ret)