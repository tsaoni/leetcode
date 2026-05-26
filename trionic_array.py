from typing import List

class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        prev = None 
        state = -1 
        ret = -float("inf")
        acc1 = s1 = e1 = a2 = _acc1 = _s1 = _e1 = -float("inf")
        for i, n in enumerate(nums):
            if prev is not None:
                if state == -1:
                    if n > prev: 
                        acc1 += n 
                        s1 = max(s1, acc1)
                        if i < (len(nums) - 1) and nums[i + 1] > nums[i]:
                            e1 = max(n, e1 + n)
                        else: 
                            e1 = e1 + n
                        state = 0
                    else: 
                        acc1 = s1 = e1 = n
                        a2 = _acc1 = _s1 = _e1 = -float("inf")
                elif state == 0: 
                    if n > prev: 
                        acc1 += n 
                        s1 = max(s1, acc1)
                        if i < (len(nums) - 1) and nums[i + 1] > nums[i]:
                            e1 = max(n, e1 + n)
                        else: 
                            e1 = e1 + n
                        tmp = _e1 + a2 + s1
                        ret = max(ret, tmp)
                    elif n < prev: 
                        # tmp = _e1 + a2 + s1
                        # ret = max(ret, tmp)
                        _s1, _e1 = s1, e1 
                        a2 = n 
                        state = 1 
                    else: 
                        acc1 = s1 = e1 = n
                        a2 = _acc1 = _s1 = _e1 = -float("inf")
                        state = -1
                elif state == 1: 
                    if n > prev: 
                        a2 -= prev
                        acc1 = prev + n 
                        s1 = acc1
                        if i < (len(nums) - 1) and nums[i + 1] > nums[i]:
                            e1 = max(acc1, n)
                        else: 
                            e1 = acc1
                        tmp = _e1 + a2 + s1
                        ret = max(ret, tmp)
                        state = 0 
                    elif n < prev: 
                        a2 += n 
                    else: 
                        acc1 = s1 = e1 = n
                        a2 = _acc1 = _s1 = _e1 = -float("inf")
                        state = -1
            else: 
                acc1 = s1 = e1 = n
        
            prev = n 
            # print(acc1, s1, e1, a2, _acc1, _s1, _e1, ret)
        return ret 
    
if __name__ == "__main__": 
    nums = [0,-2,-1,-3,0,2,-1]
    # nums = [1,4,2,7]
    nums = [-434,332,-519,-175,917,-316,645]
    ret = Solution().maxSumTrionic(nums)
    print(ret)