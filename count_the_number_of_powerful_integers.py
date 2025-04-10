class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        for c in s: 
            if int(c) > limit: 
                return 0
        si = sum([int(x) * (10 ** i) for i, x in enumerate(s[::-1])])
        d_sfx = 1 
        while si // (10 ** d_sfx) > 0: 
            d_sfx += 1

        pstart, pend = start // (10 ** d_sfx), finish // (10 ** d_sfx)  
        if start % (10 ** d_sfx) > si: 
            pstart += 1 
        if finish % (10 ** d_sfx) < si: 
            pend -= 1 
        
        def count(num): 
            if num == 0: 
                return 1
            elif num < 0: 
                return 0
            
            d_pfx = 0
            while pend // (10 ** (d_pfx)) > 0: 
                d_pfx += 1
            
            dp = []
            isequal = True
            for i in range(d_pfx - 1, -1, -1): 
                if num // (10 ** i) % 10 > limit: 
                    ub = limit + 1
                else: 
                    ub = num // (10 ** i) % 10
                # ub = min(num // (10 ** i) % 10, limit)
                if len(dp) > 0:
                    if isequal:
                        dp.append(dp[-1] * (limit + 1) + ub)
                    else: 
                        dp.append(dp[-1] * (limit + 1))
                else: 
                    dp.append(ub)
                isequal &= ub <= limit
            # print(dp)
            return dp[-1] + 1 if isequal else dp[-1]

        # print(pstart)
        # print(pend)
        return count(pend) - count(pstart - 1)
    
if __name__ == "__main__": 
    start = 1
    finish = 6000
    limit = 4
    s = "124"
    
    # start = 15
    # finish = 215
    # limit = 6
    # s = "10"

    # start = 1000
    # finish = 2000
    # limit = 4
    # s = "3000"

    # start = 20 
    # finish = 1159 
    # limit = 5 
    # s = "20"

    start = 1114 
    finish = 1864854501 
    limit = 7
    s = "26"
    test_case = (start, finish, limit, s)
    ret = Solution().numberOfPowerfulInt(*test_case)
    print(ret)