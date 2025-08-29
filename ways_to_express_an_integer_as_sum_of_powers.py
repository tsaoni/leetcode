class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        dp = [[1] + [0] * n for _ in range(n + 1)]
        modulo = 10 ** 9 + 7
        for num in range(1, n + 1): 
            tmp = num ** x
            for s in range(1, n + 1): 
                if s >= tmp:
                    dp[num][s] = dp[num - 1][s] + dp[num - 1][s - tmp]
                    dp[num][s] %= modulo
                else: 
                    dp[num][s] = dp[num - 1][s]

        return dp[-1][-1]
    
if __name__ == "__main__": 
    n = 10
    x = 2
    n = 4
    x = 1
    ret = Solution().numberOfWays(n, x)
    print(ret)