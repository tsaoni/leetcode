from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        Nw = len(weights)
        cands = [weights[i] + weights[i + 1] for i in range(Nw - 1)]
        cands.sort()
        # print(cands)
        ret = 0
        for idx in range(k - 1): 
            ret += (cands[-idx - 1] - cands[idx])
        return ret
    
if __name__ == "__main__": 
    weights = [1,3,5,1]
    k = 2
    weights = [1, 3]
    k = 2
    test_case = (weights, k)
    ret = Solution().putMarbles(*test_case)
    print(ret)