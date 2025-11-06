class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stk = []
        N = len(s)
        i = 0
        ret = 0
        while i < N: 
            while i < N and s[i] in ['a', 'b']: 
                if len(stk) > 0: 
                    if x >= y and stk[-1] == 'a' and s[i] == 'b': 
                        stk.pop(-1)
                        ret += x 
                    elif x <= y and stk[-1] == 'b' and s[i] == 'a': 
                        stk.pop(-1)
                        ret += y
                    else: 
                        stk.append(s[i])
                else: 
                    stk.append(s[i])
                i += 1
            idx = len(stk) - 2
            while idx >= 0 and len(stk) > 1: 
                if stk[idx] == 'a' and stk[idx + 1] == 'b': 
                    ret += x 
                    for _ in range(2):
                        stk.pop(idx)
                elif stk[idx] == 'b' and stk[idx + 1] == 'a': 
                    ret += y 
                    for _ in range(2):
                        stk.pop(idx)
                if idx == len(stk): 
                    idx -= 1
                idx -= 1
            stk = []
            i += 1
        return ret
    
if __name__ == "__main__": 
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    s = "aabbaaxybbaabb"
    x = 5
    y = 4
    ret = Solution().maximumGain(s, x, y)
    print(ret)