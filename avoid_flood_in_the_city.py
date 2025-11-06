from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ret = [-1] * len(rains)
        # last = [-1] * len(rains)
        em = []
        last = {}
        def search(day): 
            if len(em) == 0: 
                return -1
            l, r = 0, len(em) - 1
            while l < r: 
                mid = (l + r) // 2 
                if em[mid] > day: 
                    r = mid
                else: 
                    l = mid + 1
            return l if em[l] > day else -1 
        
        for i in range(len(rains)): 
            if rains[i] == 0: 
                em.append(i)
            else:
                if rains[i] in last: 
                    idx = last[rains[i]]
                    x = search(idx)
                    if x == -1: 
                        return []
                    d = em.pop(x)
                    ret[d] = rains[i]
                    del last[rains[i]]
                # else:
                last[rains[i]] = i 
        for d in em: 
            ret[d] = 1
        return ret
    
if __name__ == "__main__": 
    rains = [1,2,3,4]
    # rains = [1,2,0,0,2,1]
    rains = [1,2,0,1,2]
    rains = [0,1,1]
    rains = [69,0,0,0,69]
    rains = [1,0,2,0,2,1]
    ret = Solution().avoidFlood(rains)
    print(ret)