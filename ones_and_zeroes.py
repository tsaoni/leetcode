from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        ret = 0
        # cur = {(0, 0)}
        for s in strs: 
            zc, oc = 0, 0 
            for c in s: 
                if c == "0": 
                    zc += 1 
                else: 
                    oc += 1 
            
            _cur = set()
            # _dp = [[0] * (n + 1) for i in range(m + 1)]
            # for i, j in cur:
            for i in range(m, -1, -1): 
                for j in range(n, -1, -1):
                    if i - zc >= 0 and j - oc >= 0: 
                        dp[i][j] = max(dp[i - zc][j - oc] + 1, dp[i][j])
                        ret = max(ret, dp[i][j])
                    # print(s, ret)
                    # _cur.add((i + zc, j + oc))
            # cur |= _cur
            # dp = _dp
                
        return ret
    
if __name__ == "__main__": 
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3
    strs = ["10","0","1"]
    m = 1
    n = 1
    # strs = ["0","1101","01","00111","1","10010","0","0","00","1","11","0011"] 
    # m = 63 
    # n = 36
    ret = Solution().findMaxForm(strs, m, n)
    print(ret)