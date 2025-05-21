from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums) 
        lbuf, rbuf = [0] * N, [0] * N
        for l, r in queries: 
            lbuf[l] += 1 
            rbuf[r] += 1
        
        def acc_from_right(l): 
            for i in range(len(l) - 2, -1, -1): 
                l[i] += l[i + 1]
        acc_from_right(lbuf)
        lbuf = lbuf[1:] + [0]
        acc_from_right(rbuf)
        # print(lbuf, rbuf)

        for n, lb, rb in zip(nums, lbuf, rbuf): 
            if n > (rb - lb): 
                return False
        return True
    
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        return -1 

if __name__ == "__main__": 
    nums = [1,0,1]
    queries = [[0,2]]
    # nums = [4,3,2,1]
    # queries = [[1,3],[0,2]]
    ret = Solution().isZeroArray(nums, queries)
    print(ret)