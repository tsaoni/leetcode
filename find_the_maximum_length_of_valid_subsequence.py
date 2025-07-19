from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        # if nums[0] % 2 == 1:
        #     pre = [[[1, 1], [1, 1]] for _ in range(N)] 
        # else: 
        #     pre = [[[1, 1], [1, 1]] for _ in range(N)] 
        pre = [[[0, 0], [0, 0]] for _ in range(N)] 
        for i in range(N): 
            if nums[i] % 2 == 1: 
                pre[i][0][0] = pre[i - 1][0][0] 
                pre[i][0][1] = pre[i - 1][0][1] + 1
                pre[i][1][0] = pre[i - 1][1][0] 
                pre[i][1][1] = pre[i - 1][1][0] + 1
            else: 
                pre[i][0][0] = pre[i - 1][0][0] + 1
                pre[i][0][1] = pre[i - 1][0][1] 
                pre[i][1][0] = pre[i - 1][1][1] + 1
                pre[i][1][1] = pre[i - 1][1][1]

        # print(pre)
        return max(pre[-1][0][0], pre[-1][0][1], pre[-1][1][0], pre[-1][1][1])
    
    def maximumLength_2(self, nums: List[int], k: int) -> int:
        from itertools import chain
        N = len(nums)
    
        pre = [[0] * k for _ in range(k)] 
        for i in range(N): 
            # nxt = [[0] * k for _ in range(k)] 
            remain = nums[i] % k
            for j in range(k): 
                # for r in range(k): 
                    _r = (j + k - remain) % k
                    # if r == remain:
                    pre[j][remain] = pre[j][_r] + 1 
                    # else: 
                    #     pre[j][r] = pre[j][_r]
          
            # pre = nxt

        # print(pre)
        return max(list(chain(*pre)))
    

if __name__ == "__main__": 
    nums = [1,2,3,4]
    # nums = [1,2,1,1,2,1,2]
    nums = [1,3]
    # ret = Solution().maximumLength(nums)
    
    nums = [1,2,3,4,5]
    k = 2
    nums = [1,4,2,3,1,4]
    k = 3
    # nums = [1,2,3,10,2] 
    # k = 6
    ret = Solution().maximumLength_2(nums, k)
    print(ret)