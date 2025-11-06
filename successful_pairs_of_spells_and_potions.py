from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        spells = sorted([(s, i) for i, s in enumerate(spells)], key=lambda x: -x[0])
        potions.sort()
        ret = [0] * len(spells)
        cur = 0
        for s, i in spells: 
            while cur < len(potions) and s * potions[cur] < success: 
                cur += 1 
            if cur == len(potions): 
                break 
            ret[i] = len(potions) - cur
        return ret 
    
if __name__ == "__main__": 
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    ret = Solution().successfulPairs(spells, potions, success)
    print(ret)