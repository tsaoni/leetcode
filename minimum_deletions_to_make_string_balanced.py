class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0, 0]
        accb = [0, 0]
        N = len(s)
        i = 0
        while i < N and s[i] == 'a': 
            i += 1 
        while i < N:
            bi = i
            while i < N and s[i] == 'b': 
                i += 1 
            _i = i
            while i < N and s[i] == 'a': 
                i += 1 
            if _i > bi and i > _i: 
                _dp = [0, 0]
                _accb = [0, 0]
                na, nb = i - _i, _i - bi
                if dp[0] < dp[1]: 
                    _dp[0] = dp[0] + na 
                    _accb[0] = accb[0] + nb 
                else: 
                    _dp[0] = dp[1] + na 
                    _accb[0] = accb[1] + nb

                if accb[0] < accb[1]: 
                    _dp[1] = (dp[1] + accb[0] + nb)
                    _accb[1] = 0
                else: 
                    _dp[1] = (dp[1] + accb[1] + nb)
                    _accb[1] = 0
                dp = _dp 
                accb = _accb
        # print(dp)
        return min(dp)
    
if __name__ == "__main__": 
    s = "aababbab"
    s = "bbaaaaabb"
    # s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
    ret = Solution().minimumDeletions(s)
    print(ret)