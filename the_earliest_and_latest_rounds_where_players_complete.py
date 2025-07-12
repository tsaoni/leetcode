from typing import List

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        import math 
        def F(n, f, s, compare_fn): 
            depth = math.ceil(math.log2(n)) - 1
            _f, _s = n + 1 - f, n + 1 - s 
            if min(_f, _s) < min(f, s): 
                f, s = min(_f, _s), max(_f, _s)
            else: 
                f, s = min(f, s), max(f, s)
            
            mid = (n + 1) // 2 
            if s <= mid: 
                ret = max_iter if compare_fn == min else 1
                _n = (n + 1) // 2
                for i in range(f): 
                    for j in range(s - f): 
                        ret = compare_fn(ret, F(_n, i + 1, i + j + 2, compare_fn) + 1)
        
                return ret 
            else: 
                if f == n + 1 - s: 
                    return 1 
                else: 
                    _n = (n + 1) // 2 
                    _s = (n + 1) - s 
                    d = (n - 2 * _s + 1) // 2 
                    ret = max_iter if compare_fn == min else 1
                    for i in range(f): 
                        for j in range(_s - f): 
                            ret = compare_fn(ret, F(_n, i + 1, i + j + 2 + d, compare_fn) + 1)
                    
                    return ret
    
        
        max_iter = math.ceil(math.log2(n))
        # dp = [[[0] * n for _ in range(n)] for _ in range(max_iter)]
        max_it = F(n, firstPlayer, secondPlayer, min)
        
        # dp = [[[0] * n for _ in range(n)] for _ in range(max_iter)]
        min_it = F(n, firstPlayer, secondPlayer, max)
        return [max_it, min_it]
    
if __name__ == "__main__": 
    n = 11 
    firstPlayer = 2
    secondPlayer = 4

    # n = 5
    # firstPlayer = 1
    # secondPlayer = 5

    n = 5
    firstPlayer = 1
    secondPlayer = 4
    ret = Solution().earliestAndLatest(n, firstPlayer, secondPlayer)
    print(ret)