from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        live = sorted(batteries)
        extra = sum(live[: -n])
        live = live[-n: ]
        max_t = (extra + sum(live)) // n
        l, r = 0, max_t 
        def check(t, buf): 
            cur = live[0]
            i = 0 
            while i < n - 1: 
                fil = (live[i + 1] - live[i]) * (i + 1)
                if buf >= fil: 
                    cur = live[i + 1]
                    buf -= fil
                else: 
                    cur += buf // (i + 1)
                    break
                i += 1

            if i == n - 1: 
                cur += buf // n
            return True if cur >= t else False
        # print(check(50, extra))
        # import pdb 
        # pdb.set_trace()

        while l < r: 
            mid = (l + r + 1) // 2 
            if check(mid, extra): 
                l = mid 
            else: 
                r = mid - 1
        return l
    
if __name__ == "__main__": 
    n = 2
    batteries = [3,3,3]
    # n = 2
    # batteries = [1,1,1,1]
    # n = 3 
    # batteries = [10,10,3,5]
    # n = 3 
    # batteries = [10,10,6,9,3]
    n = 12 
    batteries = [11,89,16,32,70,67,35,35,31,24,41,29,6,53,78,83]
    ret = Solution().maxRunTime(n, batteries)
    print(ret)