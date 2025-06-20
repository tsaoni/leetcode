from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(self): 
        return 
    
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        from collections import defaultdict 
        s = defaultdict(set)
        for i in range(len(x)): 
            s[x[i]].add(y[i])
        l = []
        for _, values in s.items(): 
            l.append(max(values))
            l = sorted(l, key=lambda x: -x)[: 3]
        if len(l) < 3: 
            return -1
        return sum(l)

    def maximumProfit(self, prices: List[int], k: int) -> int:
        """
        results in TLE
        """
        dp = [[0] * len(prices) for _ in range(k)]
        min_idx, max_idx = 0, 0
        for i in range(1, len(prices)): 
            if prices[i] < prices[min_idx]:
                min_idx = i 
            if prices[i] > prices[max_idx]: 
                max_idx = i
            dp[0][i] = prices[max_idx] - prices[min_idx]
        
        for i in range(1, k): 
            for j in range(1, len(prices)): 
                min_idx, max_idx = j, j
                dp[i][j] = dp[i - 1][j]
                for m in range(j - 1, -1, -1): 
                    if prices[m + 1] < prices[min_idx]:
                        min_idx = m + 1 
                    if prices[m + 1] > prices[max_idx]: 
                        max_idx = m + 1
                    dp[i][j] = max(dp[i][j], dp[i - 1][m] + prices[max_idx] - prices[min_idx])
              
        return dp[k - 1][len(prices) - 1]

    def maximumProfit1(self, prices: List[int], k: int) -> int:
        profits = [[0, -float("inf"), -float("inf")]] + [[-float("inf")] * 3 for _ in range(k)]
        # three states: 0: ignore, 1: buy before, 2: sell before
        for p in prices: 
            _profits = [[0, -p, p]] + [[-float("inf")] * 3 for _ in range(k)]
            for i in range(k + 1): 
                # ignore
                # for state in range(3):
                #     _profits[i][state] = max(_profits[i][state], profits[i][state])
                if i < k:
                    _profits[i + 1][0] = max(_profits[i + 1][0], profits[i][2] - p, profits[i + 1][0])
                    _profits[i + 1][0] = max(_profits[i + 1][0], profits[i][1] + p, profits[i + 1][0]) 
            
                # buy
                _profits[i][1] = max(profits[i][1], profits[i][0] - p) \
                    if profits[i][1] is not None else profits[i][0] - p

                # sell 
                _profits[i][2] = max(profits[i][2], profits[i][0] + p) \
                    if profits[i][2] is not None else profits[i][0] + p 
                
            profits = _profits
            # print(profits)
        
        # print(profits)
        return max([x[0] for x in profits])

    def maxGCDScore(self, nums: List[int], k: int) -> int:
        
        return 0

if __name__ == "__main__": 
    # x = [1,2,1,3,2]
    # y = [5,3,4,6,2]

    # x = [1,2,1,2]
    # y = [4,5,6,7]
    # ret = Solution().maxSumDistinctTriplet(x, y)
    # print(ret)

    prices = [1,7,9,8,2]
    k = 2
    prices = [12,16,19,19,8,1,19,13,9]
    k = 3
    prices = [7,10,4,4,2,9,9,16,20] 
    k = 4
    ret = Solution().maximumProfit(prices, k)
    print(ret)