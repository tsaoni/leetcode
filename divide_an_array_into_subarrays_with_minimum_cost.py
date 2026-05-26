from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        import heapq 
        N = len(nums)
        selected, rem = [(-nums[i], i) for i in range(1, k)], []
        heapq.heapify(selected)
        ret = sum([-x[0] for x in selected])
        is_selected = [True] * (k - 1) + [False] * (dist - k + 2)
        vcur = ret
        # print("vcur1", vcur)
        for lcur in range(k, N):
            if lcur <= dist + 1: 
                start = 1
                if nums[lcur] <= -selected[0][0]: 
                    v, idx = heapq.heappop(selected)
                    heapq.heappush(rem, (-v, idx))
                    heapq.heappush(selected, (-nums[lcur], lcur))
                    is_selected[idx - start] = False
                    # print(lcur, start)
                    is_selected[lcur - start] = True 
                    vcur = vcur + nums[lcur] + v
                    ret = min(ret, vcur)
                    # print("vcur2", vcur)
                else: 
                    heapq.heappush(rem, (nums[lcur], lcur))
            else:
                start = lcur - dist - 1
                is_selected.append(False)
                if is_selected[0]: 
                    heapq.heappush(rem, (nums[lcur], lcur))
                    while rem[0][1] < (start + 1): 
                        heapq.heappop(rem)
                    v, idx = heapq.heappop(rem)
                    is_selected[idx - start] = True
                    heapq.heappush(selected, (-v, idx))
                    vcur = vcur + v - nums[start]
                    ret = min(ret, vcur)
                    # print("vcur3", vcur)
                    # import pdb 
                    # pdb.set_trace()
                else: 
                    heapq.heappush(rem, (nums[lcur], lcur))
                    while rem[0][1] < (start + 1): 
                        heapq.heappop(rem)
                    while selected[0][1] < (start + 1): 
                        heapq.heappop(selected)
                    if rem[0][0] <= -selected[0][0]: 
                        rv, ridx = heapq.heappop(rem)
                        sv, sidx = heapq.heappop(selected)
                        heapq.heappush(rem, (-sv, sidx))
                        heapq.heappush(selected, (-rv, ridx))
                        is_selected[ridx - start] = True 
                        is_selected[sidx - start] = False
                        vcur = vcur + rv + sv
                        ret = min(ret, vcur)
                    # print("vcur4", vcur)
                is_selected.pop(0)
           
        return ret + nums[0]

if __name__ == "__main__": 
    nums = [1,3,2,6,4,2]
    k = 3
    dist = 3
    # nums = [10,1,2,2,2,1]
    # k = 4
    # dist = 3
    # nums = [10,8,18,9]
    # k = 3
    # dist = 1
    ret = Solution().minimumCost(nums, k, dist) 
    print(ret)