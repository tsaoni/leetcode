class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        states = []
        def bitwise_and(x1, x2): 
            return any([a1 & a2 for a1, a2 in zip(x1, x2)])
        
        def build_states(prev): 
            if len(prev) == m: 
                # print(prev)
                states.append(prev)
            else:
                for s in [[1, 0, 0], [0, 1, 0], [0, 0, 1]]: 
                    if len(prev) == 0 or (len(prev) > 0 and not bitwise_and(prev[-1], s)):
                        build_states(prev + [s])
        build_states([])
        # print(len(states))

        def bitwise_and_state(s1, s2): 
            return any([bitwise_and(a1, a2) for a1, a2 in zip(s1, s2)])
        
        d = len(states)
        M = []
        for i in range(d): 
            row = []
            for j in range(d): 
                row.append(not bitwise_and_state(states[i], states[j]))
            M.append(row)
        # print(M)

        modulo = 10 ** 9 + 7
        def mmul(M1, M2): 
            M = []
            for r in M1: 
                row = []
                for c in zip(*M2): 
                    tmp = sum([x1 * x2 % modulo for x1, x2 in zip(r, c)]) % modulo
                    row.append(tmp)
                M.append(row)
            return M 
        
        def mul_exp(M, n): 
            ret = []
            for i in range(d): 
                row = []
                for j in range(d): 
                    if i == j: 
                        row.append(1)
                    else: 
                        row.append(0)
                ret.append(row)
            while n > 0: 
                if n & 1: 
                    ret = mmul(M, ret)
                M = mmul(M, M)
                n //= 2 
            return ret
        
        def mul(M, s): 
            return [sum([x1 * x2 % modulo for x1, x2 in zip(r, s)]) % modulo for r in M]
        s0 = [1] * d 
        M = mul_exp(M, n - 1)
        s = mul(M, s0)
        return sum(s) % modulo

if __name__ == "__main__": 
    ret = Solution().colorTheGrid(5, 5)
    print(ret)