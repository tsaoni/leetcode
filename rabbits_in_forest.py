from typing import List 
from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter()
        v = 0 
        for ans in answers: 
            if cnt[ans] % (ans + 1) == 0: 
                v += (ans + 1)
            cnt[ans] += 1 
        return v
    
if __name__ == "__main__": 
    answers = [10,10,10] 
    test_case = (answers, )
    ret = Solution().numRabbits(*test_case)
    print(ret)