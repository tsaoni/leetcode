from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        N = len(fruits)
        tl = 0
        for i in range(N - 1): 
            tl += fruits[i][i]

        for i in range(N - 1): 
            start = max(N - i - 1, i + 1)
            # print(start)
            if i == 0: 
                _dp = [fruits[i][N - 1]]
            else:
                if N - i - 1 > i: 
                    dp.insert(0, dp[0])
                _dp = []
                for j in range(start, N): 
                    # if j == start:
                    #     if N - i - 1 >= i: 
                    #         val = max(dp[: 2]) + fruits[i][j]
                    #         _dp.append(val)
                    # else: 
                    if N - i - 1 >= i: 
                        mid = j - start
                    else: 
                        mid = j - start + 1
                    # import pdb 
                    # pdb.set_trace()
                    val = max(dp[max(0, mid - 1): mid + 2]) + fruits[i][j]
                    _dp.append(val)
                # import pdb 
                # pdb.set_trace()
            dp = _dp
            # print(dp)
        tr = dp[0]
        
        for i in range(N - 1): 
            start = max(N - i - 1, i + 1)
            if i == 0: 
                _dp = [fruits[N - 1][i]]
            else:
                if N - i - 1 > i: 
                    dp.insert(0, dp[0])
                _dp = []
                for j in range(start, N): 
                    # if j == start:
                    #     if N - i - 1 >= i: 
                    #         val = max(dp[: 2]) + fruits[j][i]
                    #         _dp.append(val)
                    # else: 
                    if N - i - 1 >= i: 
                        mid = j - start
                    else: 
                        mid = j - start + 1
                    val = max(dp[max(0, mid - 1): mid + 2]) + fruits[j][i]
                    _dp.append(val)
            dp = _dp
        bl = dp[0]

        return tl + tr + bl + fruits[-1][-1]
    
if __name__ == "__main__": 
    fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]
    fruits = [[1,1],[1,1]]
    ret = Solution().maxCollectedFruits(fruits)
    print(ret)