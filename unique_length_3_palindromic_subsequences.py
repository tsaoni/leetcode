class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lpos = [[] for _ in range(26)] 
        for i, c in enumerate(s): 
            pos = ord(c) - ord('a')
            lpos[pos].append(i)
        
        def search(lst, n): 
            l, r = 0, len(lst) - 1 
            while l < r: 
                mid = (l + r + 1) // 2 
                if lst[mid] < n: 
                    l = mid 
                else: 
                    r = mid - 1  
            return l if lst[l] < n else -1
        ret = 0
        for fst in range(26): 
            for mid in range(26): 
                if fst == mid: 
                    if len(lpos[fst]) > 2: 
                        ret += 1 
                elif len(lpos[fst]) > 1 and len(lpos[mid]) > 0: 
                    l, r = lpos[fst][0], lpos[fst][-1]
                    li, ri = search(lpos[mid], l), search(lpos[mid], r)
                    if li + 1 <= ri: 
                        ret += 1 
                    # x = chr(ord('a') + fst) + chr(ord('a') + mid) + chr(ord('a') + fst)
                    # print(x)
              
        return ret
    
if __name__ == "__main__": 
    s = "aabca"
    s = "adc"
    s = "bbcbaba"
    ret = Solution().countPalindromicSubsequence(s)
    print(ret)