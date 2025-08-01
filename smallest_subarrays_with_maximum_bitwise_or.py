from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        """
        TLE
        """
        ret = []
        end = len(nums)
        res = 0
        def find(start, end, res): 
            l, r = start + 1, end  
            def OR(start, end): 
                res = 0 
                for n in nums[start: end]: 
                    res |= n 
                return res
            while l < r: 
                mid = (l + r) // 2 
                if OR(start, mid) < res: 
                    l = mid + 1
                else: 
                    r = mid 
            return l
        
        for i in range(len(nums) - 1, -1, -1): 
            res |= nums[i]
            end = find(i, end, res)
            ret.insert(0, end - i)
        return ret
    
    def smallestSubarrays_1(self, nums: List[int]) -> List[int]:
        ret = []
        end = len(nums)
        res = 0

        import math 
        n_digits = math.ceil(math.log2(10 ** 9))
        b = [0] * n_digits
        for i in range(len(nums) - 1, -1, -1): 
            tmp = nums[i]
            d = 0
            while tmp > 0: 
                if tmp & 1: 
                    b[d] += 1 
                d += 1 
                tmp >>= 1 
            # print(b)
            while end > i + 1:
                d = 0 
                tmp = nums[end - 1]
                # dec = True 
                while tmp > 0: 
                    if tmp & 1 and b[d] == 1: 
                        # dec = False 
                        break
                    d += 1 
                    tmp >>= 1 
                if tmp > 0: break 
                d = 0
                tmp = nums[end - 1]
                while tmp > 0: 
                    if tmp & 1: 
                        b[d] -= 1 
                    d += 1 
                    tmp >>= 1 
                end -= 1  
            ret.insert(0, end - i)
        return ret 

if __name__ == "__main__": 
    nums = [1,0,2,1,3]
    # nums = [1,2]
    ret = Solution().smallestSubarrays_1(nums)
    print(ret)