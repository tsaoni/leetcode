from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        using prefix sum
        complexity: 
        """
        def detect_special(x): 
            ret = True
            for i in range(len(x) - 1): 
                if (x[i] + x[i + 1]) % 2 == 0: 
                    ret = False
                    break
            return ret
        parities = []
        cnt = 0
        for i in range(len(nums) - 1): 
            tmp = 0
            if detect_special(nums[i: i + 2]): 
                tmp = 1
            cnt += tmp
            parities += [cnt]
        # parities += [cnt]
        parities = [0] + parities
        
        ret = []
        # print(parities)
        for start, end in queries: 
            tmp = parities[end] - parities[start] #all(parities[start: end])
            if tmp == end - start: 
                ret += [True]
            else: ret += [False]
        return ret
    
    def isArraySpecial_1(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        """
        TLE
        n: len(nums)
        m: len(queries)
        complexity: O(n * m)
        """
        ret = []
        def detect_special(x): 
            ret = True
            for i in range(len(x) - 1): 
                if (x[i] + x[i + 1]) % 2 == 0: 
                    ret = False
                    break
            return ret
        
        for start, end in queries: 
            tmp = detect_special(nums[start: end + 1])
            ret += [tmp]
        return ret
    
if __name__ == "__main__": 
    # nums = [3,4,1,2,6]
    # queries = [[0,4]]
    nums = [4,3,1,6]
    queries = [[0,2],[2,3]]
    test_case = (nums, queries)
    ret = Solution().isArraySpecial(*test_case)
    print(ret)