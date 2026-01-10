from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        import heapq
        N = len(events)
        events.sort(key=lambda x: x[1])
        dp = {}
        for s, _, val in events: 
            if s not in dp: 
                dp[s] = val 
            else: 
                dp[s] = max(dp[s], val)
        maxv = 0
        _dp = []
        for k in sorted(dp, key=lambda x: -x): 
            maxv = max(maxv, dp[k])
            _dp.insert(0, (k, maxv))
            # dp[k] = maxv

        def search(s): 
            l, r = 0, len(_dp) - 1 
            while l < r: 
                mid = (l + r) // 2 
                if _dp[mid][0] < s: 
                    l = mid + 1 
                else: 
                    r = mid
            return l if _dp[l][0] >= s else -1 
        
        maxv = 0
        ret = 0
        for i in range(N): 
            _, et, val = events[i]
            maxv = max(maxv, val)
            idx = search(et + 1)
            if idx >= 0:
                ret = max(ret, maxv + _dp[idx][1])
            else: 
                ret = max(ret, maxv)
        return ret
    
if __name__ == "__main__": 
    events = [[1,3,2],[4,5,2],[2,4,3]]
    events = [[1,3,2],[4,5,2],[1,5,5]]
    events = [[1,5,3],[1,5,1],[6,6,5]]
    ret = Solution().maxTwoEvents(events)
    print(ret)