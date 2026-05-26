from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Node: 
    prev: Optional["Node"] = None
    next: Optional["Node"] = None
    val: int = 0
    start: int = -1 
    end: int = -1

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        import heapq 
        N = len(nums) 
        pq = []
        op = 0 
        merged = [[False, False] for _ in range(N)] 
        ptrs = [None] * N
        dcnt = 0
        cur = root = Node(None, None, nums[0], 0, 0)
        ptrs[0] = root
        for i in range(N - 1): 
            if nums[i] > nums[i + 1]: 
                dcnt += 1 
            pq.append((nums[i] + nums[i + 1], (i, i + 1)))
            p = Node(cur, None, nums[i + 1], i + 1, i + 1)
            cur.next = p 
            cur = cur.next 
            ptrs[i + 1] = cur

        heapq.heapify(pq)
        while dcnt > 0: 
            # print(len(pq), dcnt)
            tot, (s, e) = heapq.heappop(pq)
            if merged[s][0] or merged[e][1]: 
                continue
            merged[s][1] = True 
            merged[e][0] = True 
            
            # print()
            # print((s, e))
            # print(pq)

            dori = 0 
            dori += (ptrs[e].val - ptrs[s].val) < 0
            if ptrs[s].prev:
                dori += (ptrs[s].val - ptrs[s].prev.val) < 0
            if ptrs[e].next:
                dori += (ptrs[e].next.val - ptrs[e].val) < 0

            merged[ptrs[s].end][1] = True 
            merged[ptrs[e].start][0] = True
            ptrs[s].next = ptrs[e].next 
            if ptrs[e].next is not None:
                ptrs[e].next.prev = ptrs[s]
            ptrs[s].val = ptrs[s].val + ptrs[e].val
            ptrs[s].end = ptrs[e].end
            ptrs[e] = ptrs[s]
            
            dnxt = 0 
            if ptrs[s].prev:
                dnxt += (ptrs[s].val - ptrs[s].prev.val) < 0
            if ptrs[e].next:
                dnxt += (ptrs[e].next.val - ptrs[e].val) < 0
            dcnt = dcnt - dori + dnxt 
            
            # heappush
            if ptrs[s].next:
                _s, _e = ptrs[s].start, ptrs[s].next.end 
                _tot = ptrs[s].val + ptrs[s].next.val
                heapq.heappush(pq, (_tot, (_s, _e)))
            if ptrs[s].prev:
                _s, _e = ptrs[s].prev.start, ptrs[s].end 
                _tot = ptrs[s].prev.val + ptrs[s].val
                heapq.heappush(pq, (_tot, (_s, _e)))
            
            cur = root 
            # print()
            # while cur is not None: 
            #     print((cur.start, cur.end, cur.val))
            #     cur = cur.next      

            op += 1 
        
        return op 
    
if __name__ == "__main__": 
    nums = [5,2,3,1]
    nums = [1,2,2]
    nums = [-2,1,2,-1,-1,-2,-2,-1,-1,1,1]
    ret = Solution().minimumPairRemoval(nums)
    print(ret)