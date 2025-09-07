from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq 
        sub_fn = lambda ps, total: (ps + 1) / (total + 1) - ps / total
        pq = [(-sub_fn(*c), c[0] / c[1], i) for i, c in enumerate(classes)]
        # print(pq)
        heapq.heapify(pq)
        for _ in range(extraStudents): 
            _, _, idx = heapq.heappop(pq)
            classes[idx] = [classes[idx][0] + 1, classes[idx][1] + 1]
            heapq.heappush(pq, (-sub_fn(*classes[idx]), classes[idx][0] / classes[idx][1], idx))
            # print(pq, classes)
        return sum([x[1] for x in pq]) / len(classes)
    
if __name__ == "__main__": 
    classes = [[1,2],[3,5],[2,2]]
    extraStudents = 2
    classes = [[2,4],[3,9],[4,5],[2,10]]
    extraStudents = 4
    ret = Solution().maxAverageRatio(classes, extraStudents)
    print(ret)