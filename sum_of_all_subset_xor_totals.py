from typing import List

class Solution:
    def subsetXORSum1(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        n_or = 0 
        N = len(nums)
        for n in nums: 
            n_or |= n 
        multiplier = 2 ** (N - 1) # since an odd number of 1s will always appear 2^(N-1) times

        return n_or * multiplier
    
    def subsetXORSum(self, nums: List[int]) -> int:
        
        ret = 0
        N = len(nums)
        def xor(a, b): 
            ret = 0
            base = 1
            for i in range(5): 
                c = (a % 2) ^ (b % 2)
                ret += c * base
                base *= 2 
                a //= 2 
                b //= 2
            return ret

        def xorsum(idx, n):
            if idx == N - 1: 
                return xor(0, n) + xor(nums[idx], n)

            ret = xorsum(idx + 1, n)
            _n = xor(nums[idx], n)
            ret += xorsum(idx + 1, _n)
            return ret
        
        return 0 if len(nums) == 0 else xorsum(0, 0) 
    
if __name__ == "__main__": 
    nums = [1,3]
    test_case = (nums, )
    ret = Solution().subsetXORSum(*test_case)
    print(ret)