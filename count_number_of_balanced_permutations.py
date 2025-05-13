from collections import Counter
import math
from itertools import accumulate
from copy import deepcopy

class Solution:
    def countBalancedPermutations1(self, num: str) -> int:
        nums = [int(c) for c in num]
        total = sum(nums)
        modulo = 10 ** 9 + 7
        if total % 2 == 1: 
            return 0 
        else: 
            W = total // 2 
            even_d = len(num) // 2
            odd_d = len(num) - even_d
            freq = Counter()
            for c in nums: 
                freq[c] += 1 
            acc_freq = list(accumulate([freq[i] for i in range(10)]))
            
            dp = [[[0] * (odd_d + 1) for _ in range(W + 1)] for _ in range(10)]
            # for i in range(10): 
            #     dp[i][0][0] = 1 
    
            for i in range(odd_d + 1): 
                dp[0][0][i] = 1
            
            # dp[0][0][0] = 1
            for d in range(10): 
                for w in range(W + 1): 
                    for i in range(freq[d] + 1):
                        for j in range(min(odd_d + 1, acc_freq[d] + 1)): 
                            if j - i >= 0 and w - i * d >= 0:
                                even_cur = acc_freq[d] - j #even_d - ((acc_freq[d] - j) - (freq[d] - i))
                                # if even_cur >= 0: 
                                dp[d][w][j] += math.comb(even_cur, freq[d] - i) * math.comb(j, i) * dp[d - 1][w - i * d][j - i]
                                # print(d, w, j)
               
        # print(acc_freq)
        # print(dp)                   
        return dp[-1][-1][-1] % modulo
    
    def countBalancedPermutations2(self, num: str) -> int:
        """
        example from tutorial
        """
        from math import comb 
        from functools import cache
        MOD = 10**9 + 7
        num = list(map(int, num))
        tot = sum(num)
        if tot % 2 != 0:
            return 0
        target = tot // 2
        cnt = Counter(num)
        n = len(num)
        maxOdd = (n + 1) // 2
        psum = [0] * 11
        for i in range(9, -1, -1):
            psum[i] = psum[i + 1] + cnt[i]

        @cache
        def dfs(pos, curr, oddCnt):
            # If the remaining positions cannot complete a legal placement, or the sum of the elements in the current odd positions is greater than the target value
            if oddCnt < 0 or psum[pos] < oddCnt or curr > target:
                return 0
            if pos > 9:
                return int(curr == target and oddCnt == 0)
            evenCnt = (
                psum[pos] - oddCnt
            )  # Even-numbered positions remaining to be filled
            res = 0
            for i in range(
                max(0, cnt[pos] - evenCnt), min(cnt[pos], oddCnt) + 1
            ):
                # Place i of the current number at odd positions, and cnt[pos] - i at even positions
                ways = comb(oddCnt, i) * comb(evenCnt, cnt[pos] - i) #% MOD
                res += ways * dfs(pos + 1, curr + i * pos, oddCnt - i)
            return res #% MOD

        return dfs(0, 0, maxOdd)

    def countBalancedPermutations(self, num: str) -> int:
        """
        will results in TLE
        """
        nums = [int(c) for c in num]
        total = sum(nums)
        if total % 2 == 1: 
            return 0 
        else: 
            W = total // 2 
            even_d = len(num) // 2
            freq = Counter()
            for c in nums: 
                freq[c] += 1 
            dp = [[[] for _ in range(W + 1)] for _ in range(even_d)]
            for d in range(even_d): 
                for w in range(W + 1): 
                    if d == 0: 
                        if w in freq: 
                            dp[d][w].append(Counter())
                            dp[d][w][0][w] += 1
                    else:
                        for i, cnt in freq.items(): 
                            if w - i >= 0:
                                for r in dp[d - 1][w - i]: 
                                    if r[i] < cnt: 
                                        x = deepcopy(r)
                                        x[i] += 1 
                                        if x not in dp[d][w]:
                                            dp[d][w].append(x)
            # compute permutations
            def perm(d, f): 
                b = 1
                total = 0
                for _, c in d.items(): 
                    b *= math.factorial(c)
                    # total += c 
                # return math.factorial(total) // b
                return f // b
            
    
            # print(dp[even_d - 1][W])
            ret = 0
            modulo = 10 ** 9 + 7
            even_f = math.factorial(even_d)
            odd_f = math.factorial(len(num) - even_d)
            for r in dp[even_d - 1][W]: 
                even_d = r 
                odd_d = Counter()
                for i, cnt in freq.items(): 
                    odd_d[i] = cnt - even_d[i]
                ret += (perm(even_d, f=even_f) % modulo) * (perm(odd_d, f=odd_f) % modulo)
                ret %= modulo
               
        return ret
    
if __name__ == "__main__": 
    num = "123"
    # num = "112"
    # num = "12345"
    # num = "4567"
    num = "409871932342390718772"
    num = "49871932342397187720"
    # num = "004567121"
    # num = "325419"
    # num = "00000000000000000000000000000000000000000000000000000000000000000000000000000000"
    ret = Solution().countBalancedPermutations2(num)
    print(ret)