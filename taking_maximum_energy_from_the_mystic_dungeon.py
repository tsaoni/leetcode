from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        psum = [None] * k 
        ret = -1000
        for i in range(n - 1, -1, -1): 
            idx = i % k
            psum[idx] = energy[i] + psum[idx] if psum[idx] is not None else energy[i]
            ret = max(ret, psum[idx])
        return ret
    
if __name__ == "__main__": 
    energy = [5,2,-10,-5,1]
    k = 3
    energy = [-2,-3,-1]
    k = 2
    ret = Solution().maximumEnergy(energy, k)
    print(ret)