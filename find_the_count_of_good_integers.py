import math
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        kp_n = (n + 1) // 2
        kp_set = set()
        
        def find_k_palindromes(idx, num, kpl): 
            if idx == kp_n:
                tmp = num
                # start = kp_n % 2 
                for i, x in enumerate(kpl[::-1]):
                    if i == 0 and n % 2 == 1: 
                        continue
                    num = num * 10 + x 
                if num % k == 0: 
                    start = (n - 2) // 2
                    p = kpl + kpl[start:: -1]
                    kp_set.add(tuple(sorted(p)))
                    # if tuple(sorted(p)) == (1, 2, 2): 
                    #     import pdb 
                    #     pdb.set_trace()
            else:
                start = 1 if idx == 0 else 0
                for i in range(start, 10): 
                    find_k_palindromes(idx + 1, num * 10 + i, kpl + [i])
        
        find_k_palindromes(0, 0, [])
        # print(kp_set)
            
        def perm_num(p): 
            cnt = Counter()
            for n in p: 
                cnt[n] += 1 
            mul = math.factorial(len(p))
            lz_mul = math.factorial(len(p) - 1) if 0 in cnt else 0
            for n, c in cnt.items(): 
                if n == 0: 
                    lz_mul //= math.factorial(c - 1)
                else: 
                    lz_mul //= math.factorial(c)
                mul //= math.factorial(c)
            return mul - lz_mul
        
        ret = 0
        for kp in kp_set: 
            # start = (n - 2) // 2
            # p = tuple(kp + kp[start:: -1])
            c = perm_num(kp)
            ret += c
            # print(kp, c)
        return ret
    
if __name__ == "__main__": 
    n = 3
    k = 5
    
    n = 1
    k = 4

    # n = 5
    # k = 6

    n = 3
    k = 3
    test_case = (n, k)
    ret = Solution().countGoodIntegers(*test_case)
    print(ret)