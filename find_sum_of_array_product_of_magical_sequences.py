from typing import List

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        """
        time complexity: O(n * m ** 3 * k)
        space complexity: O(n * m ** 2 * k)
        """
        n = len(nums)
        dp = [[[[[0] for _ in range(k + 1)] for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n)]
        modulo = 10 ** 9 + 7 
        
        for i in range(n): 
            for j in range(m): 
                dp

        return 
    
if __name__ == "__main__": 
    m = 5
    k = 5
    nums = [1,10,100,10000,1000000]
    ret = Solution().magicalSum(m, k, nums)