from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        """
        a wrong approach
        """
        import heapq
        from itertools import chain
        timestamps = []
        for start, end in events: 
            timestamps.append([start, 0])
            timestamps.append([end, 1])
        timestamps = sorted(timestamps, )#key=lambda x: x[0])
        # print(events)
        req = 0 
        quota = 0
        ev = 0 
        prev = -1 
        ret = 0
        for cur, type in timestamps: 
            if type == 0: 
                req += 1 
                ev += 1 
                print(cur, type) 
                print(ret, quota)
            quota += cur - prev if prev >= 0 else 1 
            # import pdb 
            # pdb.set_trace()
            
            
            if type == 1: 
                
          
                ret += 1 if quota > 0 else 0 #min(req, quota)
                print(cur, type)
                print(ret, req, quota)
                # req, quota = max(req - quota, 0), max(quota - req, 0)
                if req > 0: 
                    quota -= 1

                ev -= 1
                req = min(req, ev)

            prev = cur
        return ret 
    
    def maxEvents1(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        cur = -1 
        ret = 0
        for start, end in events: 
            if start <= cur: 
                if end > cur: 
                    ret += 1 
                    cur += 1 
            else: 
                cur = start 
                ret += 1 
        return ret 

    def maxValue(self, events: List[List[int]], k: int) -> int:
        N = len(events)
        events.sort(key=lambda x: x[1])
        dp = [[0] * (N + 1) for _ in range(k + 1)]
        def search(end, n):
            if end <= events[0][1]: 
                return -1 
            l, r = 0, n - 1
            while l < r: 
                mid = (l + r + 1) // 2 
                if events[mid][1] >= end: 
                    r = mid - 1 
                else: 
                    l = mid
            return l
        
        for i in range(1, k + 1): 
            for j in range(1, N + 1): 
                dp[i][j]
                end = events[j - 1][0]
                idx = search(end, j - 1)
                take = dp[i - 1][idx + 1] + events[j - 1][2]
                notake = dp[i][j - 1]
                dp[i][j] = max(take, notake)
        
        return dp[-1][-1] 

if __name__ == "__main__": 
    events = [[1,2],[2,3],[3,4]]
    # events= [[1,1],[1,1],[1,1]]
    # events = [[1,2],[1,2],[1,2],[1,2],[1,6],]
    # events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    # events = [[1,10],[2,2],[2,2],[2,2],[2,2]]
    events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    ret = Solution().maxEvents1(events)
    print(ret)

    # events = [[1,2,4],[3,4,3],[2,3,1]]
    # k = 2
    # events = [[1,2,4],[3,4,3],[2,3,10]]
    # k = 2
    # ret = Solution().maxValue(events, k)
    # print(ret)