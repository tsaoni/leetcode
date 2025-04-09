from typing import List

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        n_prime = [0]
        N = len(nums)
        for x in range(2, 1001): 
            isprime = True
            for p in primes: 
                if x % p == 0: 
                    isprime = False 
            if isprime: 
                primes.append(x)
                n_prime.append(len(primes) - 1)
            else: 
                n_prime.append(len(primes))
        
        pval = nums[N - 1]
        for idx in range(N - 2, -1, -1): 
            val = nums[idx]
            if val < pval: 
                pval = val 
            else:
                isless = False
                for pi in range(n_prime[val - 1]): 
                    p = primes[pi]
                    if val - p < pval: 
                        pval = val - p
                        isless = True
                        break 
                if not isless: 
                    return False

        return True
        # def find_inc(idx, pval):
        #     if idx < 0: 
        #         return True
        #     if nums[idx] < pval: 
        #         if find_inc(idx - 1, nums[idx]): 
        #             return True

        #     for i in range(n_prime[idx]):
        #         val = nums[idx] - primes[i] 
        #         if val < pval:
        #             if find_inc(idx - 1, val):
        #                 return True
        #     return False
        
        # return find_inc(N - 2, nums[N - 1])
    
if __name__ == "__main__": 
    nums = [4,9,6,10] 
    # nums = [6,8,11,12]
    # nums = [5,8,3]
    test_case = (nums, )
    ret = Solution().primeSubOperation(*test_case)
    print(ret)