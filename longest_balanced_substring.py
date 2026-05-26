class Solution:
    def longestBalanced_1(self, s: str) -> int:
        N = len(s)
        acc, acc1, acc2 = 0, 0, 0
        xa, xb, xc = 0, 0, 0
        pa, pb, pc = [0], [0], [0]
        p1, p2, p3 = {}, {}, {}
        prev = {}
        ret = 0
        for i in range(N): 
            if s[i] == 'a': 
                acc -= 1 
                acc2 += 1
                pa.append(pa[-1] + 1)
                pb.append(pb[-1])
                pc.append(pc[-1])
                xa += 1 
                ret = max(ret, xa)
                xb = xc = 0
            elif s[i] == 'b': 
                acc += 1 
                acc1 -= 1
                pa.append(pa[-1])
                pb.append(pb[-1] + 1)
                pc.append(pc[-1])
                xb += 1 
                ret = max(ret, xb)
                xa = xc = 0
            else: 
                acc1 += 1
                acc2 -= 1
                pa.append(pa[-1])
                pb.append(pb[-1])
                pc.append(pc[-1] + 1)
                xc += 1 
                ret = max(ret, xc)
                xa = xb = 0

            
            if acc in p1: 
                idx = p1[acc]
                if pc[i + 1] == pc[idx + 1]: 
                    ret = max(ret, i - idx)
                else: 
                    p1[acc] = i
            elif acc == 0: 
                if pc[i + 1] == 0: 
                    ret = max(ret, i + 1)
                else: 
                    p1[acc] = i
            else: 
                p1[acc] = i
            
          
            if acc1 in p2: 
                idx = p2[acc1]
                if pa[i + 1] == pa[idx + 1]: 
                    ret = max(ret, i - idx)
                else: 
                    p2[acc1] = i
            elif acc1 == 0: 
                if pa[i + 1] == 0: 
                    ret = max(ret, i + 1)
                else: 
                    p2[acc1] = i
            else: 
                p2[acc1] = i
            # if p2[acc1] == 2: 
            #     import pdb 
            #     pdb.set_trace()

            
            if acc2 in p3: 
                idx = p3[acc2]
                if pb[i + 1] == pb[idx + 1]: 
                    ret = max(ret, i - idx)
                else: 
                    p3[acc2] = i
            elif acc2 == 0: 
                if pb[i + 1] == 0: 
                    ret = max(ret, i + 1)
                else: 
                    p3[acc2] = i
            else: 
                p3[acc2] = i

            if acc == 0 and acc1 == 0: 
                ret = max(ret, i + 1)
            elif (acc, acc1) in prev: 
                ret = max(ret, i - prev[(acc, acc1)])
            else:
                prev[(acc, acc1)] = i 
        
        return ret 
    

    def longestBalanced(self, s: str) -> int:
        from typing import DefaultDict
        ret = 0
        N = len(s)
        for i in range(N): 
            minN, maxN = len(s), 0
            seen = DefaultDict(int)
            r = [0] * (i + 1)
            for j in range(i, -1, -1):
                seen[s[j]] += 1 
                if seen[s[j]] == 1: 
                    r[0] += 1
                    minN = 1 
                else: 
                    r[seen[s[j]] - 2] -= 1 
                    r[seen[s[j]] - 1] += 1 
                    if (seen[s[j]] - 1) == minN and r[seen[s[j]] - 2] == 0: 
                        minN += 1

                # if i == 4: 
                #     import pdb 
                #     pdb.set_trace()
                maxN = max(maxN, seen[s[j]])
            
                if minN == maxN: 
                    ret = max(ret, (i - j + 1))
                    # print(s[j: i + 1])
                    # import pdb 
                    # pdb.set_trace()
                    # print(i, j)
                    # if i == 4 and j == 0: 
                    #     import pdb 
                    #     pdb.set_trace()
                # import pdb 
                # pdb.set_trace()
            # print(minN, maxN)
        return ret 
    
if __name__ == "__main__": 
    s = "abbac"
    s = "aabcc"
    s = "aba"
    # s = "abc"
    # s = "zzabccy"
    # s = "aba"
    # s = "nllnn"
    # s = "mllml"
    s = "accc"
    # s = "abcbc"
    ret = Solution().longestBalanced_1(s)
    print(ret)