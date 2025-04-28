from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        s, c = 0, 0 
        start = 0
        ret = 0
        for end in range(len(nums)): 
            s += nums[end]
            c += 1 
            while s * c >= k: 
                s -= nums[start] 
                c -= 1 
                start += 1
            ret += (end - start + 1)
        return ret
    
if __name__ == "__main__": 
    nums = [2,1,4,3,5]
    k = 10
    nums = [1,1,1]
    k = 5
    test_case = (nums, k)
    ret = Solution().countSubarrays(*test_case)
    print(ret)