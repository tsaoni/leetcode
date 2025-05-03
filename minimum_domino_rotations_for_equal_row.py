from typing import List
from collections import Counter

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        cands = set((tops[0], bottoms[0]))
        d = Counter()
        N = len(tops)
        d[tops[0], 0] = 0
        d[bottoms[0], 1] = 0
        nfc = int(tops[0] == bottoms[0]) # count of non-flips
        if nfc == 0: 
            d[tops[0], 0] += 1
            d[bottoms[0], 1] += 1
        
        for t, b in zip(tops[1:], bottoms[1:]): 
            if t == b: 
                cur = {t: -1}
                nfc += 1
            else: 
                cur = {t: 0, b: 1}
            
            s = cands & set((t, b))
            tmp = Counter()
            def dfind(d, v): 
                return [(k1, k2) for k1, k2 in d.keys() if k1 == v]
            if len(s) > 0: 
                for c in s: 
                    tk = dfind(d, c)[0]
                    if cur[c] == tk[1]:
                        tmp[c, tk[1]] = d[tk] + 1 
                    else: 
                        tmp[c, tk[1]] = d[tk]
                d = tmp
                cands = s
            else: 
                return -1 

        # print(d, N, nfc)
        return min([min(N - nfc - v, v) for k, v in d.items()])
    
if __name__ == "__main__": 
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]

    # tops = [3,5,1,2,3]
    # bottoms = [3,6,3,3,4]

    # tops = [1,4,1,6,6,1,6,2] 
    # bottoms = [2,2,5,3,1,5,6,6]

    ret = Solution().minDominoRotations(tops, bottoms)
    print(ret)