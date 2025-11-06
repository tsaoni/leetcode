class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        N = len(s)
        def dshift(s, x): 
            _s = ""
            for i, c in enumerate(s): 
                if i & 1 == 1:
                    _s += str((int(c) + x) % 10)
                else: 
                    _s += c
            return _s 
        
        def cshift(s, x): 
            return s[-x:] + s[: -x]
        
        cands = set()
        for i in range(10):
                cands.add(dshift(s, i * a))
        if not(N & 1 == 0 and b & 1 == 0): 
            _cands = set()
            for s in cands:
                _s = cshift(s, b)
                for i in range(10):
                    _cands.add(dshift(_s, i * a))
            cands |= _cands
        # print(cands)
        ret = ""
        for c in cands: 
            _s = c 
            while True: 
                ret = min(ret, _s) if ret else _s
                # print(_s, b)
                _s = cshift(_s, b)
                if _s == c: 
                    break 

        return ret
    
if __name__ == "__main__": 
    s = "5525"
    a = 9
    b = 2
    # s = "74"
    # a = 5
    # b = 1
    s = "0011"
    a = 4
    b = 2
    s = "43987654"
    a = 7 
    b = 3
    ret = Solution().findLexSmallestString(s, a, b)
    print(ret)