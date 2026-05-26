from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        import bisect
        hFences.sort()
        vFences.sort()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        hd = [hFences[i + 1] - hFences[i] for i in range(len(hFences) - 1)]
        vd = [vFences[i + 1] - vFences[i] for i in range(len(vFences) - 1)]
        hs = set()
        vs = set()
        for i in range(len(hd)): 
            h = hd[i]
            t = set()
            x = 0
            for _h in reversed(hd[: i]):
                x += _h 
                t.add(x + h)
            hs |= t
            hs.add(h)
        
        for i in range(len(vd)): 
            v = vd[i]
            t = set()
            x = 0
            for _v in reversed(vd[: i]): 
                x += _v
                t.add(x + v)
            vs |= t
            vs.add(v)
            # import pdb 
            # pdb.set_trace()

        ret = -1
        for h in hs: 
            if h in vs: 
                ret = max(ret, h)

        modulo = 10 ** 9 + 7
        return ret if ret < 0 else ((ret % modulo) ** 2) % modulo
    
        hs = sorted(hs, key=lambda x: -x)
        vs = sorted(vs, key=lambda x: -x)
        
        ret = 0
        # print(hd, vd)
        # print(hs, vs)
        while len(hs) > 0: 
            h = hs.pop(0)
            x = -1
            while len(vs) > 0 and vs[0] >= h: 
                x = vs.pop(0)
            if x == h: 
                ret = max(ret, h)
        
        modulo = 10 ** 9 + 7
        return -1 if ret == 0 else ((ret % modulo) ** 2) % modulo
    
if __name__ == "__main__": 
    m = 4
    n = 4
    hFences = [2]
    vFences = [2,3]
    ret = Solution().maximizeSquareArea(m, n, hFences, vFences)
    print(ret)