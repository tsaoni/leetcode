class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def str2int(s): 
            s = s.ljust(50, '0')
            return int(s, 2)
        def move(i, h): 
            priority = []
            cands = []
            ret = ""
            while i < len(s): 
                if s[i] == '1': 
                    _i, _s = move(i + 1, h + 1)
                    if _i < len(s):
                        _s = "1" + _s + "0"
                        cands.append(_s)
                        i = _i + 1
                        priority.append((str2int(_s), len(priority)))
                    else: 
                        ret = "1" + _s
                        i = _i 
                else: 
                    break 

            priority.sort(key=lambda x: -x[0])
            _s = ""
            for _, idx in priority: 
                _s += cands[idx]
            ret = _s + ret
            return i, ret

        
        _, ret = move(0, 0)
        return ret 
    
if __name__ == "__main__": 
    s = "11011000"
    s = "10"
    ret = Solution().makeLargestSpecial(s)
    print(ret)