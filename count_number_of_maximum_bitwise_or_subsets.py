from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        import math
        
        n_visited = 2 ** 16
        visited = [False] * n_visited
        max_state = 0 
        for num in nums: 
            max_state |= num
        
        def count2(idx, vidx, state):
            if idx == len(nums): 
                if state == max_state: 
                    visited[vidx] = True 
            else:
                count2(idx + 1, vidx, state)
                vidx |= (1 << idx)
                state |= nums[idx]
                count2(idx + 1, vidx, state)


        count2(0, 0, 0)
        return sum(visited)
    
if __name__ == "__main__": 
    nums = [3,1]
    # nums = [2,2,2]
    ret = Solution().countMaxOrSubsets(nums)
    print(ret)