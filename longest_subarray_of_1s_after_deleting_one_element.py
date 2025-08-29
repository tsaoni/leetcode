from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        _cnt, cnt = 0, 0 
        pre = None 
        max_cnt = 0
        hz = False 
        i = 0
        while i < len(nums): 
            n = nums[i]
            if pre != n: 
                if pre == 0 and cnt == 1: 
                    hz = True 
                    if True:
                        while i < len(nums) and nums[i] == 1: 
                            i += 1  
                            cnt += 1
                            # print(i)
                        # print(_cnt, cnt)
                        max_cnt = max(_cnt + cnt - 1, max_cnt)
                    # if _cnt > 0:
                    # _cnt = cnt - 1
                    # cnt = 0
                    cnt -= 2
                    i -= 1
                else:
                    # print("pre", _cnt, cnt)
                    if pre == 1:
                        max_cnt = max(cnt, max_cnt)
                        _cnt = cnt
                    cnt = 0 
            cnt += 1 
            pre = n 
            i += 1
        
        if pre == 1:
            max_cnt = max(cnt, max_cnt)
        if not hz and len(nums) == max_cnt: 
            return max_cnt - 1 
        else: 
            return max_cnt