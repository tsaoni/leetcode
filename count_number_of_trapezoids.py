from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter
        cnt = Counter()
        # N = len(points)
        modulo = 10 ** 9 + 7
        for x, y in points: 
            cnt[y] += 1 
        ret = 0 
        c2 = lambda x: x * (x - 1) // 2
        tot = 0
        for x, c in cnt.items(): 
            cnt[x] = c2(c) 
            tot += cnt[x]
        for _, c in cnt.items(): 
            tot -= c
            ret += tot * c
            ret %= modulo
        return ret 
    
    def countTrapezoids_2(self, points: List[List[int]]) -> int:
        ht = {}
        tries = {}
        N = len(points)

        from math import gcd

        def slope_and_mid(p1, p2):
            x1, y1 = p1
            x2, y2 = p2

            dy = y2 - y1
            dx = x2 - x1

            # Handle vertical line
            if dx == 0:
                # slope is "infinite" but we represent it as (1, 0)
                slope = (1, 0)
                # line eq: x = x1  -> C = x1
                C = x1
                return slope, C

            # Normalize slope
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            # Normalize sign convention: dx > 0 OR dx == 0 and dy > 0
            if dx < 0:
                dx = -dx
                dy = -dy

            slope = (dy, dx)

            # Line offset C = dxy - dyx
            C = dx * y1 - dy * x1

            # Normalize C with slope to ensure full uniqueness
            # (if desired we can normalize by gcd of slope+offset, but usually not needed)
            return slope, C

        def _slope_and_mid(p1, p2): 
            if p2[0] - p1[0] == 0: 
                a = float("inf")
                b = p1[0]
            else:
                a = (p2[1] - p1[1]) / (p2[0] - p1[0])
                # _a = (p2[1] - p1[1]) / (p2[0] - p1[0])
                b = p2[1] - a * p2[0]
            return a, b 
        def is_exist(p): 
            i = 0 
            cur = tries
            ex = True
            while i < len(p): 
                if p[i] in cur: 
                    cur = cur[p[i]]
                else: 
                    cur[p[i]] = {}
                    cur = cur[p[i]]
                    ex = False
                i += 1 
            return ex 
        
        ret = 0
        for i in range(N): 
            for j in range(i + 1, N): 
                a, b = slope_and_mid(points[i], points[j])
                # if i == 0 and j == 2: 
                #     import pdb 
                #     pdb.set_trace()
                if a in ht:
                    for _b, st in ht[a].items(): 
                        # print(b, _b, points[i], points[j], st)
                        if b != _b: 
                            for ps in st: 
                                p = sorted([i, j, *ps])
                                if len(set(p)) < 4: 
                                    continue
                                    # for x in p: 
                                    #     print(points[x])
                                    # import pdb 
                                    # pdb.set_trace()
                                # print(p)
                                if not is_exist(p): 
                                    ret += 1 
                else: 
                    ht[a] = {}
                if b in ht[a]: 
                    ht[a][b].add((i, j))
                else: 
                    ht[a][b] = set({(i, j)})
        # print(tries)
        # print(ht)
        return ret 
    
if __name__ == "__main__": 
    points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]
    points = [[0,0],[1,0],[0,1],[2,1]]
    points = [[96,75],[12,32],[96,32],[12,-53],[12,-24]]
    points = [[0,0],[1,0],[0,1],[1,1],[2,0],[2,1]]
    points = [[-80,-47],[-37,52],[-23,75],[-44,-66],[-33,-61],[-80,94],[-38,3],[16,-43],[-38,2],[2,99],[-65,-20],[37,15],[45,2],[21,66],[76,-20],[-84,-43],[-80,-66],[-96,2]]
    points = [[285,391],[-156,29],[-158,-5],[-153,-9],[-79,249],[-133,-378],[436,50],[298,336],[-318,-378],[-29,-266],[-435,278],[-381,313],[-29,399],[-96,110],[260,-48],[342,-128],[491,-295],[58,177],[-125,385],[266,-267],[-435,308],[-296,-89],[260,-128],[-29,-447],[-78,316],[132,135],[-245,84],[436,-183],[-155,-297],[-209,-153],[-46,339],[-155,-233],[132,391],[55,308],[-259,-150],[436,27],[55,198],[-291,-146],[101,119],[465,136],[260,39],[-37,-492],[57,-476],[-295,167],[262,-89],[373,-210],[-114,-267],[-209,356],[-153,-192],[373,302],[368,-194],[-268,105],[-322,-95],[-435,-445],[113,126],[206,399],[441,302],[-435,-424],[379,-457],[-377,-65],[-329,-199],[47,308],[368,336],[-442,-476],[-29,316],[-5,200],[254,-260],[294,-160],[260,125],[436,-113],[34,231],[-94,-303],[-322,355],[339,-101],[-133,-102],[24,-146],[296,203],[-435,-413],[260,146],[-454,-146],[-29,-283],[355,-492],[185,216],[-120,-57],[436,-431],[20,167],[-450,-48],[465,-267],[396,-101],[355,-465],[118,336],[-245,-427],[-148,-98],[-435,126],[-435,-301],[379,-334],[296,-460],[-337,39],[86,224],[-435,-27],[-64,-166],[57,-166],[-347,278],[-499,391],[-435,220],[-29,-71],[-29,167],[373,146],[-435,348],[-79,-255],[345,-492],[-262,-301],[-246,-457],[-435,302],[-330,-127],[379,278],[-435,-153],[-222,-427],[-159,-151],[454,9],[296,356],[-346,50],[-322,-57],[-154,302],[-435,142],[-125,356],[-90,167],[-337,308],[195,391],[-435,105],[-322,-27],[-347,-127],[-353,348],[-156,-160],[436,380],[-135,299],[495,167],[-262,-160],[-159,308],[380,-281],[-267,146],[-291,-303],[379,120],[-245,-153],[171,36],[260,-463],[-435,-110],[379,-24],[-6,-287],[-435,-220],[55,391],[-268,-308],[2,-57],[42,336],[273,360],[320,356],[-426,-297],[-260,391],[-381,-27],[-482,308],[436,-89],[407,287],[-156,36],[-304,-9],[-358,203],[-313,391],[236,304],[72,482],[-29,287],[-435,-78],[383,39]]
    ret = Solution().countTrapezoids_2(points)
    print(ret)