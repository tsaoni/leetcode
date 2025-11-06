from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        ret = 0
        while l < r: 
            ret = max(min(height[l], height[r]) * (r - l), ret)
            if height[l] > height[r]: 
                r -= 1 
            else: 
                l += 1 
        
        return ret
    
if __name__ == "__main__": 
    height = [1,8,6,2,5,4,8,3,7]
    height = [1,1]
    ret = Solution().maxArea(height)
    print(ret)