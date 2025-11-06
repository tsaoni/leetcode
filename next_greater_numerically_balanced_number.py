class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        from collections import Counter
        tmp = n 
        d = 0 
        s = ""
        while tmp > 0: 
            d += 1
            s = str(tmp % 10) + s
            tmp //= 10
        # n_digits = [i + 1 for i in range(9)]  
        def find(cur, ncur, acc, rem, is_larger): 
            if cur == d: 
                for _, c in rem.items(): 
                    if c > 0: 
                        return None
                # print(ncur)
                return ncur if is_larger else None
            else:
                for i in range(9): 
                    # print(cur, i, rem)
                    add_new = False
                    if is_larger or i + 1  >= int(s[cur]):
                        if i + 1 not in rem and acc + (i + 1) <= d: 
                            rem[i + 1] = i + 1
                            acc += (i + 1)
                            add_new = True
                        if rem[i + 1] > 0:
                            _ncur = ncur * 10 + (i + 1)
                            _is_larger = (i + 1) > int(s[cur]) or is_larger
                            rem[i + 1] -= 1
                            res = find(cur + 1, _ncur, acc, rem, _is_larger)
                            rem[i + 1] += 1
                            if res: 
                                return res
                    if add_new: 
                        del rem[i + 1] 
                        acc -= (i + 1)
                return None
        
        ret = find(0, 0, 0, Counter(), False)
        if ret is None: 
            d += 1
            s = "0" + s
            # print(d)
            ret = find(0, 0, 0, Counter(), False)
        return ret
    
if __name__ == "__main__": 
    n = 1
    n = 1000
    n = 3000
    n = 3133
    ret = Solution().nextBeautifulNumber(n)
    print(ret)