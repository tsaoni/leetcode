from typing import List

class Solution:
    def pyramidTransition_1(self, bottom: str, allowed: List[str]) -> bool:
        from collections import defaultdict 
        ht = defaultdict(list)
        for s in allowed: 
            ht[s[: 2]].append(s[2])
        def build(cur, nxt, idx): 
            if len(cur) == 1: 
                return True 

            if idx == len(cur) - 1: 
                cur = nxt 
                nxt = ""
                idx = 0 
                return build(cur, nxt, idx)
            else:
                x = cur[idx: idx + 2]
                if x in ht: 
                    for c in ht[x]: 
                        suc = build(cur, nxt + c, idx + 1)
                        if suc: 
                            return True 
                return False

        return build(bottom, "", 0)
    
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        unfinished... 
        """
        from collections import defaultdict 
        ht = defaultdict(list)
        for s in allowed: 
            ht[s[: 2]].append(s[2])
        existed = set()
        def build(cur, nxt, memo, ri): 
            # print("s", cur, nxt)
            if len(cur) == 1: 
                return True 

            idx = len(nxt)
            if idx == len(cur) - 1: 
                # print("1")
                memo.append(cur)
                cur = nxt 
                nxt = ""
                idx = 0 
                suc = build(cur, nxt, memo, idx)
                if len(memo): memo.pop(-1)
                return suc
            else:
                x = cur[idx: idx + 2]
                if x in ht: 
                    for c in ht[x][ri: ]: 
                        # print("2", c)
                        # import pdb 
                        # pdb.set_trace()
                        suc = build(cur, nxt + c, memo, 0)
                        if suc: 
                            return True 
                else: 
                    # print("3")
                    if len(memo) == 0: 
                        return False
                    # print(cur, nxt, memo)
                    c = cur[idx + 1]
                    nxt = cur[: idx + 1]
                    cur = memo.pop(-1)
                    # print(cur, nxt)
                    x = cur[idx + 1: idx + 3]
                    # if len(ht[x]) == 0: 
                    #     import pdb 
                    #     pdb.set_trace()
                    ri = ht[x].index(c)
                    return build(cur, nxt, memo, ri + 1)
                    # print(ht[x])
                    # import pdb 
                    # pdb.set_trace()
                    # for c in ht[x][ri + 1: ]: 
                    #     suc = build(cur, nxt + c, memo, len(nxt) + 1)
                    #     if suc: 
                    #         return True 
                    # import pdb 
                    # pdb.set_trace()
                return False

        return build(bottom, "", [], 0)
    
if __name__ == "__main__": 
    bottom = "BCD"
    allowed = ["BCC","CDE","CEA","FFF"]
    # bottom = "AAAA"
    # allowed = ["AAB","AAC","BCD","BBE","DEF"]
    bottom = "ABCD" 
    allowed = ["ABC","BCA","CDA","ABD","BCE","CDF","DEA","EFF","AFF"]
    bottom = "DAAAAD" 
    allowed = ["DAD","DAE","DAB","DAF","DAC","EAD","EAE","EAB","EAF","EAC","BAD","BAE","BAB","BAF","BAC","FAD","FAE","FAB","FAF","FAC","CAD","CAE","CAB","CAF","CAC","ADD","ADE","ADB","ADF","ADC","AED","AEE","AEB","AEF","AEC","ABD","ABE","ABB","ABF","ABC","AFD","AFE","AFB","AFF","AFC","ACD","ACE","ACB","ACF","ACC","AAD","AAE","AAB","AAF","AAC","AAA"]
    # bottom = "DADAD"
    ret = Solution().pyramidTransition_1(bottom, allowed)
    print(ret)