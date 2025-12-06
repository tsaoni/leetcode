class Solution:
    def numSub(self, s: str) -> int:
        mode = 0 
        cnt = 0
        ret = 0
        modulo = 10 ** 9 + 7
        f = lambda x: x % modulo
        for c in s: 
            if c == "0": 
                if mode == 1: 
                    ret += f(((1 + cnt) * (cnt)) // 2) 
                    ret = f(ret)
                    cnt = 0 
                    mode = 0
            else: 
                mode = 1
                cnt += 1
        ret += f(((1 + cnt) * (cnt)) // 2) 
        ret = f(ret)
        return ret
    
if __name__ == "__main__": 
    s = "0110111"
    s = "101"
    s = "111111"
    ret = Solution().numSub(s)
    print(ret)