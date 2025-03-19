from typing import List
from collections import defaultdict

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        val = defaultdict(int)
        for n in nums: 
            val[n] += 1 
        return all([v % 2 == 0 for k, v in val.items()])
    
if __name__ == "__main__": 
    Solution().divideArray()