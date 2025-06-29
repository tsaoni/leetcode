from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 10 ** 9 + 7
        nums.sort()
        start = len(nums) 
        ret = 0 
        def exp_mul(num, exp): 
            tmp = exp 
            base = num 
            ret = 1
            while tmp > 0: 
                if tmp & 1:
                    ret *= base 
                    ret %= modulo
                base = base * base 
                base %= modulo
                tmp //= 2 
            return ret
        def search_start(target, ub): 
            l, r = 0, ub 
            while l < r: 
                mid = (l + r) // 2 
                if nums[mid] > target: 
                    r = mid 
                else: 
                    l = mid + 1
            # if l < len(nums) and nums[l] == target: 
            #     l += 1
            return l

        for end in range(len(nums)): 
            start = search_start(target - nums[end], start)
            if start > 0:
                tmp = min(end + 1, start)
                if tmp == end + 1: 
                    ret += exp_mul(2, tmp - 1) #(2 ** (tmp - 1))
                    ret %= modulo
                    # print(2 ** (tmp - 1))
                else:
                    # print("a", tmp)
                    gap = max(end + 1 - tmp - 1, 0) 
                    # add = 1 if nums[end]
                    # print((2 ** tmp - 1) * 2 ** gap)
                    
                    # print(tmp)
                    ret += ((exp_mul(2, tmp) - 1) % modulo) * (exp_mul(2, gap) % modulo) #((2 ** tmp - 1) * 2 ** gap) 
                    ret %= modulo

        return ret % modulo
    
if __name__ == "__main__": 
    nums = [3,5,6,7]
    target = 9
    nums = [3,3,6,8]
    target = 10
    ret = Solution().numSubseq(nums, target)
    print(ret)