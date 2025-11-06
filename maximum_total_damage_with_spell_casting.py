from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        from collections import Counter
        n = len(power)
        cands = sorted(power)
        s = list(sorted(set(cands)))
        dp = [[0, 0] for _ in range(len(s))]
        i, di = 0, 0 
        # print(cands)
        # print(s)
        while i < n: 
            cnt = 1 
            _i = i
            while _i + 1 < n and cands[_i + 1] == cands[_i]: 
                cnt += 1 
                _i += 1

            # print(i, di)
            x = cnt * s[di]
            _tmp = x
            if di > 0 and s[di] - s[di - 1] > 2: 
                _tmp = max(_tmp, x + dp[di - 1][1])
            if di > 1 and s[di] - s[di - 2] > 2: 
                _tmp = max(_tmp, x + dp[di - 2][1])
            if di > 2: 
                _tmp = max(_tmp, x + dp[di - 3][1])
            dp[di][0] = _tmp
            dp[di][1] = max(dp[di - 1][1], dp[di][0])

            i = _i + 1
            di += 1
        # print(dp)
        return dp[-1][1]
    
if __name__ == "__main__": 
    power = [1,1,3,4]
    power = [7,1,6,6]
    power = [3,4,8,10,8,8,3]
    ret = Solution().maximumTotalDamage(power)
    print(ret)