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
        for ss in s_lst: 
            for idx in range(len(ss)): 
                tmpl = 1
                start, end = idx - 1, idx + 1
                while start >= 0 and end < len(ss) and ss[start] == ss[end]: 
                    start -= 1 
                    end += 1 
                    tmpl += 2 
                max_len = max(max_len, tmpl)
                # print(ss[start: end + 1])

                tmpl = 0
                start, end = idx, idx + 1
                while start >= 0 and end < len(ss) and ss[start] == ss[end]: 
                    start -= 1 
                    end += 1 
                    tmpl += 2 
                max_len = max(max_len, tmpl)
                # print(ss[start: end + 1])

                
        return max_len

    def longestPalindrome(self, s: str, t: str) -> int:
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
        
        return 

if __name__ == "__main__": 
    # cost = [5,3,4,1,3,2]
    # cost = [1,2,4,6,7]
    # test_case = (cost, )
    # ret = Solution().minCosts(*test_case)
    s = "a"
    t = "a"
    # s = "abc"
    # t = "def"
    # s = "b"
    # t = "aaaa"
    # s = "abcde"
    # t = "ecdba"
    test_case = (s, t)
    ret = Solution().longestPalindrome1(*test_case)
    print(ret)