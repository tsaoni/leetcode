class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        N = len(s)
        cnt = [0] * 5
        # prefix sum 
        psum = [[0] * 5 for _ in range(N + 1)]
        for i in range(1, N + 1): 
            for j in range(5): 
                psum[i][j] += psum[i - 1][j]
        
            psum[i][int(s[i - 1])] += 1 
        
        # print(psum)
        # sliding windows
        starts = [[-1] * 5 for _ in range(5)]
        cnts = [[-N] * 5 for _ in range(5)]
        minFreq = [[[[N, N], [N, N]] for _ in range(5)] for _ in range(5)]
        parity = lambda x: 1 if x & 1 else 0
        setMinIfNotEqual = lambda val, x, cmpr: cmpr if x == val else min(x, cmpr)
        notupdated = [True] * 5
        for m in range(k, N + 1):
            c = int(s[m - 1])
            if m == k: 
                for i in range(5): 
                    for j in range(5):
                        if i != j: 
                            if psum[k][i] & 1 and psum[k][j] & 1 == 0 and psum[k][j] > 0:
                                cnts[i][j] = psum[k][i] - psum[k][j]
                            if psum[k][j] & 1 and psum[k][i] & 1 == 0 and psum[k][i] > 0:
                                cnts[j][i] = psum[k][j] - psum[k][i]
                # print(cnts)
            elif m > k:
            # if True:
                notupdated[c] = False
                for i in range(5): 
                    # if i != c:
                    for c in range(5): 
                        if i == c: 
                            continue
                        start = starts[c][i] + 1 if starts[c][i] == -1 else starts[c][i]
                        while m - start >= k and psum[m][i] - psum[start][i] >= 1 and psum[m][c] - psum[start][c] >= 1: 
                            if start > starts[c][i]:
                                minFreq[c][i][parity(psum[start][c])][parity(psum[start][i])] = setMinIfNotEqual(
                                    N, minFreq[c][i][parity(psum[start][c])][parity(psum[start][i])], psum[start][c] - psum[start][i])
                            
                            tmp = minFreq[c][i][1 - parity(psum[m][c])][parity(psum[m][i])]
                            # tmp = 0 if tmp == N else tmp
                            # if tmp == N and (1 - parity(psum[m][c])) & 1 == 0 and parity(psum[m][i]) & 1 == 0:
                            if (1 - parity(psum[m][c])) & 1 == 0 and parity(psum[m][i]) & 1 == 0:
                                tmp = min(tmp, 0)
                            if tmp < N:
                                cnts[c][i] = max(cnts[c][i], 
                                    psum[m][c] - psum[m][i] - tmp)
                            # minFreq[c][i][parity(psum[start + 1][c])][parity(psum[start + 1][i])] = setMinIfNotEqual(
                            #     N, minFreq[c][i][parity(psum[start + 1][c])][parity(psum[start + 1][i])], psum[start + 1][c] - psum[start + 1][i])
                            # print(start, m, c, i, minFreq[c][i])
                            # print(cnts)
                           
                            # if cnts[c][i] == 2:
                            start += 1 
                        start -= 1 
                        starts[c][i] = start
                # print()
                for i in range(5): 
                    # if i != c: 
                    for c in range(5): 
                        if i == c: 
                            continue
                        start = starts[i][c] + 1 if starts[i][c] == -1 else starts[i][c]
                        while m - start >= k and psum[m][i] - psum[start][i] >= 1 and psum[m][c] - psum[start][c] >= 1: 
                            if start > starts[i][c]:
                                minFreq[i][c][parity(psum[start][i])][parity(psum[start][c])] = setMinIfNotEqual(
                                    N, minFreq[i][c][parity(psum[start][i])][parity(psum[start][c])], psum[start][i] - psum[start][c])
                            
                            tmp = minFreq[i][c][1 - parity(psum[m][i])][parity(psum[m][c])]
                            # tmp = 0 if tmp == N else tmp
                            #if tmp == N and (1 - parity(psum[m][i])) & 1 == 0 and parity(psum[m][c]) & 1 == 0:
                            if (1 - parity(psum[m][i])) & 1 == 0 and parity(psum[m][c]) & 1 == 0:
                                tmp = min(tmp, 0)
                            if tmp < N:
                                cnts[i][c] = max(cnts[i][c], 
                                    psum[m][i] - psum[m][c] - tmp)
                    
                            
                            # minFreq[i][c][parity(psum[start + 1][i])][parity(psum[start + 1][c])] = setMinIfNotEqual(
                            #     N, minFreq[i][c][parity(psum[start + 1][i])][parity(psum[start + 1][c])], psum[start + 1][i] - psum[start + 1][c])
                            # print(start, m, i, c, minFreq[i][c])
                            # print(cnts)
                    

                            # import pdb 
                            # pdb.set_trace()
                            start += 1 
                        start -= 1 
                        starts[i][c] = start

            
        cnt = max([cnts[i][j] for i in range(5) for j in range(5) if i != j])
        return cnt
    

if __name__ == "__main__": 
    s = "12233"
    k = 4
    s = "1122211"
    k = 3
    s = "110"
    k = 3
    # s = "300"
    # k = 2
    # s = "00014313" 
    # k = 3
    # s = "44114402" 
    # k = 7
    # s = "2400030144"
    # k = 2
    # s = "21022003231211313014143313134302410430013331411032014241320342" 
    # k = 55
    ret = Solution().maxDifference(s, k)
    print(ret)