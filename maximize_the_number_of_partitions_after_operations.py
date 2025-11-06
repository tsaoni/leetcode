class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        N = len(s)
        left, right = [[0, 0, 0] for _ in range(N)], [[0, 0, 0] for _ in range(N)]
        char2idx = lambda c: ord(c) - ord("a")
        # split, mask, distinct
        ls, lm, ln = 0, 0, 0
        rs, rm, rn = 0, 0, 0
        for i in range(N): 
            left[i] = [ls, lm, ln]
            mk = 1 << char2idx(s[i])
            if lm & mk == 0: 
                lm |= mk
                ln += 1 
            if ln > k: 
                # if i > 1:
                left[i][0] += 1
                left[i][1], left[i][2] = 0, 0
                ls += 1 
                lm = mk 
                ln = 1

            ri = N - 1 - i 
            right[ri] = [rs, rm, rn]
            mk = 1 << char2idx(s[ri])
            if rm & mk == 0: 
                rm |= mk
                rn += 1 
            if rn > k: 
                # if ri + 1 < N - 1:
                right[ri][0] += 1
                right[ri][1], right[ri][2] = 0, 0
                rs += 1 
                rm = mk 
                rn = 1
        
        # print(left)
        # print(right)
        ret = left[-1][0]
        max_mk = 1 << 26 - 1
        for i in range(N): 
            mk = left[i][1] | right[i][1]
            cnt = 0
            while mk > 0: 
                cnt += mk & 1
                mk >>= 1
            if min(cnt + 1, 26) <= k: 
                x = 1 
            elif left[i][2] == k and right[i][2] == k and left[i][1] | right[i][1] < max_mk: 
                x = 3
            else: 
                x = 2
            ret = max(ret, left[i][0] + right[i][0] + x)
            # print(i, x)
        return ret
    
if __name__ == "__main__": 
    s = "accca"
    k = 2
    s = "aabaab"
    k = 3
    s = "xxyz"
    k = 1
    # s = "abbaaca" 
    # k = 2
    # s = "ghorzzjwaqhcaeibwxwedecgs" 
    # k = 1
    s = "tzaxomrbtieqpkduclsjhdyxonfwwbnbqgbvdxaqhbip" 
    k = 26
    ret = Solution().maxPartitionsAfterOperations(s, k)
    print(ret)