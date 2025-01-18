from collections import defaultdict

class Solution:
    def minimumLength(self, s: str) -> int:
        d = defaultdict(int)
        for c in s: 
            d[c] += 1 
        ret = len(s)
        for c, n in d.items(): 
            # print(c)
            # print(int((n - 1) / 2))
            # n - 2 * x > 1
            # (n - 1) / 2 > x
            ret -= int((n - 1) / 2) * 2
        return ret
    
if __name__ == "__main__": 
    s = "abaacbcbb"
    test_case = (s, )
    ret = Solution().minimumLength(*test_case)
    print(ret)