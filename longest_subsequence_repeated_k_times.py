class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str | bool:
        from collections import Counter
        cnt = Counter()
        for c in s: 
            cnt[c] += 1
        lst = []
        for c in s: 
            if cnt[c] >= k: 
                lst.append(c)
        s = "".join(lst)
        N = len(s)
        max_l = N // k
        def find_all_seqs(start, end, l, root=True): 
            if l == 0: 
                return {""}
            if start == end: 
                return set()
            
            seen = set()
            seqs = set()
            for i in range(start, end): 
                if s[i] not in seen: 
                    tmp = find_all_seqs(i + 1, end, l - 1, False)
                    for ss in tmp: 
                        seqs.add(s[i] + ss)
                    seen.add(s[i])
            return sorted(seqs, reverse=True) if root else seqs

        # import pdb 
        # pdb.set_trace()
        def match_end_idx(start, ss): 
            idx = start 
            i = 0
            while idx < N and i < len(ss): 
                if s[idx] == ss[i]: 
                    i += 1 
                idx += 1 
            return idx if i == len(ss) else -1
        def check_match(cur_k, start, s_match): 
            if cur_k > k: 
                return True
            elif cur_k == 1: 
                for l in range(max_l, 0, -1): 
                    end = N - l * (k - 1)
                    seqs = find_all_seqs(start, end, l)
                    for ss in seqs:
                        end_idx = match_end_idx(start, ss)
                        is_match = check_match(cur_k + 1, end_idx, ss)
                        if is_match: 
                            return ss
                return "" 
            else: 
                end_idx = match_end_idx(start, s_match)
                if end_idx < 0 or N - end_idx < (k - cur_k) * len(s_match): 
                    return False 
                else:
                    return check_match(cur_k + 1, end_idx, s_match)
        
        ret = check_match(1, 0, "")
        return ret
    
if __name__ == "__main__": 
    s = "letsleetcode"
    k = 2
    # s = "bb"
    # k = 2
    s = "ab"
    k = 2
    ret = Solution().longestSubsequenceRepeatedK(s, k)
    print(ret)