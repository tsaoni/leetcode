from typing import List
import heapq

class Solution:
    def mostPoints1(self, questions: List[List[int]]) -> int:
        max_pnts = 0 
        heap = []
        for qidx, (val, skip_num) in enumerate(questions): 
            while len(heap) > 0 and heap[0][0] == qidx: 
                _, tmp = heapq.heappop(heap)
                max_pnts = max(max_pnts, tmp)
            heapq.heappush(heap, (qidx + skip_num + 1, max_pnts + val))
        while len(heap) > 0: 
            _, tmp = heapq.heappop(heap)
            max_pnts = max(max_pnts, tmp)
        return max_pnts
    
    def mostPoints(self, questions: List[List[int]]) -> int:
        """TLE"""
        def dp(idx): 
            if idx >= len(questions): 
                return 0
            return max(questions[idx][0] + dp(idx + questions[idx][1] + 1), dp(idx + 1))
        return dp(0)
    
if __name__ == "__main__": 
    questions = [[3,2],[4,3],[4,4],[2,5]]
    questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    test_case = (questions, )
    ret = Solution().mostPoints1(*test_case)
    print(ret)