class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k+maxPts-1: return 1.0
        dp = [1] + [0] * n
        p = 1
        ret = 0
        for i in range(1, n + 1): 
            # if i <= k:
            dp[i] = p / maxPts
            if i >= k: 
                ret += dp[i]
        
            if i < k:
                p += dp[i]

            if i >= maxPts: 
                p -= dp[i - maxPts]
    
            
            
        #     print(dp, p)
        # print(sum(dp))

        return ret
    
if __name__ == "__main__": 
    n = 10
    k = 1
    maxPts = 10
    # n = 6
    # k = 1
    # maxPts = 10
    # n = 21
    # k = 17
    # maxPts = 10
    ret = Solution().new21Game(n, k, maxPts)
    print(ret)