from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        N = len(nums)
        def find(r): 
            cnt = 0
            i = 0
            while i < N - 1: 
                if nums[i + 1] - nums[i] <= r: 
                    cnt += 1
                    i += 2 
                else: 
                    i += 1 
            return cnt
        
        l, r = 0, nums[-1] - nums[0]
        while l < r: 
            mid = (l + r) // 2 
            if find(mid) < p: 
                l = mid + 1
            else: 
                r = mid
        return l
    
if __name__ == "__main__": 
    nums = [10,1,2,7,1,3]
    p = 2
    nums = [4,2,1,2]
    p = 1
    ret = Solution().minimizeMax(nums, p)
    print(ret)