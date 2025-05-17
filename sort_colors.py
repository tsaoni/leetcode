from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        p0, p1, p2 = 0, -1, N - 1
        
        def swap(p1, p2): 
            nums[p1] ^= nums[p2]
            nums[p2] ^= nums[p1]
            nums[p1] ^= nums[p2]
        
    
        p1 = -1 
        while p1 < p2: 
            while p0 < p2: 
                if nums[p0] == 2 or nums[p2] == 0: 
                    swap(p0, p2)
                if nums[p0] == 0: 
                    p0 += 1 
                if nums[p2] == 2: 
                    p2 -= 1 
                if nums[p0] == 1 and nums[p2] == 1: 
                    break 
                
            if p0 < p2: 
                p1 = p0 if p1 < p0 else p1
                while nums[p1] == 1 and p1 < p2: 
                    p1 += 1 
                if p1 < p2:
                    if nums[p1] == 0: 
                        swap(p0, p1)
                    elif nums[p1] == 2: 
                        swap(p1, p2)
            else: 
                break 
            

            # print(p0, p1, p2)
            # print(nums)

        print(nums)
        
    
if __name__ == "__main__": 
    nums = [2,0,2,1,1,0]
    nums = [2,0,1]
    nums = [1,2,0]
    ret = Solution().sortColors(nums)
    print(ret)