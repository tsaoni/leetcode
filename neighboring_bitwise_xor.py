from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # should have even number of ones 
        return sum(derived) % 2 == 0
    
if __name__ == "__main__": 
    derived = [1,1,0]
    test_case = (derived, )
    ret = Solution().doesValidArrayExist(*test_case)
    print(ret)