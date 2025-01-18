class Solution:
    def check(self, s): 
        for i in range(0, int(len(s) / 2)): 
            if s[i] != s[len(s) - 1 - i]: return False 
        return True
    
    def minCut1(self, s: str) -> int:
        if len(s) < 2 or self.check(s): return 0
        min_cut = len(s) - 1
        for i in range(len(s) - 1): 
            left, right = slice(0, i + 1), slice(i + 1, None)
            l_cut = self.minCut1(s[left])
            r_cut = self.minCut1(s[right])
            min_cut = min(l_cut + r_cut + 1, min_cut)
        return min_cut
    
    def find_pal_at_end(self, s): 
        pals = []
        for i in range(len(s) - 1, -1, -1): 
            # # easy check 
            # c_lst = [c for c in s[slice(i, len(s))]]
            # if len(set(c_lst)) == 1:
            #     pals += [slice(i, len(s))]
            #     continue 
            start, end = i, len(s) - 1
            while start < end: 
                if s[start] == s[end]: 
                    start += 1 
                    end -= 1 
                else: 
                    break 
            if start >= end: 
                pals += [slice(i, len(s))]

        return pals
    
    def minCut(self, s: str) -> int:
        min_cut_lst = [0]
        for i in range(1, len(s)): 
            cur = s[: i + 1]
            # # easy check 
            c_lst = [c for c in cur]
            if len(set(c_lst)) == 1:
                min_cut_lst += [0]
                continue
            prev_c_lst = [c for c in s[: i]]
            if len(set(c_lst)) == 2 and len(set(prev_c_lst)) == 1:
                min_cut_lst += [1]
                continue
            pals = self.find_pal_at_end(cur)
            min_cut = i
            for p in pals: 
                idx = p.start - 1
                if idx < 0: min_cut = 0
                else: 
                    min_cut = min(min_cut_lst[idx] + 1, min_cut)
    
            min_cut_lst += [min_cut]
    
        return min_cut_lst[-1]

if __name__ == "__main__": 
    test_case = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    #"eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
    ret = Solution().minCut(test_case)
    print(ret)