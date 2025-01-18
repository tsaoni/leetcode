class Solution:
    def longestPalindrome(self, s: str) -> str:
        active_lst = []
        stack_lst = []
        full_res_lst = []
        def detect_fn(x):
            ret = []
            if len(x) == 1: return []
            if x[-1] == x[-2]: 
                ret += [x[-2:]]
            if len(x) > 2 and x[-1] == x[-3]: 
                ret += [x[-3:]]
            return ret
        for s_i in range(len(s)): 
            # update old 
            for i in range(len(active_lst)): 
                if active_lst[i]: 
                    if len(stack_lst[i]) == 0: 
                        active_lst[i] = 0
                    elif stack_lst[i][-1] == s[s_i]: # match top
                        stack_lst[i] = stack_lst[i][:-1]
                        full_res_lst[i] = f"{s[s_i]}{full_res_lst[i]}{s[s_i]}"
                    else: 
                        active_lst[i] = 0
            # detect new palindromic
            tmp = detect_fn(s[: s_i + 1])
            for item in tmp:
                active_lst += [1]
                stack_lst += [s[: s_i + 1 -len(item)]]
                full_res_lst += [item]
        
        # if no palindrome..
        if len(active_lst) == 0: 
            return s[0]
        lengths = [len(x) for x in full_res_lst]
        max_idx = lengths.index(max(lengths))
        return full_res_lst[max_idx]
    
if __name__ == "__main__": 
    test_case = "babad"
    ret = Solution().longestPalindrome(test_case)
    print(ret)