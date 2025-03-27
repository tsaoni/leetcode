from typing import List
from collections import defaultdict

class Solution:
    def minOperations1(self, grid: list[list[int]], x: int) -> int:
        arr = sorted([a for row in grid for a in row])
        if any((a - arr[0]) % x for a in arr):
            return -1

        ans = 0

        for a in arr:
            print(abs(a - arr[len(arr) // 2]) // x)
            ans += abs(a - arr[len(arr) // 2]) // x

        return ans
    
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # check 
        cntd = defaultdict(int)
        N = len(grid) * len(grid[0])
        if N == 1: 
            return 0
        nums = set()
        n = grid[0][0] % x
        for el in grid: 
            for e in el: 
                if e % x != n: 
                    return -1 
                cntd[e] += 1
                nums |= {e}

        # count
        nums = sorted(list(nums))
        # threshold = N // 2
        acc = 0
        walk = 0
        for i, num in enumerate(nums): 
            c = cntd[num]
            # print(c,acc + c, N - acc - c)
            if acc + c > N - acc - c: 
                # print(i)
                # print(acc + c, N - acc)
                # cnt = len(nums) - i - 1
                acc = 0
                for j in range(len(nums) - 1, i, -1): 
                    # print((nums[i + 1] - nums[i]) * cnt // x)
                    acc += cntd[nums[j]]
                    walk += (nums[j] - nums[j - 1]) * acc
                    # print(acc)
                    # i += 1

                # import pdb 
                # pdb.set_trace()
                return walk // x
            # print(acc)
            
            acc += c
            # tmp = nums[i - 1] if i > 0 else 0
            walk += (nums[i + 1] - nums[i]) * acc #(i + 1)
            
            # print((nums[i + 1] - nums[i]) * (i + 1) // x)
            
        
    
if __name__ == "__main__": 
    grid = [[2,4],[6,8]]
    x = 2
    # grid = [[1,5],[2,3]]
    # x = 1
    # grid = [[1,2],[3,4]]
    # x = 2
    # grid = [[931,128],[639,712]]
    # x = 73
    # grid = [[529,529,989],[989,529,345],[989,805,69]]
    # x = 92
    test_case = (grid, x)
    ret = Solution().minOperations(*test_case)
    print(ret)