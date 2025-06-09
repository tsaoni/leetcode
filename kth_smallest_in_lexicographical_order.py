class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        n_digits = 0 
        digits = []
        tmp = n
        while tmp > 0: 
            n_digits += 1 
            digits.insert(0, tmp % 10)
            tmp //= 10 
        
        def compute(prefix, digits): 
            isupper = 1 
            cnt = 1
            ret = 1
            n_bound = 0
            pnum, dnum = 0, 0
            for i in range(n_digits): 
                if i < len(prefix): 
                    pnum *= 10 
                    pnum += prefix[i]
                    dnum *= 10 
                    dnum += digits[i]
                    if pnum < dnum: 
                        isupper = 0 
                    if pnum > dnum: 
                        isupper = 2 
                if i >= len(prefix): 
                    if isupper == 1: 
                        n_bound *= 10 
                        n_bound += digits[i]
                    if i == n_digits - 1 and isupper > 0: 
                        if isupper == 1:
                            ret += n_bound + 1
                    else:
                        ret += 10 ** cnt
                        cnt += 1 
            return ret

        def compute_num(prefix):
            state = 1
            pnum, dnum = 0, 0
            for i in range(n_digits): 
                if i < len(prefix): 
                    pnum *= 10 
                    pnum += prefix[i]
                    dnum *= 10 
                    dnum += digits[i]
                    if pnum < dnum: 
                        state = 0
                    if pnum > dnum: 
                        state = 2
            if state == 0: 
                prefix += [9] * (len(digits) - len(prefix))
            elif state == 1: 
                prefix += [digits[i] for i in range(len(prefix), len(digits))]
            else:
                prefix += [9] * (len(digits) - len(prefix) - 1)
            
            ret = 0 
            for p in prefix: 
                ret *= 10 
                ret += p 
            return ret

        def find(cnt, prefix):
            # print(prefix)
            start = 1 if len(prefix) == 0 else 0 
            for i in range(start, 10): 
                # import pdb 
                # pdb.set_trace()
                tmp = compute(prefix + [i], digits)
                # print(prefix + [i], tmp, cnt, tmp + cnt)
                if tmp + cnt > k: 
                    cnt += 1
                    if cnt == k: 
                        prefix += [i]
                        ret = 0
                        for p in prefix:
                            ret *= 10 
                            ret += p
                        return ret
                  
                    return find(cnt, prefix + [i])
                elif tmp + cnt == k: 
                    prefix += [i]
                    
                    return compute_num(prefix)
                else: 
                    cnt += tmp 
    
            # print(cnt)
            return -1

        # n_digits = 7
        # ret = compute([2, 9], [4, 2, 8, 9, 3, 8, 4])     
        # print(ret) 
        # import pdb 
        # pdb.set_trace()
        ret = find(0, [])
        return ret
    
if __name__ == "__main__": 
    n = 13
    k = 2
    n = 1
    k = 1
    n = 1000000000
    k = 999999999
    # k = 1000000000
    # n = 100 
    # k = 90
    # n = 4289384 
    # k = 1922239
    ret = Solution().findKthNumber(n, k)
    print(ret)