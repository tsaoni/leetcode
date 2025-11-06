from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(list(filter(lambda x: x > 0, nums)))
        ret = 0
        for f in range(len(nums) - 2): 
            s = f + 1 
            for l in range(f + 2, len(nums)): 
                while s < l and nums[f] + nums[s] <= nums[l]: 
                    s += 1 
                ret += (l - s)
        return ret
    
if __name__ == "__main__": 
    nums = [2,2,3,4]
    nums = [4,2,3,4]
    # nums = [0,0,0]
    ret = Solution().triangleNumber(nums)
    print(ret)