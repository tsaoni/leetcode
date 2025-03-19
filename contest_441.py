from typing import List

class Solution: 
    def func(): 
        return 
    

    def maxSum(self, nums: List[int]) -> int:
        arr = []
        for num in nums: 
            if num > 0 and num not in arr: 
                arr += [num]
        if len(arr) == 0: 
            arr += [max(nums)]
        return sum(arr)

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dist = [-1] * len(nums) #{}
        idx_dict = {}
        for i in range(2 * len(nums)): 
            # print(i)
            idx = i % len(nums)
            tmp = nums[idx]
            if tmp not in idx_dict: 
                idx_dict[tmp] = (None, i)
            else: 
                if idx_dict[tmp][0] == None: 
                    dist[idx] = i - idx_dict[tmp][1]
                    idx_dict[tmp] = (idx_dict[tmp][1], i)
                    
                else:
                    if dist[idx] == -1:
                        dist[idx] = i - idx_dict[tmp][1] #min(i - idx_dict[tmp][1], idx_dict[tmp][1] - idx_dict[tmp][0])
                    else: 
                        dist[idx] = min(i - idx_dict[tmp][1], dist[idx])
                    dist[idx_dict[tmp][1] % len(nums)] = min(
                        i - idx_dict[tmp][1], idx_dict[tmp][1] - idx_dict[tmp][0])
                    idx_dict[tmp] = (idx_dict[tmp][1], i)
            # print(dist)
        
                # if dist[tmp][1] == None: 
                #     dist[tmp] = (dist[tmp][0], idx)
                # else: 
                #     if i - dist[tmp][1] < dist[tmp][1] - dist[tmp][0]: 
                #         dist[tmp] = (dist[tmp][1], i)

            # if tmp not in dist: 
            #     dist[tmp] = (idx, None) 
            # else: 
            #     if dist[tmp][1] == None: 
            #         dist[tmp] = (dist[tmp][0], idx)
            #     else: 
            #         if i - dist[tmp][1] < dist[tmp][1] - dist[tmp][0]: 
            #             dist[tmp] = (dist[tmp][1], i)

        # for i in range(len(nums)): 
        #     tmp = nums[i]
        #     if tmp in idx_dict:
        #         idx_dict[tmp] += [i]
        #     else: 
        #         idx_dict[tmp] = [i]

        # print(dist)
        # print(idx_dict)
        # print(nums)
        # print(queries)
        # return
        ret = []
        for q in queries: 
            if dist[q] == len(nums): 
                ret += [-1] 
            else: ret += [dist[q]]
            # num = nums[q]
            # idxs = idx_dict[num]
            # if len(idxs) == 1: 
            #     ret += [-1]
            # else: 
            #     idx = idxs.index(q)
            #     prev = (idx - 1 + len(idxs)) % len(idxs)
            #     next = (idx + 1) % len(idxs)
            #     dist_fn = lambda p, n: n - p if n - p >= 0 else (n - p + len(nums))
            #     tmp = min(dist_fn(idxs[prev], idxs[idx]), dist_fn(idxs[idx], idxs[next]))
            #     ret += [tmp]
                # import pdb 
                # pdb.set_trace()
            
            # d = dist[num][1] - dist[num][0]
            # if d == 0: 
            #     ret += [-1] 
            # else: ret += [d]
        return ret

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if sum(nums) == 0: 
            return 0
        cnt = [False] * len(nums)
        vals = []
        for i, x in enumerate(nums): 
            if x == 0: 
                cnt[i] = True
            vals += [{x}]
        k = 0
        for l, r, val in queries: 
            for i in range(l, r + 1): 
                if not cnt[i]:
                    s = set()
                    for v in vals[i]: 
                        if v == val: 
                            cnt[i] = True 
                        elif v > val: 
                            s |= {v - val}
                    vals[i] |= s
            k += 1
            if sum(cnt) == len(nums): 
                return k
        return -1



if __name__ == "__main__": 
    
    # nums = [1,3,1,4,1,3,2]
    # queries = [0,3,5]
    # nums = [1,2,3,4]
    # queries = [0,1,2,3]
    # nums = [14,14,4,2,19,19,14,19,14]
    # queries = [2,4,8,6,3]
    # test_case = (nums, queries)
    # ret = Solution().solveQueries(*test_case)
    # print(ret)

    nums = [2,0,2]
    queries = [[0,2,1],[0,2,1],[1,1,3]]
    test_case = (nums, queries)
    ret = Solution().minZeroArray(*test_case)
    print(ret)