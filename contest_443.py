from typing import List
import math

from collections import defaultdict
class Solution: 
    def func(): 
        return 
    
    def minCosts(self, cost: List[int]) -> List[int]:
        ret = []
        minv = cost[0]
        for i in range(len(cost)): 
            minv = min(minv, cost[i])
            ret += [minv]
        return ret

    def longestPalindrome1(self, s: str, t: str) -> int:
        s_lst = [s, t]
        for i in range(len(s)): 
            for j in range(len(t)): 
                s_lst.append(s[:i + 1] + t[j:])
        
        max_len = 1
        # print(s_lst)
        tmp = None
        for ss in s_lst: 
            for idx in range(len(ss)): 
                tmpl = 1
                start, end = idx - 1, idx + 1
                while start >= 0 and end < len(ss) and ss[start] == ss[end]: 
                    start -= 1 
                    end += 1 
                    tmpl += 2 
                max_len = max(max_len, tmpl)
                # if max_len == tmpl: 
                #     tmp = ss[start: end + 1]
                # print(ss[start: end + 1])

                tmpl = 0
                start, end = idx, idx + 1
                while start >= 0 and end < len(ss) and ss[start] == ss[end]: 
                    start -= 1 
                    end += 1 
                    tmpl += 2 
                max_len = max(max_len, tmpl)
                # if max_len == tmpl: 
                #     tmp = ss[start: end + 1]
                # print(ss[start: end + 1])

        # print(tmp)
        return max_len

    def longestPalindrome(self, s: str, t: str) -> int:
        """
        do not refer this
        """
        pstack = defaultdict(list)
        for si in range(len(s)): 
            n_pstack = defaultdict(list)
            for p, tidxs in pstack.items(): 
                if len(tidxs) > 0:
                    n_p = p + s[si]
                    n_tidxs = []
                    for tidx in tidxs: 
                        if tidx > 0 and t[tidx - 1] == s[si]: 
                            n_tidxs.append(tidx - 1)
                    if len(n_tidxs) > 0: 
                        n_pstack[n_p] = n_tidxs 
                    else: 
                        n_pstack[p] = []
            for ti in range(len(t)):
                if t[ti] == s[si]: 
                    n_pstack[s[si]].append(ti)
            pstack = n_pstack
        
        ret = 1
        for p, _ in pstack.items(): 
            sidx = s.index(p)
            tidx = t.index(p)
            if sidx < len(s) - 1 or tidx > 0: 
                ret = max(len(p) + 1, ret)
            else: 
                ret = max(len(p), ret)
        return ret

    def longestPalindrome_2(self, s: str, t: str) -> int:
        """
        should figure out a faster solution
        """
        if len(set(s)) == 1 and len(set(t)) == 1 and s[0] == t[0]: 
            return len(s) + len(t)
        
        from copy import deepcopy
        _t = "".join(reversed(t))
        def longest_palindrome(s): 
            p = s[0]
            cands = []
            for i, c in enumerate(s): 
                n_cands = []
                for cand in cands: 
                    if cand > 0 and s[cand - 1] == c: 
                        n_cands.append(cand - 1)
                        if i + 2 - cand > len(p):
                            p = s[cand - 1: i + 1] 
                if i > 0 and s[i - 1] == c: 
                    n_cands.append(i - 1)
                    if len(p) < 2: 
                        p = s[i - 1: i + 1]
                if i > 1 and s[i - 2] == c: 
                    n_cands.append(i - 2)
                    if len(p) < 3: 
                        p = s[i - 2: i + 1]

                cands = n_cands
            #     print(cands)
            # print()
            return p
        
        def longest_common_substring(s, t): 
            Ns, Nt = len(s), len(t) 
            cnts = [0] * (Ns + 1)
            max_cnt = 0
            max_cnts = [0] * (Ns + 1)
            idxs = [[-1, {-1}, None] for _ in range(Ns + 1)]
            for i in range(1, Nt + 1): 
                new_cnts = [0]
                # cur_idxs = [(-1, -1, None)]
                cur_max_cnt = 0
                for j in range(1, Ns + 1): 
                    if t[i - 1] == s[j - 1]: 
                        new_cnts.append(cnts[j - 1] + 1)
                        s_start, t_start = j - cnts[j - 1] - 1, i - cnts[j - 1] - 1
                        not_end = j < Ns  or i < Nt  #- cnts[j - 1] - 1 > 0
                        # cur_idxs.append((s_start, t_start, not_end))
                        cur_max_cnt = max(cur_max_cnt, cnts[j - 1] + 1)
                        if cnts[j - 1] + 1 > max_cnts[j]:
                            max_cnts[j] = cnts[j - 1] + 1 
                            idxs[j] = [s_start, {t_start}, not_end]
                        elif cnts[j - 1] + 1 == max_cnts[j]:
                            idxs[j][1] |= {t_start}
                    else: 
                        new_cnts.append(0)
                        # cur_idxs.append((-1, -1, None))
                
                cnts = new_cnts
                # if cur_max_cnt > max_cnt: 
                #     max_cnts = new_cnts
                #     max_cnt = cur_max_cnt
                #     idxs = cur_idxs
                
                # print(cur_max_cnt)
                # print(cnts)
                # print(idxs)
            
            
            if idxs is None: 
                return ""
            p = ""
            tmp = 0
            def get_palindrome_at_start(s): 
                if len(s) == 0: 
                    return ""
                p = s[0]
                l = 1
                for i in range(1, len(s)): 
                    if s[i] == s[0]: 
                        start, end = 1, i - 1
                        tmp = 2
                        while start <= end: 
                            if start == end: 
                                tmp += 1 
                            elif s[start] == s[end]: 
                                tmp += 2
                            else: 
                                tmp = 1 
                                break
                            start += 1 
                            end -= 1
                        l = max(l, tmp)
                        p = s[: l]
                return p
            
            def is_palindrome(s): 
                start, end = 0, len(s) - 1 
                while start < end: 
                    if s[start] != s[end]: 
                        return False 
                    start += 1 
                    end -= 1 
                return True
            
            for i in range(1, Ns + 1): 
                if True: #max_cnts[i] >= tmp: 
                    s_start, t_start_set, not_end = idxs[i]
                    for t_start in t_start_set:
                        if not_end is not None:
                            s_end, t_end = s_start + max_cnts[i], t_start + max_cnts[i]
                            add_c = ""
                            if not_end: 
                                cs, ct = add_c = get_palindrome_at_start(s[s_end: ]), get_palindrome_at_start(t[t_end: ]) 
                                add_c = cs if len(cs) > len(ct) else ct
                                add_c = cs + ct if is_palindrome(cs + ct) else add_c
                                # import pdb 
                                # pdb.set_trace()
                                # if s_end < Ns: 
                                #     add_c = get_palindrome_at_start(s[s_end: ])#s[s_end]
                                # else: 
                                #     add_c = get_palindrome_at_start(t[t_end: ]) #t[t_end]
                            subs = s[s_start: s_end]
                            subt = "".join(reversed(t[t_start: t_end]))
                            
                            _p = subs + add_c + subt
                            p = _p if len(_p) > len(p) else p
                            # print(subs, add_c, subt)
                            tmp = max_cnts[i]
            return p
        
        slp = longest_palindrome(s)
        tlp = longest_palindrome(t)
        lcs = longest_common_substring(s, _t)
        print("slp: ", slp, " tlp: ", tlp, " lcs: ", lcs)
        return max(len(slp), len(tlp), len(lcs))



if __name__ == "__main__": 
    # cost = [5,3,4,1,3,2]
    # cost = [1,2,4,6,7]
    # test_case = (cost, )
    # ret = Solution().minCosts(*test_case)
    s = "a"
    t = "a"
    s = "abc"
    t = "def"
    s = "b"
    t = "aaaa"
    s = "abcde"
    t = "ecdba"
    s = "x"
    t = "hnh"
    s = "xxz"
    t = "z"
    s = "i"
    t = "ih"
    s = "mrb"
    t = "r"
    s = "rtk" 
    t = "hrgpgt"
    s = "sqddk" 
    t = "qdmlw"
    s = "hxfa" 
    t = "xplpprpxux"
    s = "cjcyqvhbnmvuyjycdcmmcvbhgkdhtlxglsnoijmrrdaiaksnbm" 
    t = "sljcgeuhhlkbtvadvdgiedipcqtzzsidzwanafr"
    test_case = (s, t)
    ret = Solution().longestPalindrome_2(*test_case)
    print(ret)