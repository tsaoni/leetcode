from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        N = max(nums) * 2
        modulo = 10 ** 9 + 7
        dp = {} #[[0, 0, 0, 0] for _ in range(N + 1)]
        ret = 0 
        for n in nums: 
            if n == 0: 
                if n not in dp: 
                    dp[n] = [0, 0, 0, 0, 0]
                dp[n][1] += 1  
                if dp[n][1] >= 3: 
                    ret += (dp[n][1] - 1) * (dp[n][1] - 2) // 2
                    ret %= modulo 
            else:
                if n not in dp: 
                    dp[n] = [0, 0, 0, 0, 0]
                if 2 * n not in dp: 
                    dp[2 * n] = [0, 0, 0, 0, 0]
                # if (n % 2 == 0) and (n // 2 not in dp): 
                #     dp[n // 2] = [0, 0, 0, 0]
                
                dp[n][1] += 1  
                dp[n * 2][0] += dp[n * 2][1]
                dp[n * 2][1] = 0 
                dp[n][3] += 1 
                if n % 2 == 0: 
                    # dp[n][1] += 1 
                    rev_i = n // 2
                    if rev_i not in dp: 
                        dp[rev_i] = [0, 0, 0, 0, 0]
                    if dp[rev_i][3] > 0:
                        dp[rev_i][2] = dp[rev_i][3]
                        dp[rev_i][3] = 0
                        dp[rev_i][4] += dp[n][0] * dp[rev_i][2]
                        dp[rev_i][4] %= modulo
                    ret += dp[rev_i][4] #dp[n][0] * dp[rev_i][2]
                    ret %= modulo
                    # print(ret, n)
                # print(dp)
                # import pdb 
                # pdb.set_trace()
        return ret 
    
if __name__ == "__main__": 
    nums = [6,3,6]
    # nums = [0,1,0,0]
    # nums = [8,4,2,8,4]
    # nums = [37,9,24,12,12,24,52,35]
    nums = [84,2,93,1,2,2,26]
    nums = [84,2,93,1,2,2,26,1,1,2]
    nums = [2,1,2,1,2]
    ret = Solution().specialTriplets(nums)
    print(ret)