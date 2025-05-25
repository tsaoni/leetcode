from typing import List
from collections import defaultdict, Counter

class Solution: 
    def func(self): 
        modulo = 10 ** 9 + 7
        max_d = 50000
        max_odd = max_d if max_d & 1 else max_d - 1
        ret = 0
        u = max_d
        d = 1
        acc = (u // d)
        for i in range(1, max_odd + 1, 2): 
            print(i)
            ret += acc
            ret %= modulo
            u -= 2 
            d += 2
            acc = ((u * (u + 1) * acc) // (d * (d - 1)))
            acc %= modulo
            # import pdb 
            # pdb.set_trace()

        return 2 ** (max_d - 1) % modulo
       
    
    def sumOfLargestPrimes(self, s: str) -> int:
        import math
        def isPrime(n): 
            idx = 2 
            if n < 2: 
                return False
            while idx <= int(math.sqrt(n)): 
                if n % idx == 0: 
                    return False 
                idx += 1 
            return True
        
        def dlen(n): 
            d = 0 
            while n > 0:
                d += 1 
                n //= 10
            return d

        primes = []
        length = len(s)
        min_d = 10
        while length > 0: 
            for i in range(len(s) - length + 1): 
                ss = s[i: i + length]
                tmp = int(ss)
                # print(tmp)
                if isPrime(tmp): 
                    min_d = min(min_d, dlen(tmp))
                    primes.append(tmp)
                    primes = sorted(list(set(primes)))
            if len(primes) >= 3 and length <= min_d: 
                break
            length -= 1 

        # print(primes)
        return sum(primes[-3:])

    def maxSubstrings(self, word: str) -> int:
        from collections import defaultdict
        N = len(word)
        dp = [0] * (N + 1)
        hist = defaultdict(list)
        for i in range(N): 
            c = word[i]
            dp[i + 1] = dp[i]
            for j in range(len(hist[c]) - 1, -1, -1): 
                idx = hist[c][j]
                if (i + 1) - idx + 1 >= 4: 
                    dp[i + 1] = max(dp[idx - 1] + 1, dp[i])
                    # print(c, idx, dp[i + 1])
                    break
            # if c not in hist or (c in hist and (i + 1) - hist[c] + 1 < 4): 
            #     dp[i + 1] = dp[i]
            # else: 
            #     dp[i + 1] = max(dp[hist[c]] + 1, dp[i])

            hist[c].append(i + 1)
        # print(dp)
        return dp[-1]

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        modulo = 10 ** 9 + 7
        n = max([max(x) for x in edges])
        T = [[] for _ in range(n)] 
        for u, v in edges: 
            T[u - 1].append(v - 1)
            T[v - 1].append(u - 1)
        visited = [False] * n
        def dfs(u, depth): 
            tmp = depth
            visited[u] = True
            for v in T[u]: 
                if not visited[v]: 
                    tmp = max(dfs(v, depth + 1), tmp)
            return tmp
    
        max_d = dfs(0, 0)
        print(max_d)
        max_odd = max_d if max_d & 1 else max_d - 1
        ret = 0
        u = max_d
        d = 1
        acc = (u // d)
        #for i in range(1, max_odd + 1, 2): 
        while u > 0:
            ret += acc
            ret %= modulo
            u -= 2 
            d += 2
            acc = ((u * (u + 1) * acc) // (d * (d - 1)))
            # acc %= modulo
            # import pdb 
            # pdb.set_trace()

        return ret % modulo

if __name__ == "__main__": 
    # ret = Solution().sumOfLargestPrimes("50393")

    word = "abcdeafdef"
    # word = "bcdaaaab"
    word = "aaaeaaa"
    # word = "abcceaddba"
    # word = "abeaebddae"
    # ret = Solution().maxSubstrings(word)
    # print(ret)

    edges = [[1,2]]
    edges = [[1,2],[1,3],[3,4],[3,5]]
    edges = [[1,2],[2,3],[3,4]]
    ret = Solution().assignEdgeWeights(edges)
    print(ret)

