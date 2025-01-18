class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ptrs = [0]
        valid = True
        # easy check
        s_set = set([c for c in s])
        p_set = set([c for i, c in enumerate(p) 
                    if c not in [".", "*"] and not (i < len(p) - 1 and p[i + 1] == "*")])
        for c in p_set: 
            if c not in s_set: 
                return False
        # main
        for i, c in enumerate(s): 
            new_ptrs = []
            for j, id in enumerate(ptrs): 
                p_c = p[id]
                # print(f"c = {c}")
                # print(f"pc = {p_c}")
                accept = False
                while id < len(p) - 1 and p[id + 1] == "*":
                    if c != p_c and p_c != ".":
                        ptrs[j] += 2
                        id = ptrs[j]
                        if id == len(p): break
                        p_c = p[id]
                    else: # match 
                        new_ptrs += [id]
                        ptrs[j] += 2
                        id = ptrs[j]
                        if id == len(p): break
                        p_c = p[id]
                        accept = True
                
                if ptrs[j] == len(p): 
                    if accept:
                        ptrs[j] = -1 
                    else: ptrs[j] = -2
                else:
                    if c == p_c or p_c == ".": # match 
                        if accept:
                            new_ptrs += [id]
                        ptrs[j] += 1
                    else: 
                        if not accept: 
                            ptrs[j] = -2
                    # while c == p_c or p_c == ".": 
                    #     if id < len(p) - 1 and p[id + 1] == "*":
                    #         new_ptrs += [id]
                    #         ptrs[j] += 2
                    #         id = ptrs[j]
                    #         if id == len(p): break
                    #         p_c = p[id]
                    #     else:
                    #         ptrs[j] += 1 
                    #         break
                    #     import pdb 
                    #     pdb.set_trace()
                    # else: 
                    #     ptrs[j] = -2
            
                    if ptrs[j] == len(p): 
                        ptrs[j] = -1 
                # print(ptrs)
                # print(new_ptrs)
            ptrs += new_ptrs
            # if p[-1] == "*": 
            #     if i == len(s) - 1 and len(p) - 2 in ptrs: return True
            # else:
            if True:
                if i == len(s) - 1: 
                    if -1 in ptrs: 
                        return True
                    idx = -1
                    while -idx < len(p) and p[idx] == "*": 
                        tmp = len(p) + idx - 1
                        if tmp in ptrs:
                            return True
                        idx -= 2
                
            # print(ptrs)
            ptrs = list(filter(lambda x: x >= 0, ptrs))
        
        return False
    
if __name__ == "__main__": 
    test_case = ("aab", "c*a*b")
    # ("aa", "a*")
    # ("bbab", "b*a*")
    # ("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*")
    # ("aaa", "ab*a*c*a")
    #("mississippi", "mis*is*p*.")
    ret = Solution().isMatch(*test_case)
    print(ret)