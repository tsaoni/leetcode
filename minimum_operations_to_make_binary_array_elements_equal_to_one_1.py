from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_ops = 0
        for i, num in enumerate(nums): 
            if i > len(nums) - 3 and sum(nums[-2:]) < 2: 
                n_ops = -1
                break
            if num == 0: 
                for j in range(i, min(i + 3, len(nums))): 
                    nums[j] ^= 1 
                n_ops += 1 
            # print(nums)
            
        return n_ops
    
if __name__ == "__main__": 
    nums = [0,1,1,1,0,0]
    nums = [0,1,1,1]
    test_case = (nums, )
    ret = Solution().minOperations(*test_case)
    print(ret)