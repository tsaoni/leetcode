from typing import List

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xnums = [n ^ k for n in nums]
        ret = sum(nums)
        d = sorted([n1 - n2 for n1, n2 in zip(xnums, nums)])
        # print(ret, d)
        for i in range(len(d) - 1, 0, -2): 
            if d[i] + d[i - 1] > 0: 
                ret += (d[i] + d[i - 1])
            else: 
                break
        return ret
    
if __name__ == "__main__": 
    nums = [1,2,1]
    k = 3
    edges = [[0,1],[0,2]]
    nums = [2,3]
    k = 7
    edges = [[0,1]]
    # nums = [24,78,1,97,44] 
    # k = 6 
    # edges = [[0,2],[1,2],[4,2],[3,4]]
    ret = Solution().maximumValueSum(nums, k, edges)
    print(ret)