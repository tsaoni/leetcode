from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cntr = Counter()
        nr, crmax = -1, 0
        nrl = []
        for i in range(len(nums) - 1, -1, -1): 
            num = nums[i]
            cntr[num] += 1 
            if cntr[num] > crmax: 
                nr = num 
                crmax = cntr[num]
            nrl.insert(0, nr)
                # nrl = [nr] + nrl
        
        cntl = Counter()
        nl, clmax = -1, 0
        for idx, num in enumerate(nums[: -1]): 
            cntl[num] += 1 
            cntr[num] -= 1 
            if cntl[num] > clmax: 
                nl = num 
                clmax = cntl[num]
            
            kr = nrl[idx + 1] #max(cntr, key=cntr.get) 
            if kr == nl and cntr[kr] > (len(nums) - idx - 1) // 2 and clmax > (idx + 1) // 2: 
                return idx
            # if max(cntr, key=cntr.get) == nl: 
            #     return idx

        return -1
    
if __name__ == "__main__": 
    nums = [1,2,2,2] 
    # nums = [2,1,3,1,1,1,7,1,2,1]
    # nums = [3,3,3,3,7,2,2]
    test_case = (nums, )
    ret = Solution().minimumIndex(*test_case)
    print(ret)