from typing import List

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        minN = -10 ** 6
        N, M = len(nums1), len(nums2)
        _dp = [0] * (M + 1) 
        dp = [0] + [minN] * (M) 
        for i in range(N): 
            n = nums1[i]
            for j in range(1, M + 1): 
                if i == 0: 
                    if j == 1: 
                        dp[j] = nums2[j - 1] * n
                    else:
                        dp[j] = max(dp[j - 1], nums2[j - 1] * n)
                else:
                    x = nums2[j - 1] * n
                    if j == 1: 
                        dp[j] = max(_dp[j], x + _dp[j - 1], x) 
                    else:
                        dp[j] = max(dp[j - 1], _dp[j], x + _dp[j - 1], x)
            tmp = _dp 
            _dp = dp 
            dp = tmp 
            # print(_dp)
        return _dp[-1] 
    
if __name__ == "__main__": 
    nums1 = [2,1,-2,5]
    nums2 = [3,0,-6]
    nums1 = [3,-2]
    nums2 = [2,-6,7]
    nums1 = [-1,-1]
    nums2 = [1,1]
    nums1 = [-5,-1,-2] 
    nums2 = [3,3,5,5]
    nums1 = [-5,3,-5,-3,1] 
    nums2 = [-2,4,2,5,-5]
    nums1 = [-3,-8,3,-10,1,3,9] 
    nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]
    ret = Solution().maxDotProduct(nums1, nums2)
    print(ret)