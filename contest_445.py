from collections import Counter
import math

class Solution: 
    def func(): 
        return 
    
    def smallestPalindrome(self, s: str) -> str:
        if len(s) == 1: 
            return s 
        else:
            l = len(s) // 2 - 1
            cl = sorted(s[: l + 1])
            
            return "".join(cl) + "".join(cl[::-1]) if len(s) % 2 == 0 else "".join(cl) + s[l + 1] +  "".join(cl[::-1])
    
    def smallestPalindrome_2(self, s: str, k: int) -> str:
        """too bad, TLE"""
        if len(s) == 1: 
            return s if k == 1 else ""
        else:
            l = len(s) // 2 - 1
            cl = sorted(s[: l + 1])

            def swap(cl, i, j): 
                tmp = cl[i]
                cl[i] = cl[j]
                cl[j] = tmp

            def perm_num(s): 
                if len(s) == 1: 
                    return 1
                cnt = Counter()
                for c in s: 
                    cnt[c] += 1 
                ret = math.factorial(len(s))
                for _, c in cnt.items(): 
                    ret //= math.factorial(c)
                return ret

            def perm(cl, idx, cnt): 
                if idx == len(cl) - 1: 
                    # print(cnt + 1, "".join(cl) + "".join(cl[::-1]) if len(s) % 2 == 0 else "".join(cl) + s[l + 1] +  "".join(cl[::-1]))
                    if cnt + 1 == k:
                        return cnt + 1, "".join(cl) + "".join(cl[::-1]) if len(s) % 2 == 0 else "".join(cl) + s[l + 1] +  "".join(cl[::-1])
                    return cnt + 1, "" 
                else: 
                    seen = set()
                    for nidx in range(idx, len(cl)):
                        if nidx > idx and cl[nidx] == cl[idx]: 
                            continue
                        # swap(cl, idx, nidx)
                        if cl[nidx] in seen: 
                            continue
                        
                        x = cl.pop(nidx)
                        cl.insert(idx, x)
                        pn = perm_num(cl[idx + 1: ])
                        if k - cnt > pn: 
                            # print(cl[idx + 1:], pn)
                            cnt += pn
                            x = cl.pop(idx)
                            cl.insert(nidx, x)
                            seen.add(x)
                            continue
                        
                        cnt, ss = perm(cl, idx + 1, cnt)
                        seen.add(x)
                        if cnt == k: 
                            return cnt, ss
                        # swap(cl, idx, nidx)
                        x = cl.pop(idx)
                        cl.insert(nidx, x)
                        


                    # cnt, ss = perm(cl, idx + 1, cnt)
                    # if cnt == k: 
                    #     return cnt, ss
                    # swap(cl, idx, idx + 1)
                    # cnt, ss = perm(cl, idx + 1, cnt)
                    # if cnt == k: 
                    #     return cnt, ss
                    # swap(cl, idx, idx + 1)
                    return cnt, ""
            

        return perm(cl, 0, 0)[1]

    def smallestPalindrome_2_1(self, s: str, k: int) -> str:
        if len(s) == 1: 
            return s if k == 1 else ""
        else:
            l = len(s) // 2 
            cl = sorted(s[: l])
            cmid = s[l] if len(s) & 1 else ""
            cs = []
            cnts, ptrs = [], [] 
            prev = None
            for c in cl: 
                if prev != c: 
                    cs.append(c)
                    cnts.append(1)
                    ptrs.append(len(cnts))
                else: 
                    cnts[-1] += 1
                prev = c 
            Nc = len(cnts) 
            # print(cs)
            # print(cnts) 
            # print(ptrs) 

            def perm_num(cnts): 
                total = sum(cnts)
                fl = [1] 
                for i in range(total): 
                    fl.append((i + 1) * fl[-1])
                
                ret = fl[total] #math.factorial(total) 
                for n in cnts:
                    ret //= fl[n] #math.factorial(n)
                return ret
            cur_pn = perm_num(cnts)
            # print(cur_pn)
            
            def perm(start, kr, kstr): 
                nonlocal cur_pn
                # if kr == 0: 
                #     i = start 
                #     while i < Nc: 
                #         kstr += cs[i] * cnts[i]
                #         i = ptrs[i]
                #     return kstr 
                
                i = start
                # for i in range(start, Nc): 
                while i < Nc:
                    tmp = cur_pn
                    tmp *= cnts[i]
                    tmp //= (len(cl) - len(kstr))
                    cnts[i] -= 1 
                    # tmp = perm_num(cnts)
                    if tmp < kr: 
                        kr -= tmp
                        cnts[i] += 1 
                        i = ptrs[i]
                        continue 
                    elif tmp == kr: 
                        kstr += cs[i]
                        i = start 
                        subs = ""
                        while i < Nc: 
                            subs += cs[i] * cnts[i]
                            i = ptrs[i]
                        kstr += subs[::-1]
                        return kstr + cmid + kstr[::-1]
                    else: 
                        cur_pn = tmp
                        nstart = start
                        if cnts[i] == 0: 
                            pi = i
                            while pi >= 0 and cnts[pi] == 0: 
                                pi -= 1 
                            if pi >= 0: 
                                ptrs[pi] = ptrs[i]
                            
                            # print(nstart, cnts)
                            while cnts[nstart] == 0:
                                nstart += 1
            
                        return perm(nstart, kr, kstr + cs[i])
                        cnts[i] += 1 
                return ""

            return perm(0, k, "")

if __name__ == "__main__": 
    s = "abba"
    k = 2
    # s = "aa"
    # k = 2
    # s = "bacab"
    # k = 1
    # s = "xiccix"
    # k = 6
    # s = "ghdhhdhg"
    # k = 5
    # s = "xxnfnxx" 
    # k = 3
    # s = "ztyzzytz" 
    # k = 15
    s = "kkkk"
    k = 1
    test_case = (s, k)
    ret = Solution().smallestPalindrome_2_1(*test_case)
    print(ret)