from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        minPos, maxPos = max(0, startPos - k), min(2 * 10 ** 5, startPos + k)
        psum = [0] * (maxPos - minPos + 1)
        for pos, f in fruits: 
            if pos >= minPos and pos <= maxPos: 
                p = pos - minPos 
                psum[p] = f 
        # print(psum)
        for i in range(1, len(psum)): 
            psum[i] += psum[i - 1]
        ret = 0 
        for i in range(minPos, startPos + 1): 
            ret 
            n_step = startPos - i
            r = startPos + max(k - 2 * n_step, (k - n_step) // 2)
            # print(k - 2 * n_step, (k - n_step) // 2, startPos, r, n_step)
            if r - minPos >= len(psum): 
                break
            ret = max(ret, psum[r - minPos] - psum[i - 1 - minPos] if i - 1 - minPos >= 0 else psum[r - minPos])
        return ret
    
if __name__ == "__main__": 
    fruits = [[2,8],[6,3],[8,6]]
    startPos = 5
    k = 4
    fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]]
    startPos = 5
    k = 4
    fruits = [[0,3],[6,4],[8,5]]
    startPos = 3
    k = 2
    fruits = [[200000,10000]] 
    startPos = 200000
    k = 200000
    ret = Solution().maxTotalFruits(fruits, startPos, k, )
    print(ret)