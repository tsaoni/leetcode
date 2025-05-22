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
        def isZeroArray(nums: List[int], queries: List[List[int]]) -> bool:
            N = len(nums) 
            lbuf, rbuf = [0] * N, [0] * N
            for l, r, v in queries: 
                lbuf[l] += v 
                rbuf[r] += v
            
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
        
        # print(isZeroArray(nums, queries[: 4]))
        if not isZeroArray(nums, queries): 
            return -1
        l, r = 0, len(queries)  
        while l < r: 
            mid = (l + r) // 2 
            tmp = isZeroArray(nums, queries[: mid])
            if tmp:
                r = mid 
            else: 
                l = mid + 1
       
        return l

    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        will result in TLE
        """
        import heapq
        N = len(nums)
        queries.sort()
        buffers = [0] * N 
        queue = []
        cur = -1
        n_remain = 0
        for i in range(N): 
            while cur < len(queries) - 1 and i >= queries[cur + 1][0] and i <= queries[cur + 1][1]: 
                cur += 1 
                heapq.heappush(queue, [-queries[cur][1], *queries[cur]])
            # print(queue)
            while len(queue) > 0 and buffers[i] < nums[i]: 
                x = heapq.heappop(queue)
                if x[1] <= i: 
                    n_remain += 1
                    # print(x)
                    for idx in range(i, x[2] + 1): 
                        buffers[idx] += 1 
            if buffers[i] < nums[i]: 
                return -1 
            # print(buffers)
        
        return len(queries) - n_remain

    def maxRemoval1(self, nums: List[int], queries: List[List[int]]) -> int:
        import heapq
        N = len(nums)
        queries.sort()
        # buffers = [0] * N 
        queue = []
        active = []
        cur = -1
        n_remain = 0
        for i in range(N): 
            while cur < len(queries) - 1 and i >= queries[cur + 1][0] and i <= queries[cur + 1][1]: 
                cur += 1 
                heapq.heappush(queue, [-queries[cur][1], *queries[cur]])
            # print(queue)
            
            while len(active) > 0 and active[0] < i: 
                heapq.heappop(active)
            while len(queue) > 0 and len(active) < nums[i]: 
                x = heapq.heappop(queue)
                if x[1] <= i and i <= x[2]: 
                    # n_remain += 1
                    heapq.heappush(active, x[2])
                    # print(x)
                    # for idx in range(i, x[2] + 1): 
                    #     buffers[idx] += 1 
            
            # print(active)
            if len(active) < nums[i]: 
                return -1 
            # print(buffers)
        
        return len(queue) 

if __name__ == "__main__": 
    nums = [1,0,1]
    queries = [[0,2]]
    # nums = [4,3,2,1]
    # queries = [[1,3],[0,2]]
    # ret = Solution().isZeroArray(nums, queries)
    # print(ret)

    nums = [2,0,2]
    queries = [[0,2],[0,2],[1,1]]
    # nums = [1,1,1,1]
    # queries = [[1,3],[0,2],[1,3],[1,2]]
    nums = [1,2,3,4]
    queries = [[0,3]]
    # nums = [0,0,3] 
    # queries = [[0,2],[1,1],[0,0],[0,0]]
    # ret = Solution().maxRemoval1(nums, queries)
    # print(ret)

    nums = [2,0,2]
    queries = [[0,2,1],[0,2,1],[1,1,3]]
    nums = [7,6,8] 
    queries = [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]
    ret = Solution().minZeroArray(nums, queries)
    print(ret)