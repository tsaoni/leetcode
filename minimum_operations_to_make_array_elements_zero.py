from typing import List

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        import math
        mask = int('10' * 15 + '1', 2)
        def setBitNumber(n): 
            n |= n >> 1 
            n |= n >> 2 
            n |= n >> 4 
            n |= n >> 8 
            n |= n >> 16 
            n = (n + 1) >> 1 | n & (n << 31)
            n = n >> 1 if n & mask == 0 else n
            return n 
        
        ret = 0
        for start, end in queries: 
            _s, _e = setBitNumber(start), setBitNumber(end)
            base = 1
            rec = []
            n_ops = 1
            while base <= _e: 
                if base >= _s: 
                    rec.append((n_ops, base))
                n_ops += 1
                base <<= 2
            
            n_ops = 0
            s_rem, e_rem = start - rec[0][1], end - rec[-1][1] + 1
            rem = 0
            # print(rec, s_rem, e_rem)
            for i in range(len(rec) - 1): 
                # if i == 0: 
                #     cnt = rec[i + 1][1] - rec[i][1] - s_rem
                # else: 
                cnt = rec[i + 1][1] - rec[i][1]
                n_ops += rec[i][0] * (cnt)
                if cnt & 1:
                    rem = rec[i][0] 
                # print(cnt, n_ops)
    
            n_ops += rec[-1][0] * e_rem - rec[0][0] * s_rem
            # print(n_ops, e_rem)
            # n_ops += max(rec[-1][0], rem)
            ret += math.ceil(n_ops / 2)
            
        return ret
    
if __name__ == "__main__": 
    queries = [[1,2],[2,4]]
    queries = [[2,6]]
    queries = [[5,8]]
    # queries = [[3,10]]
    ret = Solution().minOperations(queries)
    print(ret)