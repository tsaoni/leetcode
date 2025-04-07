from typing import List
from collections import Counter
from copy import deepcopy

class Solution:
    def canPartition4(self, nums: List[int]) -> bool:
        """
        similar to origin solution I came out
        """
        total = sum(nums)
        if total % 2 == 1: 
            return False 
        else: 
            k = total // 2
            cur = {0}
            for num in nums: 
                ncur = set()
                for c in cur: 
                    if c + num == k: 
                        return True 
                    elif c + num < k: 
                        ncur |= {c + num}
                cur |= ncur
            return False
        
    def canPartition3(self, nums: List[int]) -> bool:
        """
        magic solution
        """
        total = sum(nums)
        if total % 2 == 1: 
            return False 
        else: 
            k = total // 2 
            dp = [False] * (k + 1)
            dp[0] = True 
            for n in nums: 
                for i in range(k, n - 1, -1): # backward!!
                    dp[i] |= dp[i - n]

            return dp[k]
    
    def canPartition2(self, nums: List[int]) -> bool:
        """
        too bad, exponential time
        """
        total = sum(nums)
        if total % 2 == 1: 
            return False 
        else: 
            k = total // 2 
            cands = []
            for n in nums: 
                if n == k: 
                    return True 
                elif n < k: 
                    cands.append(n)
            def find_equal(idx, acc): 
                if acc == k: 
                    return True 
                elif acc > k: 
                    return False
                else: 
                    ret = False
                    for i in range(idx, len(cands)): 
                        ret |= find_equal(i + 1, acc + cands[i])
                    return ret
            
            return find_equal(0, 0)

    def canPartition1(self, nums: List[int]) -> bool:
        """
        take too much time bang
        """
        total = sum(nums)
        if total % 2 == 1: 
            return False 
        else: 
            k = total // 2 
            acc = [[] for _ in range(k)]
            cnt = Counter()
            start = 0
            cands = set()
            for n in nums: 
                if n == k: 
                    return True
                elif n < k:
                    tmp = Counter()
                    tmp[n] = 1
                    acc[n - 1] = [tmp]
                    start = max(start, n)
                    cnt[n] += 1
                    cands |= {n}
    
            for i in range(start, k): 
                # for n in nums: 
                for n in cands:
                    if len(acc[i - n]) > 0: 
                        for x in acc[i - n]: 
                            if x[n] < cnt[n]: 
                                tmp = deepcopy(x)
                                tmp[n] += 1
                                acc[i].append(tmp)
            
            # print(cnt)
            # print(acc)
            return True if len(acc[k - 1]) > 0 else False
            


    def canPartition(self, nums: List[int]) -> bool:
        """
        wrong implementation
        (will result in duplicate values)
        """
        total = sum(nums)
        if total % 2 == 1: 
            return False 
        else: 
            k = total // 2 
            nums.sort()
            curl = nums
            # N = len(nums)
            for n in nums: 
                if n == k: 
                    return True
            
            def merge(la, lb): 
                retl = []
                while len(la) > 0 and len(lb) > 0: 
                    if la[0] < lb[0]: 
                        retl.append(la.pop(0))
                    else: 
                        retl.append(lb.pop(0))
                while len(la) > 0: 
                    retl.append(la.pop(0)) 
                while len(lb) > 0: 
                    retl.append(lb.pop(0))
                return retl
            
            while True: 
                print(curl)
                val = curl.pop(0)
                newl = []
                for n in curl: 
                    if n + val == k: 
                        return True 
                    elif n + val < k: 
                        newl.append(n + val)
                if len(newl) == 0: 
                    return False 
                # merge
                curl = merge(curl, newl)
        
    
if __name__ == "__main__": 
    nums = [1,5,11,5] 
    # nums = [1,2,3,5]
    # nums = [1,1,2]
    # nums = [2,2,3,5]
    test_case = (nums, )
    ret = Solution().canPartition4(*test_case)
    print(ret)