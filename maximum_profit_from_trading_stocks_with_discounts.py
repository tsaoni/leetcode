from typing import List

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        from collections import defaultdict
        T = defaultdict(list)
        for u, v in hierarchy: 
            T[u].append(v)
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(budget + 1)]
        def dfs(cur, b): 
            pre = cur 
            for nxt in T[cur]: 
                pre 
                lst = dfs(nxt, b)
                pre = lst  
            return pre 
        
        for b in range(1, budget + 1): 
            dfs(1, b)
            
        return 0 
    
if __name__ == "__main__": 
    Solution().maxProfit