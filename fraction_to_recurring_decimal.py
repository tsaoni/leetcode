class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        import math 
        MAX_LEN = 10 ** 4 
        digits = []
        sign = "-" if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator >= 0) else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        f = math.gcd(numerator, denominator)
        numerator //= f 
        denominator //= f 

        tmp = numerator 
        while tmp > 0: 
            digits.insert(0, tmp % 10)
            tmp //= 10 
        cur = 0
        integer, fraction = numerator // denominator, []
        cur = numerator - denominator * integer
        # print(cur, integer)
        # remain_idx = [-1] * denominator
        mp = {}
        ridx = -1
        
        # for i in range(MAX_LEN): 
        while cur > 0:
            idx = cur
            cur *= 10
            # if i < len(digits): 
            #     cur += digits[i]
        
            factor = cur // denominator
            
            # if i < len(digits): 
            #     integer = integer * 10 + factor
            # else: 
            if True:
                if idx in mp: 
                    ridx = mp[idx]
                # if remain_idx[idx] >= 0: 
                #     ridx = remain_idx[idx]
                    break
                fraction.append(str(factor))
                # remain_idx[idx] = len(fraction) - 1
                mp[idx] = len(fraction) - 1

            cur -= denominator * factor
            if cur == 0: 
                break 

        ret = str(integer)
        if len(fraction) > 0: 
            ret += "."
            if ridx >= 0: 
                ret += "".join(fraction[: ridx]) + "(" + "".join(fraction[ridx: ]) + ")"
            else: 
                ret += "".join(fraction)
        return sign + ret
    
if __name__ == "__main__": 
    numerator = 1
    denominator = 2
    numerator = 2
    denominator = 1
    numerator = 4
    denominator = 333
    # numerator = 0
    # denominator = 3
    # numerator = 500
    # denominator = 10
    # numerator = -1
    # denominator = -2147483648
    # numerator = 1
    # denominator = 6
    ret = Solution().fractionToDecimal(numerator, denominator)
    print(ret)