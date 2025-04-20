from collections import Counter
import math 
from typing import List

class Solution: 
    def func(): 
        return 
    
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        N = len(instructions)
        visited = [False] * N 
        idx = 0
        score = 0
        while idx >= 0 and idx < N and not visited[idx]: 
            visited[idx] = True
            if instructions[idx] == "add": 
                score += values[idx] 
                idx += 1 
            else: 
                idx += values[idx]
        return score
    
    def maximumPossibleSize(self, nums: List[int]) -> int:
        N = len(nums)
        start = 1
        ret = 1
        v = nums[0]
        while start < N: 
            if nums[start] >= v: 
                ret += 1 
            v = max(v, nums[start])
            start += 1
        return ret 
    
    def resultArray1(self, nums: List[int], k: int) -> List[int]:
        # arr = [0] * k 
        # for i in range(nums): 
        #     arr[nums[i] % k] += 1 
        acc = [0] * k 
        ret = [0] * k
        acc[nums[0] % k] += 1
        ret[nums[0] % k] += 1
        for i in range(1, len(nums)): 
            # print(acc)
            n = nums[i] 
            nacc = [0] * k
            nacc[n % k] += 1
            for j in range(k): 
                nacc[j * n % k] += acc[j]
            acc = nacc
            for j in range(k): 
                ret[j] += acc[j]
        return ret

    def resultArray(self, nums: List[int], k: int) -> List[int]:
        """
        TLE
        """
        products = nums 
        arr = [0] * k 
        idx = 1
        while len(products): 
            # print(products)
            nproducts = []
            for i, p in enumerate(products): 
                tmp = p % k
                arr[tmp] += 1 
                if i + idx < len(nums):
                    nproducts.append(tmp * nums[i + idx])
            idx += 1
            products = nproducts
        
        return arr
    
    def resultArray_2(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        acc = [[0] * k] 
        acc[0][nums[0] % k] += 1
        for i in range(1, len(nums)): 
            n = nums[i]
            tmp = [0] * k 
            tmp[n % k] = 1 
            for j in range(k): 
                tmp[acc[-1][j] * n % k] += acc[-1][j]
            acc.append(tmp) 
        
        d = []
        product = 1
        for i in range(len(nums) - 1, -1, -1): 
            product *= nums[i]
            product %= k
            d.insert(0, product)
        
        for idx, val, start, x in queries: 
            f
        return 


if __name__ == "__main__": 
    nums = [1,2,3,4,5]
    k = 3
    test_case = (nums, k)
    ret = Solution().resultArray1(*test_case)
    print(ret)