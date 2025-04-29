from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_n = max(nums) 
        cnt = 0 
        ranges = []
        for n in nums: 
            if n == max_n: 
                ranges.append(cnt)
                cnt = 0
            else: 
                cnt += 1 
        ranges.append(cnt)
        # print(ranges)

        ret = 0
        acc = 0
        for i in range(len(ranges) - k): 
            acc += ranges[i] + 1
            ret += acc * (ranges[i + k] + 1)
        return ret
    
if __name__ == "__main__": 
    nums = [1,3,2,3,3]
    k = 2
    nums = [1,4,2,1]
    k = 3
    test_case = (nums, k)
    ret = Solution().countSubarrays(*test_case)
    print(ret)