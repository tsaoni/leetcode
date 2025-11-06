from typing import List

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ret = 0
        l, r = 0, 0
        N = len(nums)
        k = -1
        while r < N: 
            if k < 0:
                while r + 1 < N and nums[r] < nums[r + 1]: 
                    r += 1 
                _k = r - l + 1
            else: 
                _k = k
            l = r + 1 
            r = l
            while r + 1 < N and nums[r] < nums[r + 1]: 
                r += 1 
            k = r - l + 1 
            ret = max(ret, min(k, _k), k // 2, _k // 2)
            # print(_k, k)

        return ret 
    
if __name__ == "__main__": 
    nums = [2,5,7,8,9,2,3,4,3,1]
    # nums = [1,2,3,4,4,4,4,5,6,7]
    ret = Solution().maxIncreasingSubarrays(nums)
    print(ret)