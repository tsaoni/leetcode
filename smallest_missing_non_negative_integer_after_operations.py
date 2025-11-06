from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cntr = [0] * value 
        mex = 0
        for n in nums: 
            tmp = n % value
            tmp = tmp if tmp >= 0 else value + tmp 
            cntr[tmp] += 1 
        idx = 0
        for i in range(value): 
            if cntr[i] < cntr[idx]: 
                idx = i

        mex = cntr[idx] * value + idx
        return mex
    
if __name__ == "__main__": 
    nums = [1,-10,7,13,6,8]
    value = 5
    # nums = [1,-10,7,13,6,8]
    # value = 7
    ret = Solution().findSmallestInteger(nums, value)
    print(ret)