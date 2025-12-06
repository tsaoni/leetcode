from typing import List

class Solution:
    def maxSubarraySum_err(self, nums: List[int], k: int) -> int:
        """
        misunderstand the problem..
        """
        dp = [None] * k
        for n in nums: 
            _dp = [None] * k
            for i in range(k): 
                if i == 0 and dp[i] is None: 
                    x = 0 
                else: 
                    x = dp[i]
                if x is not None: 
                    idx = (i + n) % k 
                    if i == 0: 
                        _dp[idx] = max(_dp[idx], x + n, n) if _dp[idx] is not None else max(x + n, n) 
                    else:
                        _dp[idx] = max(_dp[idx], x + n) if _dp[idx] is not None else x + n 
            dp = _dp 
        return dp[0]
    
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        """
        TLE
        """
        dp = [None] * k
        ret = -float("inf")
        for n in nums: 
            _dp = [None] * k
            for i in range(k): 
                if i == 0 and dp[i] is None: 
                    x = 0 
                else: 
                    x = dp[i]
                if x is not None: 
                    idx = (i + 1) % k 
                    if i == 0: 
                        _dp[idx] = max(_dp[idx], x + n, n) if _dp[idx] is not None else max(x + n, n) 
                    else:
                        _dp[idx] = max(_dp[idx], x + n) if _dp[idx] is not None else x + n 
                    if idx == 0: 
                        ret = max(ret, _dp[idx])
            dp = _dp 
        return ret
    
    def maxSubarraySum_1(self, nums: List[int], k: int) -> int:
        minK = [0] + [float("inf")] * (k - 1)
        last_idx = [-1] * k
        # acc = [0] * (k + 1)
        # ret = -float("inf")
        pre = 0
        N = len(nums)
        ret = -float("inf")
        for i in range(N): 
            idx = i % k
            # acc[idx + 1] = acc[idx] + nums[i]
            # if i >= k: 
            #     pre += (nums[i] - nums[i - k])
            pre += nums[i]
            if minK[(idx + 1) % k] < float("inf"):
                ret = max(ret, pre - minK[(idx + 1) % k])
            if pre <  minK[(idx + 1) % k]: 
                minK[(idx + 1) % k] = pre 
                last_idx[(idx + 1) % k] = i 
            # else: 
            #     minK[(idx + 1) % k] = minK[(idx + 1) % k]
            # minK[(idx + 1) % k] = min(acc[idx + 1], pre + minK[(idx + 1) % k])
            # if i == k - 1: 
            #     pre = acc[-1]
            # print(pre, minK, last_idx)
        # minK[0] = min(minK[0], 0)
        # ret = minK[0]
        # acc = 0
        # for i in range(N): 
        #     acc += nums[i]
        #     idx = (i + 1) % k 

            # if k == 1: 
            #     ret = max(ret, nums[i])
            # if idx == 0: 
            #     ret = max(ret, acc)
            # if i > last_idx[idx]:
            #     ret = max(ret, acc - minK[idx])
            # elif i < last_idx[idx]:
            #     ret = max(ret, minK[idx] - acc)
        # print(minK)
        return ret
    
if __name__ == "__main__": 
    nums = [1,2]
    k = 1
    nums = [-1,-2,-3,-4,-5]
    k = 4
    nums = [-5,1,2,-3,4]
    k = 2
    # nums = [-19,-8,-16]
    # k = 1
    nums = [-6,-25,3,-33,-37]
    k = 2
    ret = Solution().maxSubarraySum_1(nums, k)
    print(ret)