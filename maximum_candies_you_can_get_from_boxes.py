from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        from itertools import chain
        boxes = set(initialBoxes)
        ret = 0
        have_new = True
        while have_new: 
            have_new = False
            nboxes = set()
            avail_keys = set(chain(*[keys[bidx] if status[bidx] else [] for bidx in boxes]))
            for k in avail_keys: 
                status[k] = 1
            for bidx in boxes: 
                if status[bidx]:
                    ret += candies[bidx]
                    for nbidx in containedBoxes[bidx]: 
                        have_new = True
                        nboxes.add(nbidx)
                else: 
                    nboxes.add(bidx)
            boxes = nboxes
        return ret
    
if __name__ == "__main__": 
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]

    status = [1,0,0,0,0,0]
    candies = [1,1,1,1,1,1]
    keys = [[1,2,3,4,5],[],[],[],[],[]]
    containedBoxes = [[1,2,3,4,5],[],[],[],[],[]]
    initialBoxes = [0]
    ret = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print(ret)