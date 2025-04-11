class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ret = 0
        for num in range(low, high + 1): 
            acc = [0]
            while num > 0: 
                acc.append(acc[-1] + num % 10)
                num //= 10
            if len(acc) % 2 == 1: 
                hidx = len(acc) // 2
                if acc[hidx] == acc[-1] / 2: 
                    ret += 1
        return ret
        # unfinished (this might be harder)
        # def count(num): 
        #     n_digit = 0 
        #     while num // (10 ** n_digit) > 0: 
        #         n_digit += 1 
        #     cnt = 0 
        #     for d in range(2, n_digit + 1, 2): 
        #         if d == n_digit: 
        #             pass 
        #         else: 
        #             d // 2
        #     return 
        # return count(high) - count(low - 1)
    
if __name__ == "__main__": 
    low = 1200 
    high = 1230
    test_case = (low, high)
    ret = Solution().countSymmetricIntegers(*test_case)
    print(ret)