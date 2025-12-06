from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        wrong approach
        """
        import heapq
        intervals.sort()
        ret = 0 
        waive = 0
        ws = False
        eh = []
        N = len(intervals)
        mins = -1
        
        for i, (s, e) in enumerate(intervals):
            if i < N - 1 and intervals[i + 1][0] == intervals[i][0]: 
                heapq.heappush(eh, (e, s)) 
                continue
            if waive > 0: 
                ws = True 
            x = -1
            m = -1
            tmp = -1
            mine = 10 ** 8
            while len(eh) > 0 and s >= eh[0][0]: 
                _tmp, _s = heapq.heappop(eh)
                tmp = max(tmp, _tmp)
                
                if mins < 0 or (mins >= 0 and _s >= mins): 
                    x = _tmp
                    mine = min(mine, _tmp)
                m = min(x, m)
                # import pdb 
                # pdb.set_trace()
            mins = max(tmp, mins)
            # print(x, mins, mine, "l")
            
            # if s == 15: 
            #     import pdb 
            #     pdb.set_trace()
            # import pdb 
            # pdb.set_trace()
            if x >= 0 and x < s: 
                if waive == 0:
                    ret += 2
                else: 
                    ret += 1
                    waive = 0
    
            elif x == s: 
                if waive == 0: 
                    ret += 2 
                    waive = 1 if mine >= x else 0
                    ws = False
                    # al = False
                else: 
                    # if m < s: 
                    #     ret += 1 
                    #     waive = 0 
                    #     import pdb 
                    #     pdb.set_trace()
                    # else: 
                    ret += 1
                    waive = 1 if mine >= x else 0
                    ws = False
                    # al = True
            heapq.heappush(eh, (e, s)) 
           
            print(s, e, ret, mine)

        print(eh, s, waive)
        if len(eh) > 0: 
            if waive > 0 and not ws: 
                # if al:
                ret += 1 
            else:
                ret += 2
        return ret 
    
    def intersectionSizeTwo_1(self, intervals: List[List[int]]) -> int:
        import heapq
        intervals.sort()
        ret = 0
        
        return ret 

if __name__ == "__main__": 
    intervals = [[1,3],[3,7],[8,9]]
    # intervals = [[1,3],[1,4],[2,5],[3,5]]
    # intervals = [[1,2],[2,3],[2,4],[4,5]]
    # intervals = [[1,3],[1,2],[0,1]]
    # intervals = [[6,21],[1,15],[15,20],[10,21],[0,7]]
    # intervals = [[0,3],[3,5],[3,5],[0,1],[0,1]]
    # intervals = [[2,15],[9,17],[0,6],[17,25],[0,25]]
    # intervals = [[4,14],[6,17],[7,14],[14,21],[4,7]]
    intervals = [[1,3],[3,7],[5,7],[7,8]]
    ret = Solution().intersectionSizeTwo(intervals)
    print(ret)