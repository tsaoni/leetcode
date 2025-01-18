from typing import List
from itertools import chain

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = [["a", "b", "c"], 
                 ["d", "e", "f"], 
                 ["g", "h", "i"], 
                 ["j", "k", "l"], 
                 ["m", "n", "o"], 
                 ["p", "q", "r", "s"], 
                 ["t", "u", "v"], 
                 ["w", "x", "y", "z"]]
        ret = []
        for d in digits: 
            idx = int(d) - 2
            if len(ret) == 0:
                ret = [x for x in table[idx]]
            else: 
                ret = list(chain(*[[x1 + x for x in table[idx]] for x1 in ret]))
        
        return ret
    
if __name__ == "__main__": 
    test_case = "23"
    ret = Solution().letterCombinations(test_case)
    print(ret)