class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        prev = None 
        cnt = 0 
        cnts = []
        modulo = 10 ** 9 + 7
        for c in word: 
            if prev is not None and c != prev: 
                cnts.append(cnt)
                cnt = 0 
            prev = c
            cnt += 1
        cnts.append(cnt)
        # print(cnts)
        Nc = len(cnts)
        total = 1
        for c in cnts: 
            total *= (c % modulo) 
            total %= modulo
        # print(total)
        if Nc >= k: # add the line wtf
            return total
        dp = [[1] * k] + [[0] * (k) for _ in range(Nc)]
        
        m = Nc + 1
        for i in range(1, Nc + 1): 
            prefixes = [0] * (k) 
            prefixes[0] = dp[(i - 1) % m][0]
            for l in range(k - 1): 
                prefixes[l + 1] = prefixes[l] + dp[(i - 1) % m][l + 1]
                prefixes[l + 1] %= modulo
                dp[i % m][l + 1] = prefixes[l] - (prefixes[l - cnts[i - 1]] if l - cnts[i - 1] >= 0 else 0)
                dp[i % m][l + 1] = (dp[i % m][l + 1] + modulo) % modulo
            
                # for j in range(1, cnts[i - 1] + 1): 
                #     if l + 1 - j >= 0:
                #         dp[i][l + 1] += dp[i - 1][l + 1 - j] 
                #         dp[i][l + 1] %= modulo
                # print(l)
                # print("p", prefixes)
                # print(dp[i - 1])
                # print(dp[i])
        
        # print(dp)
        ret = total - dp[Nc % m][-1]
        return (ret + modulo) % modulo
    
if __name__ == "__main__": 
    word = "aabbccdd"
    k = 7
    # word = "aabbccdd"
    # k = 8
    word = "aaabbb"
    k = 3
    word = "vtkk" 
    k = 3
    ret = Solution().possibleStringCount(word, k)
    print(ret)