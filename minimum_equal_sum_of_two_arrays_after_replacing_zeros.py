from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zcnt1, zcnt2 = 0, 0
        sum1, sum2 = 0, 0
        for n in nums1: 
            if n == 0: 
                zcnt1 += 1 
            sum1 += n
        for n in nums2: 
            if n == 0: 
                zcnt2 += 1 
            sum2 += n

        if zcnt1 == 0: 
            if sum1 < sum2 + zcnt2: 
                return -1 
        if zcnt2 == 0: 
            if sum2 < sum1 + zcnt1: 
                return -1


        return max(sum1 + zcnt1, sum2 + zcnt2)
    
if __name__ == "__main__": 
    ret = Solution().minSum()
    print(ret)