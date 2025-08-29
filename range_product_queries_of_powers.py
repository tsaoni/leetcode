from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        tmp, num = n, 0 
        modulo = 10 ** 9 + 7
        while tmp > 0: 
            if tmp & 1: 
                powers.append(num)
            tmp >>= 1 
            num += 1 
        for i in range(1, len(powers)): 
            powers[i] += powers[i - 1] 
        ret = []
        def power_exp(base, exp): 
            mul = base
            ret = 1 
            while exp > 0: 
                if exp & 1: 
                    ret *= mul
                    ret %= modulo 
                mul = mul * mul 
                exp >>= 1
            return ret
        for start, end in queries:
            exp = powers[end] - powers[start - 1] if start > 0 else powers[end]
            ret.append(power_exp(2, exp))
        return ret
    
if __name__ == "__main__": 
    n = 15
    queries = [[0,1],[2,2],[0,3]]
    n = 2
    queries = [[0,0]]
    ret = Solution().productQueries(n, queries)
    print(ret)