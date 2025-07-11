from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        import heapq
        end_heap, non_end_heap = [[i, 0] for i in range(n)], []
        n_meetings = [0] * n 
        meetings.sort(key=lambda x: x[0])
        for start, end in meetings: 
            while len(non_end_heap) > 0 and non_end_heap[0][0] <= start: 
                t, r_id = heapq.heappop(non_end_heap)
                heapq.heappush(end_heap, [r_id, t])
            if len(end_heap) > 0:
                r_id, t = heapq.heappop(end_heap)
                n_meetings[r_id] += 1 
                heapq.heappush(non_end_heap, [end, r_id])
            else: 
                t, r_id = heapq.heappop(non_end_heap)
                n_meetings[r_id] += 1
                heapq.heappush(non_end_heap, [end + t - start, r_id])

        ret = 0 
        for i in range(1, n): 
            if n_meetings[i] > n_meetings[ret]: 
                ret = i 
        return ret 
    
if __name__ == "__main__": 
    n = 2
    meetings = [[0,10],[1,5],[2,7],[3,4]]
    n = 3
    meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
    ret = Solution().mostBooked(n, meetings) 
    print(ret)