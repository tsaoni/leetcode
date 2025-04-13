import math

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # ret = 1
        mod = (10 ** 9) + 7
        n_even = math.ceil(n / 2)
        n_odd = n // 2
        n_2 = n_odd * 2 #2
        if n_even > n_2: 
            return (5 ** n_even) * (2 ** n_2) % mod 
        else: 
            def fast_exp(base, exp): 
                ret = 1
                while exp > 1:
                    lg_mod = math.ceil(math.log((10 ** 9) + 7) / math.log(base))
                    ret *= base ** (exp % lg_mod)
                    exp = exp // lg_mod 
                    base = (base ** lg_mod) % mod
                ret *= (base ** exp) 
                return ret % mod
            return (fast_exp(2, n_2 - n_even) * fast_exp(10, n_even)) % mod
                #2 ** (n_2 - n_even) * 10 ** n_even % mod
        
        # for i in range(n): 
        #     if i % 2 == 0: 
        #         ret *= 5 
        #     else: 
        #         ret *= 4 
        #     ret = ret % mod
        # return ret
    
if __name__ == "__main__": 
    ret = Solution().countGoodNumbers(806166225460393)
    
    print(ret)