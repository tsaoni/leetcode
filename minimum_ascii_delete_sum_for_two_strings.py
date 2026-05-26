class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        N, M = len(s1), len(s2)
        dp = [0] 
        acc = 0 
        for i in range(M): 
            acc += ord(s2[i])
            dp.append(acc)
        acc = 0
        for i in range(N): 
            _dp = [0] * (M + 1)
            acc += ord(s1[i])
            _dp[0] = acc
            for j in range(1, M + 1): 
                _dp[j] = min(dp[j] + ord(s1[i]), _dp[j - 1] + ord(s2[j - 1]))
                if s1[i] == s2[j - 1]: 
                    _dp[j] = min(_dp[j], dp[j - 1])
            dp = _dp
            # print(dp)
        return dp[-1]
    
if __name__ == "__main__": 
    s1 = "sea"
    s2 = "eat"
    # s1 = "delete"
    # s2 = "leet"
    ret = Solution().minimumDeleteSum(s1, s2)
    print(ret)