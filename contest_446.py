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
        class SegmentTree: 
            def __init__(self, arr): 
                self.n = len(arr)
                self.tree = [0] * (4 * self.n)
                self.build(arr, 0, 0, self.n - 1)

            def build(self, arr, node, start, end): 
                if start == end: 
                    self.tree[node] = arr[start]
                else: 
                    mid = (start + end) // 2
                    self.build(arr, 2 * node + 1, start, mid)
                    self.build(arr, 2 * node + 2, mid + 1, end)
                    self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


            def set(self, index, value, node=0, start=0, end=None): 
                if end is None: 
                    end = self.n - 1 
                if start == end: 
                    self.tree[node] = value 
                else: 
                    mid = (start + end) // 2 
                    if index <= mid: 
                        self.set(index, value, 2 * node + 1, start, mid)
                    else: 
                        self.set(index, value, 2 * node + 2, mid + 1, end)
                    self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
            
            def get_max(self, L, R, node=0, start=0, end=None): 
                if end is None: 
                    end = self.n - 1 
                if R < start or L > end: 
                    return float("-inf")
                if L <= start and R >= end: 
                    return self.tree[node]
                mid = (start + end) // 2 
                val = max(self.get_max(L, R, 2 * node + 1, start, mid), 
                        self.get_max(L, R, 2 * node + 2, mid + 1, end))
                return val

        acc = [[0] * k] 
        acc[0][nums[0] % k] += 1
        for i in range(1, len(nums)): 
            n = nums[i]
            tmp = [0] * k 
            tmp[n % k] = 1 
            for j in range(k): 
                tmp[acc[-1][j] * n % k] += acc[-1][j]
            acc.append(tmp) 
        
    
        for idx, val, start, x in queries: 
            f
        return 


if __name__ == "__main__": 
    nums = [1,2,3,4,5]
    k = 3
    test_case = (nums, k)
    ret = Solution().resultArray1(*test_case)
    print(ret)