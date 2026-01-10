from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        gain = 0
        max_gain = 0
        ori = 0
        N = len(prices) 
        for i in range(N): 
            ori += prices[i] * strategy[i]
            if i < k // 2: 
                gain += (0 - strategy[i]) * prices[i]
            elif i < k: 
                gain += (1 - strategy[i]) * prices[i]
            else: 
                gain -= (0 - strategy[i - k]) * prices[i - k]
                gain -= prices[i - k // 2]
                gain += (1 - strategy[i]) * prices[i]
            
            if i >= k - 1:
                max_gain = max(max_gain, gain)

            # print(ori, max_gain, gain)
        return ori + max_gain
    
if __name__ == "__main__": 
    prices = [4,2,8]
    strategy = [-1,0,1]
    k = 2
    prices = [5,4,3]
    strategy = [1,1,0]
    k = 2
    ret = Solution().maxProfit(prices, strategy, k)
    print(ret)