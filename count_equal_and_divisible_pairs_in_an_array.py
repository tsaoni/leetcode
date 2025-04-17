from typing import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        idx_d = defaultdict(list)
        ret = 0
        for j in range(len(nums)): 
            for vi in idx_d[nums[j]]: 
                if vi * j % k == 0: 
                    ret += 1
            idx_d[nums[j]].append(j)

        return ret
    
if __name__ == "__main__": 
    ret = Solution().countPairs()
    print(ret)