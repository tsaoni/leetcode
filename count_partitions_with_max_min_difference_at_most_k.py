from typing import List

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        wrong approach
        """
        N = len(nums)
        dp = [0] * (N + 1)
        ps = [0] * (N + 1)
        # ps[0] = -1
        modulo = 10 ** 9 + 7
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
                dp[i + 1] = 1
            else:
                val = lambda x: dp[x] if x > 0 else 0
                dp[i + 1] += val(i)
                ps[i + 1] = val(i) - val(idx - 1)
                if idx == 0: 
                    ps[i + 1] += 1
                dp[i + 1] += ps[i + 1]
                dp[i + 1] %= modulo 
                ps[i + 1] %= modulo
                
            print(ps, dp, idx)
            # import pdb 
            # pdb.set_trace()
            
        return ps[-1]
    
    def countPartitions_1(self, nums: List[int], k: int) -> int:
      
        N = len(nums)
        dp = [0] * (N + 1)
        ps = [0] * (N + 1)
        # ps[0] = -1
        modulo = 10 ** 9 + 7
        min_q, max_q = [], []
        idx = 0
        for i in range(N): 
            
            # import pdb 
            # pdb.set_trace()
            
            while len(min_q) > 0 and nums[min_q[-1]] > nums[i]: 
                min_q.pop(-1)
            min_q.append(i)

            while len(max_q) > 0 and nums[max_q[-1]] < nums[i]: 
                max_q.pop(-1)
            max_q.append(i)

            # idx = 0
            if len(max_q) == 1: 
                while nums[max_q[0]] - nums[min_q[0]] > k: 
                    idx = min_q.pop(0)
                    idx += 1
                    # print("h", idx)
            elif len(min_q) == 1: 
                while nums[max_q[0]] - nums[min_q[0]] > k: 
                    idx = max_q.pop(0)
                    idx += 1
                    # print("h", idx)
        
            # print(max_q, min_q)

            if i == 0: 
                ps[i + 1] = 1 
                dp[i + 1] = 1
            else:
                val = lambda x: dp[x] if x > 0 else 0
                dp[i + 1] += val(i)
                ps[i + 1] = val(i) - val(idx - 1)
                if idx == 0: 
                    ps[i + 1] += 1
                dp[i + 1] += ps[i + 1]
                dp[i + 1] %= modulo 
                ps[i + 1] %= modulo
                
            # print(ps, dp, idx)
            # import pdb 
            # pdb.set_trace()
            
        return ps[-1]
    
if __name__ == "__main__": 
    nums = [9,4,1,3,7]
    k = 4
    nums = [3,3,4]
    k = 0
    # nums = [25,10,22] 
    # k = 14
    ret = Solution().countPartitions_1(nums, k)
    print(ret)