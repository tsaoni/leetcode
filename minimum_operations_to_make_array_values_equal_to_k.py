from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        cnt = 0
        for n in set(nums): 
            if n > k: 
                cnt += 1 
            elif n < k: 
                return -1
        return cnt 
    
if __name__ == "__main__": 
    ret = Solution().minOperations([1], 1)
    print(ret)