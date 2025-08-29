class Solution:
    def soupServings(self, n: int) -> float:
        if n == 0: 
            return 0.5
        elif n > 10000: 
            return 1.
        import math 
        l = math.ceil(n / 25)
        dp = []
        for i in range(l + 1): 
            r = [0] * (l + 1)
            for j in range(l + 1): 
                t0 = r[j - 4] if j > 4 else 1
                if i > 1 and j > 3:
                    t1 = dp[-1][j - 3] 
                elif i <= 1 and j > 3:
                    t1 = 0 
                elif i <= 1 and j <= 3:
                    t1 = 0.5
                else: 
                    t1 = 1 

                if i > 2 and j > 2:
                    t2 = dp[-2][j - 2] 
                elif i <= 2 and j > 2:
                    t2 = 0 
                elif i <= 2 and j <= 2:
                    t2 = 0.5
                else: 
                    t2 = 1 
              
                if i > 3 and j > 1:
                    t3 = dp[-3][j - 1] 
                elif i <= 3 and j > 1:
                    t3 = 0 
                elif i <= 3 and j <= 1:
                    t3 = 0.5
                else: 
                    t3 = 1 
               
                r[j] = sum([0.25 * t for t in [t0, t1, t2, t3]])
            dp.append(r)
            dp = dp[-3:]
        
            if 1 - dp[-1][-1] < 10 ** (-5): 
                return 1.
        
        return dp[-1][-1]
    
if __name__ == "__main__": 
    n = 50
    n = 100
    n = 660295675
    # n = 10000
    ret = Solution().soupServings(n)
    print(ret)