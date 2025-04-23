class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = 1
        while n // (10 ** d) > 0: 
            d += 1 
    
        N = (9 * d + 1)
        cnts = [0] * N
        ds = 0
        for i in range(d - 1, -1, -1): 
            v = n // (10 ** i) % 10
            
            ncnts = [0] * N 
            # if i == d - 1: 
            start = 0
            if i < d - 1:
                start = 1
                for j in range(N): 
                    for k in range(0, 10): 
                        if j + k < N:
                            ncnts[j + k] += cnts[j]
                        else: 
                            break
                # import pdb 
                # pdb.set_trace()
            for j in range(v): 
                ncnts[ds + j] += 1 
                # for j in range(0, v): 
                #     ncnts[ds + j] += 1
                # import pdb 
                # pdb.set_trace()
            ds += v
            cnts = ncnts
    
        cnts[ds] += 1
        cnts[0] = 0
        c = max(cnts)
        # print(cnts)

        return sum([x == c for x in cnts])
    
if __name__ == "__main__": 
    ret = Solution().countLargestGroup(2)
    print(ret)