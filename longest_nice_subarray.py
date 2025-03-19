from typing import List
from itertools import chain
from collections import defaultdict
import heapq

class Solution:

    def longestNiceSubarray1(self, nums: List[int]) -> int:
        """
        sliding window
        """
        max_num = max(nums) 
        n_digits = 1 
        while max_num // 2 ** (n_digits) > 0: 
            n_digits += 1 
        mask = [0 for _ in range(n_digits)]
        n_idx = []
        r = [0, 0]
        f = [0, 0]
        for i, num in enumerate(nums): 
            tmp = num
            idxs = []
            idx = 0
            while tmp > 0: 
                if tmp % 2 == 1: 
                    idxs += [idx]
                tmp = tmp // 2 
                idx += 1 
            n_idx += [idxs]
            if sum([mask[x] for x in idxs]) == 0: 
                for x in idxs: 
                    mask[x] = 1 
                r[1] = i 
                if r[1] - r[0] > f[1] - f[0]: 
                    f = [r[0], r[1]]
            else: 
                start = r[0]
                while True: 
                    for idx in n_idx[start]: 
                        mask[idx] = 0 
                    start += 1
                    if sum([mask[x] for x in idxs]) == 0: 
                        break 

                for x in idxs: 
                    mask[x] = 1
                r[0] = start 
                r[1] = i
            # import pdb 
            # pdb.set_trace()

        # print(nums[slice(f[0], f[1] + 1)])
        return f[1] - f[0] + 1
        

    def longestNiceSubarray(self, nums: List[int]) -> int:
        """
        non contigious!!!
        """
        max_num = max(nums) 
        n_digits = 1 
        while max_num // 2 ** (n_digits) > 0: 
            n_digits += 1 
        d_lst = [[] for _ in range(n_digits)]
        n_lst = [[] for _ in nums]
        for i, num in enumerate(nums): 
            tmp = num
            idx = 0
            while tmp > 0: 
                if tmp % 2 == 1: 
                    d_lst[idx] += [i]
                    n_lst[i] += [idx]
                tmp = tmp // 2 
                idx += 1 
        # print(d_lst)
        # print(n_digits)
        cnts = []
        for lst in n_lst: 
            c = len(set(chain(*[d_lst[x] for x in lst]))) 
            cnts += [c]
        # print(cnts)
        mask = [0 for _ in range(n_digits)]
        cnts_d = defaultdict(list)
        for i, c in enumerate(cnts): 
            cnts_d[c] += [i]
        heapq.heapify(cnts)
        ret = 0 
        tmp = []
        while len(cnts) > 0: 
            c = heapq.heappop(cnts)
            idx = cnts_d[c].pop(0)
            n_hit = sum([mask[x] for x in n_lst[idx]])
            if n_hit == 0:
                for x in n_lst[idx]: 
                    mask[x] += 1 
                ret += 1 
                tmp += [nums[idx]]

        print(tmp)
        print(n_lst[8])
        print(n_lst[9])
        print(n_lst[10])
        print(n_lst[12])
        print(mask)
        return ret
    
if __name__ == "__main__": 
    nums = [1,3,8,48,10] 
    nums = [3,1,5,11,13]
    nums = [904163577,321202512,470948612,490925389,550193477,87742556,151890632,655280661,4,263168,32,573703555,886743681,937599702,120293650,725712231,257119393]
    test_case = (nums, )
    ret = Solution().longestNiceSubarray1(*test_case)
    print(ret)