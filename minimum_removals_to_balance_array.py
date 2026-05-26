from typing import List

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        def search(val): 
            l, r = 0, N - 1 
            while l < r: 
                mid = (l + r) // 2 
                if nums[mid] * k >= val: 
                    r = mid 
                else: 
                    l = mid + 1
            return l 
        
        pre, end = search(nums[N - 1]), N - 1 
        ret = N - (end - pre + 1)
        # print(ret)
        while pre > 0: 
            end -= 1 
            while pre > 0 and nums[pre - 1] * k >= nums[end]: 
                pre -= 1 
            tmp = N - (end - pre + 1)
            if tmp <= ret: 
                ret = tmp 
                # print(ret)
            # else: 
            #     break 
        return ret 

if __name__ == "__main__": 
    nums = [2,1,5]
    k = 2
    nums = [1,6,2,9]
    k = 3
    nums = [4,6]
    k = 2
    nums = [92,75,335,26,221,19,54]
    k = 4
    ret = Solution().minRemoval(nums, k)
    print(ret)