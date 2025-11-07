from typing import List

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        diff = [x for x in stations] 
        le, ri = 0, min(N - 1, r) 
        add = sum([stations[d] for d in range(1, r + 1)])
        minv, maxv = -1, k
        for i in range(N): 
            minv = min(minv, stations[i]) if minv >= 0 else stations[i]
            maxv += stations[i]
            diff[i] += add  
            if i == N - 1: 
                break
            add += stations[i]
            add -= stations[i + 1]
            if ri < N - 1: 
                add += stations[ri + 1]
                ri += 1
            if le == i - r: 
                add -= stations[le]
                le += 1

        # print(diff, minv, maxv)
        def check(val, buf): 
            ps = [0] * N
            l = 2 * r + 1
            for i, x in enumerate(diff): 
                if i > 0: 
                    ps[i] += ps[i - 1]
                x += ps[i]
                if x < val: 
                    add = val - x 
                    if buf < add: 
                        return False
                    else: 
                        buf -= add 
                    ps[i] += add 
                    if i + l < N: 
                        ps[i + l] -= add
               
            return True

        while minv < maxv: 
            mid = (minv + maxv + 1) // 2 
            # print(minv, maxv, mid)
            if check(mid, k): 
                minv = mid 
            else: 
                maxv = mid - 1  

        return minv 
    
if __name__ == "__main__": 
    stations = [1,2,4,5,0]
    r = 1
    k = 2

    # stations = [4,4,4,4]
    # r = 0
    # k = 3
    
    stations = [4,2]
    r = 1 
    k = 1

    stations = [13,12,8,14,7] 
    r = 2 
    k = 23
    ret = Solution().maxPower(stations, r, k)
    print(ret)