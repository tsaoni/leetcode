class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3: 
            return n 
        else: 
            dp = [1, 2] + [0] * (n - 2)
            for i in range(2, n): 
                dp[i] = 2 + dp[i - 2] + dp[i - 1] + 2 * sum(dp[: i - 2])
              
        # print(dp)
        return dp[-1] % (10 ** 9 + 7)
    
if __name__ == "__main__": 
    ret = Solution().numTilings(5)
    print(ret)