from typing import List

class Solution:
    
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        from collections import Counter
        d = Counter
        for x, y in dominoes: 
            t = tuple(sorted([x, y]))
            d[t] += 1 
        
        ret = 0
        for k, v in d.items(): 
            ret += v * (v - 1) // 2

        return ret
    
