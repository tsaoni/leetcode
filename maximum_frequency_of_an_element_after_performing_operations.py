from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter
        maxv, minv = max(nums) + k, min(nums) - k 
        psum = [0] * (maxv - minv + 1)
        f = Counter()
        for n in nums: 
            _n = n - minv
            f[_n] += 1
            s, e = min(_n + k, maxv - minv), max(_n - k, 0)
            psum[s] += 1 
            if e > 0:
                psum[e - 1] -= 1 
        ret = psum[-1]
        for i in range(maxv - minv - 1, -1, -1): 
            psum[i] += psum[i + 1]
            tmp = numOperations if i not in f else f[i] + numOperations
            ret = max(ret, min(psum[i], tmp))
        # print(psum)
        return ret
    
    def maxFrequency_1(self, nums: List[int], k: int, numOperations: int) -> int:
        from collections import Counter 
      
        nums = sorted(nums)
        N = len(nums)
        s, e = 0, 0 
        i = -1
        ret = 1 
        # minv, maxv = nums[0], nums[-1]
        # print(maxv - minv)
        ref = set(nums + [x - k for x in nums[1:]] + [x + k for x in nums[: -1]])
        ref = sorted(ref)
        for x in ref: #range(minv, maxv + 1): 
            c = 0
            while i < N - 1 and nums[i + 1] == x: 
                i += 1 
                c += 1
            n = x # nums[i]
            while nums[s] < n - k: 
                s += 1 

            e = max(i, e)
            while e < N - 1 and nums[e + 1] <= n + k: 
                e += 1 
           
            ex = min(numOperations, e - s + 1 - c)
            ret = max(ret, c + ex)
            # print(x, s, e, c)
            # if i < N:
            #     i += 1
        
        return ret

if __name__ == "__main__": 
    nums = [1,4,5]
    k = 1
    numOperations = 2
    nums = [5,11,20,20]
    k = 5
    numOperations = 1
    nums = [88,53]
    k = 27
    numOperations = 2
    nums = [999999997,999999999,999999999]
    k = 999999999
    numOperations = 2
    ret = Solution().maxFrequency_1(nums, k, numOperations)
    print(ret)