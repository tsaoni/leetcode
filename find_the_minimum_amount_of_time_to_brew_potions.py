from typing import List

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        dp = [0] * (n + 1)
        # _dp = [0] * (n + 1)
        for x in mana: 
            idx = -1 
            d = 0
            start = dp[1] 
            for i in range(1, n): 
                # print(dp[i + 1] - (start + skill[i - 1] * x))
                tmp = skill[i - 1] * x
                if dp[i + 1] - (start + tmp) >= d: 
                    idx = i 
                    d = dp[i + 1] - (start + tmp)
                start = start + tmp
            # _dp = [0] * (n + 1)
            if idx < 0: 
                dp[0] = dp[1]  #+ skill[0] * x
                for i in range(1, n + 1): 
                    dp[i] = dp[i - 1] + skill[i - 1] * x
            else: 
                dp[idx] = dp[idx + 1]
                for i in range(idx - 1, -1, -1): 
                    dp[i] = dp[i + 1] - skill[i] * x 
                for i in range(idx + 1, n + 1): 
                    dp[i] = dp[i - 1] + skill[i - 1] * x
            # dp = _dp
            # print(idx, dp)
        return dp[-1]
    
if __name__ == "__main__": 
    skill = [1,5,2,4]
    mana = [5,1,4,2]
    skill = [1,1,1]
    mana = [1,1,1]
    skill = [1,2,3,4]
    mana = [1,2]
    skill = [9,4,5] 
    mana = [6,6,8,10]
    ret = Solution().minTime(skill, mana)
    print(ret)