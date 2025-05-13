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
    
if __name__ == "__main__": 
    s = "abcyy"
    t = 2

    s = "azbk"
    t = 1

    # s = "a"
    # t = 54

    # s = "jqktcurgdvlibczdsvnsg" 
    # t = 7517
    ret = Solution().lengthAfterTransformations(s, t)
    print(ret)