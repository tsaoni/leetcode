class Solution:
    def robotWithString(self, s: str) -> str:
        """
        a wrong approach
        """
        import string 
        p = ""
        last_idxs = [[] for _ in range(26)] 
        get_idx_fn = lambda c: ord(c) - ord('a')
        for i, c in enumerate(s): 
            last_idxs[get_idx_fn(c)].append(i)
        start_idx = 0
        def compare_reverse(s1, s2): 
            l = min(len(s1), len(s2))
            for i in range(-1, -l - 1, -1): 
                if s1[i] < s2[i]: 
                    return True 
                if s1[i] > s2[i]: 
                    return False 
            return len(s1) < len(s2)

        for c in string.ascii_lowercase: 
            if start_idx == len(s): 
                break 
            idx = get_idx_fn(c)
            if len(last_idxs[idx]) > 0 and last_idxs[idx][-1] >= start_idx: 
                top = -1
                for i, ii in enumerate(last_idxs[idx]): 
                    if ii < start_idx: 
                        continue 
            
                    if top >= 0:
                        ii0 = start_idx if top == 0 else last_idxs[idx][top - 1]
                        ii1, ii2 = last_idxs[idx][top], ii
                        issublarger = compare_reverse(s[ii0: ii1 + 1], s[ii1 + 1: ii2 + 1])
                        if issublarger: 
                            for j in range(ii1, ii0 - 1, -1):
                                p += s[j]
                            start_idx = last_idxs[idx][top] + 1
                    top = i 
                # import pdb 
                # pdb.set_trace()
                for j in range(last_idxs[idx][top], start_idx - 1, -1): 
                    p += s[j]
                start_idx = last_idxs[idx][top] + 1
                # print(p, start_idx)
        return p
    
    def robotWithString1(self, s: str) -> str:
        import string 
        p = ""
        last_idxs = [[] for _ in range(26)] 
        get_idx_fn = lambda c: ord(c) - ord('a')
        for i, c in enumerate(s): 
            last_idxs[get_idx_fn(c)].append(i)
        
        start_idx = 0
        stack = []
        for c in string.ascii_lowercase: 
            idx = get_idx_fn(c)
            while len(stack) > 0 and stack[-1] <= c: 
                tmp = stack.pop(-1)
                p += tmp
            for i in last_idxs[idx]: 
                if i >= start_idx:
                    for j in range(start_idx, i):
                        stack.append(s[j])
                    p += s[i]
                    start_idx = i + 1
        # print(p)
        # print(stack)
        
        p += "".join(list(reversed(stack)))
        return p

if __name__ == "__main__": 
    s = "zza"
    # s = "bac"
    s = "bdda"
    s = "bydizfve"
    s = "xayar"
    ret = Solution().robotWithString1(s)
    print(ret)