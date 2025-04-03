from typing import List

class Solution:
    
    def maximumTripletValue1(self, nums: List[int]) -> int: 
        nk = nums[2]
        ni = nums[0]
        maxL = 0
        ret = 0
        N = len(nums)
        for i in range(1, N - 1): 
            cur = nums[i]
            nk = nums[i + 1]
            maxL = max(maxL, ni - cur)
            ret = max(ret, maxL * nk)
            ni = max(ni, cur)
        return ret

    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        time complexity: O(n)
        """
        kidxs = [len(nums) - 1]
        for i in range(len(nums) - 2, 1, -1): 
            if nums[kidxs[0]] > nums[i]: 
                kidxs.insert(0, kidxs[0])
            else: 
                kidxs.insert(0, i)

        # ni, nj, nk = nums[0], nums[1], nums[kidxs[0]]
        ret = 0
        max_v = nums[0]
        for nidx, num in enumerate(nums[1: -1]): 
            k = kidxs[nidx]
            if (max_v - num) * nums[k] > ret: 
                ret = (max_v - num) * nums[k]
            if num > max_v: 
                max_v = num 

            # k = kidxs[nidx]
            # if nidx < k - 2:
            #     _nk = nums[k]
            #     if (ni - num) * _nk > (nj - num) * _nk: 
            #         if (ni - num) * _nk > (ni - nj) * nk: 
            #             nj = num 
            #             nk = _nk
            #     else: 
            #         if (nj - num) * _nk > (ni - nj) * nk: 
            #             import pdb 
            #             pdb.set_trace()
            #             ni = nj 
            #             nj = num
            #             nk = _nk
        # print(kidxs)
        # print(ni, nj, nk)
        return ret
    
if __name__ == "__main__": 
    nums = [12,6,1,2,7]
    nums = [1,10,3,4,19]
    nums = [1,2,3]
    nums = [8,6,3,13,2,12,19,5,19,6,10,11,9]
    nums = [2, 3, 1]
    test_case = (nums, )
    ret = Solution().maximumTripletValue1(*test_case)
    print(ret)