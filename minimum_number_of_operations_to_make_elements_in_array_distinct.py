from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        s = {}
        ret = 0
        for i, n in enumerate(nums): 
            if n in s: # remove
                idx = s[n]
                while ret * 3 <= idx: 
                    ret += 1
            s[n] = i
        return ret
    
if __name__ == "__main__": 
    ret = Solution().minimumOperations
    print(ret)