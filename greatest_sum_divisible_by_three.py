from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        maxn = [0] * 3 
        for n in nums: 
            _maxn = [x for x in maxn] 
            for i in range(3): 
                idx = (maxn[i] + n) % 3
                if i == 0 or i > 0 and maxn[i] > 0:
                    _maxn[idx] = max(maxn[i] + n, maxn[idx])
               
                
            maxn = _maxn
            # print(maxn)
        return maxn[0]
    
if __name__ == "__main__": 
    nums = [3,6,5,1,8]
    nums = [4]
    nums = [1,2,3,4,4]
    ret = Solution().maxSumDivThree(nums)
    print(ret)