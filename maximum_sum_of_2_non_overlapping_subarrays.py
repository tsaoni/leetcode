from typing import List

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        acc = sum(nums[: k])
        slst = [acc]
        for i in range(1, N - k + 1): 
            acc += nums[i + k - 1]
            acc -= nums[i - 1]
            slst.append(acc)
        
        Ns = N - k + 1
        maxl, maxr = [0], [Ns - 1]
        for i in range(1, Ns): 
            idx = i if slst[i] > slst[maxl[-1]] else maxl[-1]
            maxl.append(idx)
        for i in range(Ns - 2, -1, -1): 
            idx = i if slst[i] >= slst[maxr[0]] else maxr[0]
            maxr.insert(0, idx)
        tmp = -1
        ret = [N]
        # print(maxl, maxr)
        for i in range(k, Ns - k): 
            lidx, ridx = maxl[i - k], maxr[i + k]
            if slst[lidx] + slst[i] + slst[ridx] > tmp: 
                tmp = slst[lidx] + slst[i] + slst[ridx] 
                ret = [lidx, i, ridx] 
                # print(ret)
            elif slst[lidx] + slst[i] + slst[ridx] == tmp: 
                ret = min(ret, [lidx, i, ridx])
                # print(ret)
        # print(tmp)
        return ret
    
if __name__ == "__main__": 
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    nums = [1,2,1,2,1,2,1,2,1]
    k = 2
    ret = Solution().maxSumOfThreeSubarrays(nums, k)
    print(ret)