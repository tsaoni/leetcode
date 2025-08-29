from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        acc = []
        ret = 0
        s = [0] * 32 
        for i, num in enumerate(arr): 
            tmp = num 
            idx = 0
            inc = 0
            for _ in range(32): 
                if tmp & 1: 
                    if s[idx] == 0: 
                        inc = 1
                    # s[idx] += 1 
                else: 
                    if s[idx] == 1: 
                        inc = 1
                tmp >>= 1 
                idx += 1 
            if i == 0 or inc > 0: 
                acc.append(num) 
                tmp = num
                idx = 0
                while tmp > 0: 
                    if tmp & 1: 
                        s[idx] += 1 
                    tmp >>= 1 
                    idx += 1 
           
            full_cover = True 
            while full_cover and len(acc) > 1 and inc: 
                # print(acc)
                tmp = acc[0]
                idx = 0
                while tmp > 0: 
                    # import pdb 
                    # pdb.set_trace()
                    if tmp & 1 and s[idx] == 1: 
                        full_cover = False 
                        break 
                    tmp >>= 1 
                    idx += 1
                # print(full_cover)
                if full_cover: 
                    acc.pop(0)
            # print(acc)
            if i == 0 or inc:
                ret += len(acc) 
            print(acc)
        return ret
    
if __name__ == "__main__": 
    arr = [0]
    # arr = [1,1,2]
    arr = [1,2,4]
    arr = [3,11]
    arr = [13,4,2]
    ret = Solution().subarrayBitwiseORs(arr)
    print(ret)