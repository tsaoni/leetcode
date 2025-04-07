from typing import List

class Solution:
    def largestDivisibleSubset1(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()

        parents = [-1] * N 
        sz = [0] * N 
        max_i = 0
        for i in range(N): 
            n = nums[i]
            for j in range(i): 
                if n % nums[j] == 0: 
                    if sz[j] + 1 > sz[i]: 
                        sz[i] = sz[j] + 1 
                        parents[i] = j
            if sz[i] > sz[max_i]: 
                max_i = i
        
        s = set()
        while max_i != -1: 
            s |= {nums[max_i]}
            max_i = parents[max_i]

        return list(s)

        # div = []
        # cur = set()
        # for ni in range(N): 
        #     num = nums[ni]
        #     s = cur
        #     while True:
        #         d = set()
        #         ns = set()
        #         for idx in s: 
        #             if num % nums[idx] == 0: 
        #                 print("%", num, nums[ni], ni, nums[idx])
        #                 d |= {idx}
        #             else: 
        #                 ns |= set(div[idx])
        #         if len(d) > 0 or len(ns) == 0: 
        #             break
        #         else: 
        #             s = ns
        #     cur = cur - d | {ni}
        #     div.append(d)
        #     print(ni, cur)
        # print(div)
        # print(nums)
        # return 
    
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        TLE
        """
        N = len(nums)
        nums.sort()
        
        def find_largest(idx, cur, s): 
            ns = s
            for i in range(idx, N): 
                if nums[i] % cur == 0: 
                    tmp = find_largest(i + 1, nums[i], s + [nums[i]])
                    if len(tmp) > len(ns):
                        ns = tmp
            return ns

     
        return find_largest(0, 1, [])
    
if __name__ == "__main__": 
    nums = [1,2,3] 
    # nums = [1,2,4,8]
    # nums = [5,9,18,54,108,540,90,180,360,720]
    test_case = (nums, )
    ret = Solution().largestDivisibleSubset1(*test_case)
    print(ret)