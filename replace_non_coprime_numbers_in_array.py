from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a, b): 
            return a * b // gcd(a, b)
        
        def gcd(a, b): 
            # print(a, b)
            if a > b: 
                a, b = b, a
            if a > 0: 
                c = b // a 
                a, b = min(a, b - c * a), max(a, b - c * a)
                return gcd(a, b)
            else: 
                return b
            
        def get_coprimes(lst): 
            if len(lst) <= 1: 
                return lst
            mid = len(lst) // 2 
            llst = get_coprimes(lst[: mid])
            rlst = get_coprimes(lst[mid: ])
            # print(llst, rlst)
            if len(llst) > 0 and len(rlst) > 0: 
                tmp = rlst.pop(0)
                while True:
                    _tmp = tmp
                    while len(llst) > 0: 
                        c = gcd(llst[-1], tmp)
                        if c == 1: 
                            break 
                        else: 
                            tmp = tmp * llst.pop(-1) // c
                    
                    while len(rlst) > 0: 
                        c = gcd(rlst[0], tmp)
                        if c == 1: 
                            break 
                        else: 
                            tmp = tmp * rlst.pop(0) // c
                    if _tmp == tmp: 
                        break    
                # print(llst + [tmp] + rlst)
                # import pdb 
                # pdb.set_trace()
                return llst + [tmp] + rlst
            elif len(llst) > 0: 
                return llst 
            else: 
                return rlst
            
        return get_coprimes(nums)
    
if __name__ == "__main__": 
    nums = [6,4,3,2,7,6,2]
    nums = [2,2,1,1,3,3,3]
    ret = Solution().replaceNonCoprimes(nums)
    print(ret)