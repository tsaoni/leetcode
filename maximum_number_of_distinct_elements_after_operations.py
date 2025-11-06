from typing import List

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        ret = 0
        cur = nums[0] - k
        for n in nums: 
            if n - k > cur: 
                cur = n - k 
            if cur <= n + k: 
                ret += 1 
                cur += 1 
                    
                
        return ret
    
if __name__ == "__main__": 
    nums = [1,2,2,3,3,4]
    k = 2
    nums = [4,4,4,4]
    k = 1
    ret = Solution().maxDistinctElements(nums, k)
    print(ret)