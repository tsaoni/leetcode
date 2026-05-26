from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        # h, v = set({0}), set({0})
        def get_lens(brs, n_bar):
            if len(brs) > 0 and brs[0] == 1: 
                i = 0 
                while i < len(brs) - 1: 
                    if brs[i] + 1 == brs[i + 1]: 
                        i += 1 
                    else: 
                        break 
                brs = brs[i + 1:]
            if len(brs) > 0 and brs[-1] == n_bar: 
                i = len(brs) - 1
                while i > 0: 
                    if brs[i] - 1 == brs[i - 1]: 
                        i -= 1 
                    else: 
                        break 
                brs = brs[: i]
            if len(brs) == 0: 
                return 0
            ret = 1 
            l = 1 
            for i in range(len(brs) - 1): 
                if i < len(brs) - 1 and brs[i] + 1 == brs[i + 1]: 
                    l += 1 
                else: 
                    ret = max(ret, l)
                    l = 1 
            ret = max(ret, l)
            return ret 
        
        h = get_lens(hBars, n + 2)
        v = get_lens(vBars, m + 2)
        # h = sorted(h)
        # v = sorted(v)
        # print(h, v)
        x = min(h, v)
        
            
        return (x + 1) ** 2
    
if __name__ == "__main__": 
    n = 1
    m = 1
    hBars = [2]
    vBars = [2]

    n = 2
    m = 3
    hBars = [2,3]
    vBars = [1,2,4,5]
    ret = Solution().maximizeSquareHoleArea(n, m, hBars, vBars)
    print(ret)