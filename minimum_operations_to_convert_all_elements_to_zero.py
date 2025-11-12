from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stk = []
        op = 0
        for n in nums: 
            if len(stk) == 0: 
                stk.append(n)
            else: 
                while len(stk) > 0 and stk[-1] > n: 
                    stk.pop(-1)
                    op += 1 
                if len(stk) == 0 or len(stk) > 0 and stk[-1] < n: 
                    stk.append(n)

        while len(stk) > 0 and stk[0] == 0: 
            stk.pop(0)
        op += len(stk)
        return op 
    
if __name__ == "__main__": 
    nums = [0,2]
    nums = [3,1,2,1]
    nums = [1,2,1,2,1,2]
    ret = Solution().minOperations(nums)
    print(ret)