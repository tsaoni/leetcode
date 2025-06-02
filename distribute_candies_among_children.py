from typing import List

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        import math 
        ret = 0
        for i in range(4): 
            remain = n - (limit + 1) * i
            
            if remain >= 0:
                ret += (1 if i & 1 == 0 else -1) * math.comb(3, i) * math.comb(remain + 2, 2)
            else: 
                break
            # print(remain, ret)

        return ret
    
if __name__ == "__main__": 
    n = 5
    limit = 2
    n = 2 
    limit = 1
    ret = Solution().distributeCandies(n, limit)
    print(ret)