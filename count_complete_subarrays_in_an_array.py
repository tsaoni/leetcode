from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        last_idxs = [-1] * 2000
        k = len(set(nums))
        start, cnt = 0, 0
        ret = 0
        for i in range(N): 
            n = nums[i]
            if last_idxs[n - 1] < 0: 
                cnt += 1
            last_idxs[n - 1] = i 
            # print(last_idxs[n - 1])
            # print(last_idxs[nums[start] - 1])
            if cnt == k: 
                while last_idxs[nums[start] - 1] > start: 
                    start += 1 
                last_idxs[nums[start] - 1] = -1 
                start += 1
                cnt -= 1
    
            ret += start 
            # print(ret)
            # print(start)
            # print()
        return ret
    
if __name__ == "__main__": 
    nums = [1,3,1,2,2]
    # nums = [5,5,5,5]
    ret = Solution().countCompleteSubarrays(nums)
    print(ret)