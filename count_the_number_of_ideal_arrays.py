class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        
        parents = [[] for _ in range(maxValue)]
        for p in range(1, maxValue): 
            for c in range(maxValue): 
                if (c + 1) * (p + 1) <= maxValue: 
                    parents[c].append(p)
                else: 
                    break 

        def comb(n_num, n): 
            # at least one for each category
            # (n - n_num) + (n_num - 1) = n - 1 
            # n_num - 1 
            ac, bc = n - 1, n_num - 1 
            a = b = 1
            for i in range(n_num - 1): 
                a *= ac 
                b *= bc
                ac -= 1 
                bc -= 1 
            return a // b

        maxv = [1] * maxValue
        n_step, cnt = 0, maxValue
        ret = 0
        mod = 10 ** 9 + 7
        while True: 
            # print(maxv)
            n_step += 1
            nmaxv = [0] * maxValue
            for j in range(maxValue): 
                for p in parents[j]: 
                    nidx = (p + 1) * (j + 1) - 1
                    nmaxv[nidx] += maxv[j]

            ret = (ret + cnt * comb(n_step, n)) % mod
            # print(comb(n_step, n))
            maxv = nmaxv
            cnt = sum(maxv)
            if cnt == 0: 
                break
        
        return ret
    
if __name__ == "__main__": 
    n = 2
    maxValue = 5
    n = 5
    maxValue = 3
    # n = 5
    # maxValue = 9
    test_case = (n, maxValue)
    ret = Solution().idealArrays(*test_case)
    print(ret)