from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        cnt_dict = Counter()
        cnt = 0
        N = len(nums)
        ret = 0
        head = 0
        for i in range(N): 
            n = nums[i]
            cnt_dict[n] += 1 
            if cnt_dict[n] > 1: 
                tmp = cnt_dict[n]
                cnt += tmp * (tmp - 1) // 2 - (tmp - 1) * (tmp - 2) // 2

            ret += head
            while cnt >= k: 
                # print(nums[head: i + 1])
                n = nums[head]
                tmp = cnt_dict[n]
                cnt -= tmp * (tmp - 1) // 2 - (tmp - 1) * (tmp - 2) // 2
                cnt_dict[n] -= 1
                ret += 1
                head += 1

        return ret
    
if __name__ == "__main__": 
    nums = [1,1,1,1,1]
    k = 10
    nums = [3,1,4,3,2,2,4]
    k = 2
    # nums = [2,3,1,3,2,3,3,3,1,1,3,2,2,2] 
    # k = 18
    test_case = (nums, k)
    ret = Solution().countGood(*test_case)
    print(ret)