from typing import List

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        import math
        nums.sort() 
        x = math.sqrt(nums[-1])
        n = math.ceil(x)
        n = n + 1 if x == n else n
        
        primes = []
        for i in range(2, n): 
            isprime = True 
            for p in primes: 
                if i % p == 0: 
                    isprime = False 
                    break 
            if isprime: 
                primes.append(i)

        cur = 0 
        dp = [[0, 0] for _ in range(len(nums))] 
        for i in primes:
            while cur < len(nums) and i > math.sqrt(nums[cur]): 
                cur += 1
            for k in range(cur, len(nums)): 
                if nums[k] % i == 0: 
                    x = nums[k] // i
                    # print(k, nums[k], i, x)
                    dp[k][0] += len(set({x, i}))
                    dp[k][1] += (x + i if x != i else x)
                    if x % i == 0 and x // i > 1 and x // i != i: 
                        dp[k][0] += 1
            # if i == math.sqrt(nums[cur]): 
            #     cur += 1
            # print(dp)

        ret = 0 
        for i in range(len(nums)): 
            if dp[i][0] == 2: 
                ret += (dp[i][1] + 1 + nums[i])
        
        return ret 

if __name__ == "__main__": 
    nums = [21,4,7]
    # nums = [21,21,21]
    # nums = [1,2,3,4,5]
    # nums = [2]
    # nums = [7286,18704,70773,8224,91675]
    # nums = [1,2,3,4,5,6,7,8,9,10]
    ret = Solution().sumFourDivisors(nums)
    print(ret)