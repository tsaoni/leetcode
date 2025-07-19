from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        import heapq 
        n = len(nums) // 3
        arr1 = [(-nums[i], i) for i in range(n)]
        tmp = sorted([(nums[i], i) for i in range(n, 3 * n)])
        arr2, rem = [(tmp[i][1], tmp[i][0]) for i in range(n, 2 * n)], [(-tmp[i][0], tmp[i][1]) for i in range(n)]
        sum1, sum2 = sum([-x[0] for x in arr1]), sum([x[1] for x in arr2])
        heapq.heapify(arr1)
        heapq.heapify(arr2)
        heapq.heapify(rem)

        ret = sum1 - sum2
        _ret = ret
        # print(ret)
        for i in range(n, 2 * n): 
            d = 0
            if nums[i] < -arr1[0][0]: 
                _n, _i = heapq.heappop(arr1) 
                heapq.heappush(arr1, (-nums[i], i))
                d += nums[i] + _n
                # print("a", nums[i], _n)
            if i == arr2[0][0]: 
                _i2, _n2 = heapq.heappop(arr2)
                while rem[0][1] <= i: 
                    heapq.heappop(rem)
                _n, _i = heapq.heappop(rem)
                heapq.heappush(arr2, (_i, -_n))
                d += _n + _n2
                # print(_n, _n2)
            # print("d", d)
            # if d < 0: 
            #     import pdb 
            #     pdb.set_trace()
            _ret = _ret + d
            ret = min(ret, _ret)
        return ret 
    

if __name__ == "__main__": 
    nums = [3,1,2]
    # nums = [7,9,5,8,1,3]
    # nums = [16,46,43,41,42,14,36,49,50,28,38,25,17,5,18,11,14,21,23,39,23]
    ret = Solution().minimumDifference(nums)
    print(ret)