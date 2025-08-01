from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
        F = [[n - 1, n - 1] for _ in range(n)]
        for a, b in conflictingPairs: 
            start, end = (a, b) if a < b else (b, a)
            F[start - 1].append(end - 2)
            F[start - 1] = sorted(F[start - 1])[: 2]
          
        for i in range(n - 1, 0, -1): 
            F[i - 1] = sorted(F[i - 1] + F[i])[: 2]
        # print(F)
        ret = 0 
        for i in range(n): 
            ret += (F[i][0] - i + 1)

        delCount = [0] * n
        for i in range(n): 
            i_rev = F[i][0]
            delCount[i_rev] += (F[i][1] - F[i][0])

        return ret + max(delCount)
    
if __name__ == "__main__": 
    n = 4
    conflictingPairs = [[2,3],[1,4]]
    n = 5
    conflictingPairs = [[1,2],[2,5],[3,5]]
    ret = Solution().maxSubarrays(n, conflictingPairs)
    print(ret)