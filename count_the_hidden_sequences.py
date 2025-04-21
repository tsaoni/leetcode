from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        start = 0 
        minv = maxv = 0
        for d in differences: 
            start += d 
            minv = min(minv, start)
            maxv = max(maxv, start)
        return max(upper - (lower + (maxv - minv)) + 1, 0)
    

    
if __name__ == "__main__": 
    differences = [1,-3,4]
    lower = 1
    upper = 6
    test_case = (differences, lower, upper)
    ret = Solution().numberOfArrays(*test_case)
    print(ret)