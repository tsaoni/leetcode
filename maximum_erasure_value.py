from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        S = set()
        start = 0
        
        nxt = [-1] * len(nums)
        d = {}
        for i in range(len(nums) - 1, -1, -1): 
            if nums[i] in d: 
                nxt[i] = d[nums[i]]
            d[nums[i]] = i 
        
        for i in range(1, len(nums)): 
            nums[i] += nums[i - 1]
        # print(nums)
        ret = 0
        for i in range(len(nums)): 
            x = nums[i] - nums[i - 1] if i > 0 else nums[i]
            if x in S: 
               
                ret = max(ret, nums[i - 1] - (nums[start - 1] if start > 0 else 0))
                print(start, i, ret)
                while nums[start] - (nums[start - 1] if start > 0 else 0) != x:
                    # print(nums[start], x)
                    if nxt[start] > i or nxt[start] == -1: 
                        S.remove(nums[start] - (nums[start - 1] if start > 0 else 0))
                    start += 1 
                print(nums[start]- (nums[start - 1] if start > 0 else 0), x)
                start += 1
                
                
            S.add(x)
        ret = max(ret, nums[len(nums) - 1] - (nums[start - 1] if start > 0 else 0))
        return ret
    
if __name__ == "__main__": 
    nums = [4,2,4,5,6]
    # nums = [5,2,1,2,5,2,1,2,5]
    nums = [558,508,782,32,187,103,370,607,619,267,984,10]
    nums = [11]
    ret = Solution().maximumUniqueSubarray(nums)
    print(ret)