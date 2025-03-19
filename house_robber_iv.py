from typing import List

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def good(num): 
            visited = False
            acc = 0
            for n in nums: 
                if n > num: 
                    visited = False
                else: 
                    if not visited: 
                        visited = True 
                        acc += 1 
                    else: 
                        visited = False 
                if acc == k: 
                    return True
            return False
        
        left, right = min(nums), max(nums)
        while True: 
            mid = (left + right) // 2
            if mid == right: 
                break
            if good(mid): 
                right = mid 
            else: 
                left = mid + 1

        return left
    
if __name__ == "__main__": 
    nums = [2,3,5,9]
    k = 2
    nums = [2,7,9,3,1]
    k = 2
    test_case = (nums, k)
    ret = Solution().minCapability(*test_case)
    print(ret)