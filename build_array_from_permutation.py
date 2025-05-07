from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        idx = 0 
        arr = [0] * len(nums)
        for idx in range(len(nums)): 
            arr[idx] = nums[nums[idx]]
        return arr
    
if __name__ == "__main__": 
    Solution().buildArray