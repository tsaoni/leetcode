class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        import math
        N = len(s)
        prez = [0] * N 
        pz = -1
        pso = [0] * N 
        ret = 0
        for i in range(N): 
            prez[N - 1 - i] = pz
            if s[N - 1 - i] == "0": 
                pz = N - 1 - i
            if s[i] == "1":
                pso[i] += 1 
            if i > 0:
                # psz[i] += psz[i - 1]
                pso[i] += pso[i - 1]

        # print(prez, pso)
        # acc_z = 0
        for l in range(N): 
            _acc_z = 0
            idx = l 
            if s[l] == "0": 
                _acc_z += 1
            # _acc_z = acc_z
            # n = pso[N - 1] - pso[l - 1] if l > 0 else pso[N - 1]
            while idx < N and pso[N - 1] >= _acc_z ** 2: 
                nidx = prez[idx] if prez[idx] >= 0 else N 
                no = pso[nidx - 1] - pso[idx - 1] if idx > 0 else pso[nidx - 1]
                fno = pso[nidx - 1] - (pso[l - 1] if l > 0 else 0) - _acc_z ** 2 + 1
                ret += max(min(no, fno), 0)
                # print(no, fno)
                if s[idx] == "0" and pso[idx] - (pso[l - 1] if l > 0 else 0) >= _acc_z ** 2: 
                    ret += 1
                # if l == 2:
                # import pdb 
                # pdb.set_trace()
                idx = nidx 
                _acc_z += 1
            # print(l, ret, _acc_z)
            # will results in TLE
            # acc_z, acc_o = 0, 0 
            # no = pso[N - 1] - pso[l - 1] if l > 0 else pso[N - 1] 
            # sqrt_v = math.sqrt(no)
            # idx = l
            # while idx < N and acc_z < sqrt_v: 
            #     if s[idx] == "0": 
            #         acc_z += 1 
            #     else: 
            #         acc_o += 1 
            #     if math.sqrt(acc_o) >= acc_z: 
            #         ret += 1 
            #     idx += 1

        return ret
    
if __name__ == "__main__": 
    s = "00011"
    # s = "101101"
    ret = Solution().numberOfSubstrings(s)
    print(ret)