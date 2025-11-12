from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        def gcd(a, b): 
            if a == 0: 
                return b 
            else: 
                b = b - a
                return gcd(b, a) if b < a else gcd(a, b)
        _nums = []
        of = 1
        non1 = 0
        for x in nums: 
            _nums.append(x)
            if x == 1: 
                of = 0
            else: 
                non1 += 1

        if of == 0: 
            return non1
        lv = False
        while not lv and len(_nums) > 1: 
            for i in range(len(_nums) - 1): 
                _nums[i] = gcd(_nums[i], nums[i + of]) if _nums[i] < nums[i + of] else gcd(nums[i + of], _nums[i])
                if _nums[i] == 1: 
                    lv = True 
                    break
            _nums.pop(-1)
            of += 1
        if of == N and _nums[0] > 1: 
            return -1 
        return N + of - 2
    
if __name__ == "__main__": 
    nums = [2,6,3,4]
    nums = [2,10,6,14]
    nums = [1,2]
    ret = Solution().minOperations(nums)
    print(ret)