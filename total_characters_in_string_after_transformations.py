from typing import List

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        cnt = [[0, 0] for _ in range(t + 1)]
        modulo = 10 ** 9 + 7
        cnt[0] = [1, 1]
        # for i in range(min(26, t + 1)): 
        #     cnt[i] = [1, 1]
        for i in range(t + 1): 
            # cnt[i][0] += cnt[i - 1][0]
            # cnt[i][1] += cnt[i - 1][0]
            if i + 26 < t + 1:
                cnt[i + 26][0] += cnt[i][0]
                cnt[i + 26][1] += cnt[i][0]
                cnt[i + 26][0] %= modulo 
                cnt[i + 26][1] %= modulo
            if i + 25 < t + 1:
                cnt[i + 25][0] += cnt[i][1]
                cnt[i + 25][1] += cnt[i][1]
                cnt[i + 25][0] %= modulo 
                cnt[i + 25][1] %= modulo

        # print([(i, c) for i, c in enumerate(cnt)])
        # print()
        cnt[0][0] = 2
        for i in range(1, t + 1): 
            cnt[i][0] += cnt[i - 1][0]
            # cnt[i][1] += cnt[i - 1][1]

        # print([(i, c) for i, c in enumerate(cnt)])
        ret = 0
        for c in s: 
            tmp = t - (ord('z') - ord(c)) - 1
            if tmp >= 0: 
                ret += cnt[tmp][0] #sum(cnt[tmp]) 
            else: 
                ret += 1 
            ret %= modulo
            # print(tmp, ret)
        return ret
    
    def lengthAfterTransformations_1(self, s: str, t: int, nums: List[int]) -> int:
        import string 
    

        M = [[0] * 26 for _ in range(26)]
        x = [0] * 26 
        modulo = 10 ** 9 + 7
        for c in s: 
            idx = ord(c) - ord('a')
            x[idx] += 1 
        for c in string.ascii_lowercase:
            idx = ord(c) - ord('a')
            for i in range(idx + 1, idx + nums[idx] + 1):
                M[i % 26][idx] = 1
        
        def mul(M, x): 
            return [sum([a * b % modulo for a, b in zip(r, x)]) for r in M]
        
        def emul(M, n): 
            def mmul(m1, m2): 
                ret = []
                k = len(m2)
                for r in m1: 
                    ret.append([])
                    for c in zip(*m2): 
                        e = sum([a * b % modulo for a, b in zip(r, c)]) % modulo
                        ret[-1].append(e)
                return ret 
            
            d = len(M)
            ret = [[0] * d for _ in range(d)]
            for i in range(d): 
                ret[i][i] = 1 
            
            while n > 0: 
                if n & 1: 
                    ret = mmul(M, ret)
                M = mmul(M, M)
                n //= 2
            return ret

        # for _ in range(t): 
        #     x = mul(M, x)

        M = emul(M, t)
        x = mul(M, x)

        return sum(x) % modulo

if __name__ == "__main__": 
    s = "abcyy"
    t = 2

    s = "azbk"
    t = 1

    # s = "a"
    # t = 54

    # s = "jqktcurgdvlibczdsvnsg" 
    # t = 7517

    s = "abcyy"
    t = 2
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]

    # s = "azbk"
    # t = 1
    # nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ret = Solution().lengthAfterTransformations_1(s, t, nums)
    print(ret)