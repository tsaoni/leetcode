from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        start, end = -1, -1
        cnt, inc = [0, 0], [] # stack for inclusive indexes
        ret = 0
        for i in range(N + 1): 
            if i < N and nums[i] >= minK and nums[i] <= maxK: 
                if nums[i] == minK:
                    cnt[0] += 1
                    inc.append((0, i))
                elif nums[i] == maxK: 
                    cnt[1] += 1
                    inc.append((1, i))
        
                end = i 
                if start < 0: 
                    start = i
                if minK == maxK and cnt[0] > 0 or minK < maxK and all([c > 0 for c in cnt]): 
                    while cnt[inc[0][0]] > 1: 
                        cnt[inc[0][0]] -= 1 
                        inc.pop(0)
                        
                    ret += inc[0][1] - start + 1
                    # print(cnt)
                    # print(start, inc, ret)
            else: 
                start = -1
                cnt, inc = [0, 0], []
        return ret
    
if __name__ == "__main__": 
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    # nums = [1,1,1,1]
    # minK = 1
    # maxK = 1
    
    test_case = (nums, minK, maxK)
    ret = Solution().countSubarrays(*test_case)
    print(ret)