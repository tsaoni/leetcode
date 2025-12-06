from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        ps = [0] * (N + 1)
        # ps[0] = -1
        min_s, max_s = [], []
        for i in range(N): 
            
            # import pdb 
            # pdb.set_trace()
            while len(min_s) > 0 and nums[min_s[-1][0]] > nums[i]: 
                _, idx = min_s.pop(-1)
            idx = 0 if len(min_s) == 0 else min_s[-1][1]
            while idx < len(min_s): 
                if nums[i] - nums[min_s[idx][0]] <= k: 
                    break 
                idx += 1 
            min_s.append((i, idx))
            _idx = idx

            
            while len(max_s) > 0 and nums[max_s[-1][0]] < nums[i]: 
                _, idx = max_s.pop(-1)
            idx = 0 if len(max_s) == 0 else max_s[-1][1]
            while idx < len(max_s): 
                if nums[max_s[idx][0]] - nums[i] <= k: 
                    break 
                idx += 1 
            max_s.append((i, idx))

            _idx = min_s[_idx - 1][0] + 1 if _idx > 0 else 0
            idx = max_s[idx - 1][0] + 1 if idx > 0 else 0
            
            print(min_s, max_s, _idx, idx)
            idx = max(_idx, idx)
            if i == 0: 
                ps[i + 1] = 1 
            else:
                if idx > 1:
                    ps[i + 1] = 2 * ps[i] - ps[idx - 1]
                elif idx == 1: 
                    ps[i + 1] = 2 * ps[i] - 1
                elif idx == 0: 
                    ps[i + 1] = 2 * ps[i] 
            print(ps, idx)
            # import pdb 
            # pdb.set_trace()
            
        return ps[-1]
    
if __name__ == "__main__": 
    nums = [9,4,1,3,7]
    k = 4
    ret = Solution().countPartitions(nums, k)
    print(ret)