from typing import List

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        """
        a two pointer problem 
        time complexity: O(n)
        """
        nums.sort()
        N = len(nums)
        def count(u): 
            # if u < 0: return 0
            start, end = 0, N - 1 
            cnt = 0
            while start < end: 
                # print(start, end)
                pend = end
                while end > 0 and nums[end] == nums[end - 1]: 
                    end -= 1
                if nums[end] * 2 <= u: 
                    cnt += (pend - end + 1) * (pend - end) // 2
                while start < end and nums[start] + nums[end] <= u: 
                    start += 1 
                cnt += start * (pend - end + 1)
                end -= 1 
                # print(cnt)
            # import pdb 
            # pdb.set_trace()
            cnt += (end + 1) * end // 2
            
            return cnt 

        return count(upper) - count(lower - 1)
    
if __name__ == "__main__": 
    nums = [0,1,7,4,4,5]
    lower = 3
    upper = 6
    # nums = [1,7,9,2,5]
    # lower = 11
    # upper = 11
    nums = [0,0,0,0,0,0]
    lower = 0
    upper = 0
    test_case = (nums, lower, upper)
    ret = Solution().countFairPairs(*test_case)
    print(ret)