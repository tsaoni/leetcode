from typing import List
import heapq

class Solution:
    def countDays1(self, days: int, meetings: List[List[int]]) -> int:
        sheap, eheap = [], []
        d_lst = []
        for s, e in meetings: 
            sheap += [s]
            eheap += [e]
            d_lst += [s, e]
        heapq.heapify(sheap)
        heapq.heapify(eheap)
        d_lst = list(set(d_lst))
        d_lst.sort()
        # print(sheap)
        # print(eheap)
        ret = 0
        prev = 0
        for day in d_lst: 

            if len(sheap) == len(eheap): 
                # print(day)
                # print(sheap)
                # print(eheap)
                ret += (day - prev - 1)
                # for i in range(prev + 1, day): 
                #     print(i)
            prev = day

            while len(sheap) > 0 and day == sheap[0]: 
                x = heapq.heappop(sheap)
            
            while len(eheap) > 0 and day == eheap[0]:
                x = heapq.heappop(eheap)
        
        ret += days - d_lst[-1]
        # for i in range(d_lst[-1] + 1, days + 1): 
        #     print(i)

        return ret
    
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        """
        TLE
        """
        sheap, eheap = [], []
        for s, e in meetings: 
            sheap += [s]
            eheap += [e]
        heapq.heapify(sheap)
        heapq.heapify(eheap)
        # print(sheap)
        # print(eheap)
        ret = 0
        for day in range(1, days + 1): 
            # if len(eheap) == 0: 
            #     ret += 1 
            # else:
            x = -1
            while len(sheap) > 0 and day == sheap[0]: 
                x = heapq.heappop(sheap)
            
            while len(eheap) > 0 and day == eheap[0]:
                x = heapq.heappop(eheap)
            
            if x == -1: 
                if len(sheap) == len(eheap): 
                    # print(day)
                    # print(sheap)
                    # print(eheap)
                    ret += 1

        return ret
    
if __name__ == "__main__": 
    days = 10
    meetings = [[5,7],[1,3],[9,10]]
    
    days = 5
    meetings = [[2,4],[1,3]]

    days = 6
    meetings = [[1,6]]

    days = 8 
    meetings = [[3,4],[4,8],[2,5],[3,8]]

    test_case = (days, meetings)
    ret = Solution().countDays1(*test_case)
    print(ret)