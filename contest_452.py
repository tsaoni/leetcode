from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(self): 
        return  
    
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        import math
        maxp = 1 
        for n in nums: 
            maxp *= n
        if math.sqrt(maxp) != target: 
            return False
        # products = [1] + [0] * (target - 1) 
        cands = {0}
        for num in nums: 
            ncands = set()
            for i in cands: #range(target - 1, -1, -1): 
                p = i + 1 
                #if p % num == 0: 
                if p * num <= target:
                    # if products[p - 1]: 
                    # products[p * num - 1] = 1
                    ncands.add(p * num - 1)
    
                if p * num == target: 
                    return True
            cands = cands.union(ncands) 
            # d = []
            # for i in range(target): 
            #     if products[i]: 
            #         d.append(i + 1)
            # products[num - 1] = 1
            # print(d)
        return False

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        return [[]]

if __name__ == "__main__": 
    nums = [3,1,6,8,4]
    target = 24
    # nums = [2,5,3,7]
    # target = 15
    # nums = [20,14,18,15,7,12]
    # target = 2520
    ret = Solution().checkEqualPartitions(nums, target)
    print(ret)