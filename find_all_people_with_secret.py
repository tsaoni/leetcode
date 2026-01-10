from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = set({0, firstPerson})
        meetings.sort(key=lambda x: x[2])
        prev = -1
        cur = set() 

        for x, y, t in meetings: 
            if t != prev: 
                cur |= set({x, y})
    
            else: 
                
                prev = t 
        return [] 

if __name__ == "__main__": 
    Solution().findAllPeople