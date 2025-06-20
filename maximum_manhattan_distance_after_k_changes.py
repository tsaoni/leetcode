class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ds = ["ES", "EN", "WS", "WN"]
        ret = 0
        for d in ds: 
            prefix = [0] * len(s)
            peak = 0 
            _k = k
            def dist(v, l): 
                return 2 * v - l
            for i, c in enumerate(s): 
                prefix[i] += prefix[i - 1]
                if c in d: 
                    prefix[i] += 1 
                else: 
                    if _k > 0: 
                        prefix[i] += 1 
                        _k -= 1 
                if dist(prefix[i], i + 1) >= dist(prefix[peak], peak + 1): 
                    peak = i 
            # tmp = k - (peak + 1 - prefix[peak]) 
            # if tmp > 0: 
            #     _ret = dist(prefix[peak], peak + 1) + 2 * (peak + 1 - prefix[peak])
            #     idx = peak + 1
            #     # import pdb 
            #     # pdb.set_trace()
            #     while idx < len(s): 
            #         if s[idx] not in d: 
            #             if tmp == 0: 
            #                 break
            #             tmp -= 1 
            #         _ret += 1
            #         idx += 1
            #     ret = max(_ret, ret)
            #     # print(ret)
            # else: 
            # ret = max(ret, dist(prefix[peak], peak + 1) + 2 * k)
            # print(d, prefix, peak)
            ret = max(ret, dist(prefix[peak], peak + 1))

        return ret 
    
if __name__ == "__main__": 
    s = "NWSE"
    k = 1
    s = "NSWWEW"
    k = 3
    # s = "NW"
    # k = 2
    s = "WSNS" 
    k = 1
    s = "NNNSSEWNN" 
    k = 2
    ret = Solution().maxDistance(s, k)
    print(ret)