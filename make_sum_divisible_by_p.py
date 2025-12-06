from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        mp = {0: -1}
        N = len(nums)
        target = 0
        for i in range(N): 
            target = (target + nums[i]) % p 
        # print(target)
        if target == 0: 
            return 0 
        else: 
            cur = 0
            minl = N
            for i in range(N): 
                cur = (cur + nums[i]) % p 
                rem = (cur - target + p) % p
                if rem in mp: 
                    minl = min(minl, i - mp[rem])
                mp[cur] = i
                # print(mp)
               
            return -1 if minl == N else minl
    
if __name__ == "__main__": 
    nums = [3,1,4,2]
    p = 6
    nums = [6,3,5,2]
    p = 9
    nums = [1,2,3]
    p = 3
    ret = Solution().minSubarray(nums, p)
    print(ret)