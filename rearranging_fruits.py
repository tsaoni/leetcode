from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        basket1.sort()
        basket2.sort()
        # print(basket1)
        # print(basket2)
        idx1, idx2 = 0, 0
        cnt1, cnt2 = 0, 0 
        sw1, sw2 = [], []
        while idx1 < len(basket1) and idx2 < len(basket2): 
            if basket1[idx1] < basket2[idx2]: 
                pre = basket1[idx1]
                cnt = 0
                while idx1 < len(basket1) and basket1[idx1] == pre: 
                    idx1 += 1
                    cnt += 1 
                # print(cnt)
                if cnt & 1 == 1: 
                    return -1 
                cnt1 += cnt // 2 
                sw1.extend([pre] * (cnt // 2))
            elif basket2[idx2] < basket1[idx1]: 
                pre = basket2[idx2]
                cnt = 0
                while idx2 < len(basket2) and basket2[idx2] == pre: 
                    idx2 += 1
                    cnt += 1 
                if cnt & 1 == 1: 
                    return -1 
                # print(cnt)
                cnt2 += cnt // 2 
                sw2.extend([pre] * (cnt // 2))
            else: 
                idx1 += 1 
                idx2 += 1 
        cnt = 0
        while idx1 < len(basket1): 
            pre = basket1[idx1]
            cnt = 0
            while idx1 < len(basket1) and basket1[idx1] == pre: 
                idx1 += 1
                cnt += 1 
            # print(cnt)
            if cnt & 1 == 1: 
                return -1 
            cnt1 += cnt // 2 
            sw1.extend([pre] * (cnt // 2))
      
        while idx2 < len(basket2): 
            pre = basket2[idx2]
            cnt = 0
            while idx2 < len(basket2) and basket2[idx2] == pre: 
                idx2 += 1
                cnt += 1 
            if cnt & 1 == 1: 
                return -1 
            # print(cnt)
            cnt2 += cnt // 2 
            sw2.extend([pre] * (cnt // 2))
       
        if cnt1 != cnt2: 
            return -1 
        else: 
            # print(cnt1)
            # print(sw1, sw2)
            l = cnt1 // 2
            ret = 0 
            p = min(basket1[0], basket2[0])
            for x1, x2 in zip(sw1, reversed(sw2)): 
                ret += min(x1, x2, 2 * p)
                # print(ret)
            return ret

    
if __name__ == "__main__": 
    basket1 = [4,2,2,2]
    basket2 = [1,4,1,2]
    # basket1 = [2,3,4,1]
    # basket2 = [3,2,5,1]
    basket1 = [4,4,4,4,3]
    basket2 = [5,5,5,5,3]
    # basket1 = [84,80,43,8,80,88,43,14,100,88]
    # basket2 = [32,32,42,68,68,100,42,84,14,8]
    ret = Solution().minCost(basket1, basket2)
    print(ret)