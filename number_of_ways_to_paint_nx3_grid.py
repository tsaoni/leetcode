class Solution:
    def numOfWays(self, n: int) -> int:
        states = [[0], [1], [2]]
        for _ in range(2): 
            _states = [] 
            for i in range(3): 
                for s in states: 
                    if s[-1] != i: 
                        _states.append(s + [i]) 
            states = _states 
        
        # print(states)
        N = len(states)
        dp = [1] * N 
        # s_idxs = {}
        # for i in range(N): 
        #     s_idxs[tuple(states[i])] = i 
        modulo = 10 ** 9 + 7
        for _ in range(n - 1): 
            _dp = [0] * N 
            for src in range(N): 
                for dst in range(N): 
                    ps = True 
                    for i in range(3): 
                        if states[src][i] == states[dst][i]: 
                            ps = False 
                            break 
                    if ps: 
                        _dp[dst] += dp[src]
                        _dp[dst] %= modulo
            dp = _dp 
        
        return sum(dp) % modulo
    
if __name__ == "__main__": 
    n = 1
    n = 5000
    ret = Solution().numOfWays(n)
    print(ret)