class Solution:

    def countGoodArrays1(self, n: int, m: int, k: int) -> int:
        import math
        modulo = 10 ** 9 + 7
        cnt = 0
        def exp_mul(num, exp): 
            res = 1
            tmp = num
            while exp > 0: 
                if exp & 1:
                    res *= tmp 
                    res %= modulo
                tmp = tmp * tmp 
                tmp %= modulo
                exp //= 2
            return res 
        
        mul = m * exp_mul(m - 1, n - k - 1) #((m - 1) ** (n - k - 1))
        mul %= modulo

        cnt = math.comb(n - 1, k) % modulo
        return cnt * mul % modulo 
    
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        import math
        modulo = 10 ** 9 + 7
        cnt = 0
        def exp_mul(num, exp): 
            res = 1
            tmp = num
            while exp > 0: 
                if exp & 1:
                    res *= tmp 
                    res %= modulo
                tmp = tmp * tmp 
                tmp %= modulo
                exp //= 2
            return res 
        
        mul = m * exp_mul(m - 1, n - k - 1) #((m - 1) ** (n - k - 1))
        mul %= modulo
        # print(mul)
        c1, c2 = 1, 1
        for i in range(1, k + 1): 
            # if n - k - i >= i - 1:
                # cnt += mul * math.comb(k - 1, i - 1) * math.comb(n - k - i + 1, i)
            if i > 1:
                # if c1 == 1: 
                #     c1 = k - 1
                if i < k:
                    c1 = c1 * (k - i + 1) // (i - 1) 
                else: 
                    c1 = 1
                
                # c1 %= modulo
            c2 = c2 * (n - k + 1 - i) // i
            # c2 %= modulo
            
            cnt += (c1 % modulo) * (c2 % modulo) 
            

            # cnt += mul * math.comb(k - 1, i - 1) * math.comb(n - k, i)
            cnt %= modulo
            # print(c1, cnt)
            # k + i, n - k - i, i 
    
        # 2 * k, n - 2 * k, k 
        # k + i, n - k - i, i  
        # k + 1, n - k - 1, 1

        cnt = 1 if cnt == 0 else cnt
        return cnt * mul % modulo
    
    
if __name__ == "__main__": 
    n = 3
    m = 2
    k = 1
    n = 4
    m = 2
    k = 2
    # n = 5
    # m = 2
    # k = 0
    n = 40603 
    m = 16984 
    k = 29979
    ret = Solution().countGoodArrays(n, m, k)
    print(ret)