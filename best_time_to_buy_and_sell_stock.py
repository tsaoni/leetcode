from typing import List

class Solution:
    def maximumProfit_v(self, prices: List[int], k: int) -> int:
        N = len(prices)
        _dp = [[-float("inf")] * 3 for _ in range(k + 1)]
        dp = [[-float("inf")] * 3 for _ in range(k + 1)]
        _dp[0][0] = dp[0][0] = 0
        for i in range(N): 
            for j in range(k + 1): 
                if j > 0:
                    _dp[j][0] = max(dp[j][0], dp[j - 1][1] - prices[i], dp[j - 1][2] + prices[i])
                if j < k + 1:
                    _dp[j][1] = max(dp[j][1], dp[j][0] + prices[i])
                    _dp[j][2] = max(dp[j][2], dp[j][0] - prices[i])
            
            # print(_dp)
            tmp = dp 
            dp = _dp 
            _dp = tmp
            
        return max([x[0] for x in dp])
    
if __name__ == "__main__": 
    prices = [1,7,9,8,2]
    k = 2
    prices = [12,16,19,19,8,1,19,13,9]
    k = 3
    prices = [14,6,10,19] 
    k = 1
    prices = [6,11,1,5,3,15,8] 
    k = 3
    ret = Solution().maximumProfit_v(prices, k)
    print(ret)