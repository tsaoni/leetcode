from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        N = len(strs)
        M = len(strs[0])
        dp = [1] * M
        ret = 1
        for i in range(1, M): 
            for j in range(i): 
                a = True
                for n in range(N): 
                    a &= (strs[n][j] <= strs[n][i])
                if a:
                    dp[i] = max(dp[i], dp[j] + 1)
            ret = max(ret, dp[i])
        # print(dp)
        return M - ret 

if __name__ == "__main__": 
    strs = ["babca","bbazb"]
    strs = ["edcba"]
    strs = ["ghi","def","abc"]
    ret = Solution().minDeletionSize(strs)
    print(ret)