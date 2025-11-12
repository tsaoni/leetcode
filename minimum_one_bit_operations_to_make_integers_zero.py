class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0: 
            return 0
        tmp = n 
        d = 0 
        op = 0
        digits = []
        while tmp > 0: 
            if tmp & 1: 
                digits.insert(0, d)
            d += 1 
            tmp >>= 1
        
        cur = 1
        for d in digits: 
            op += cur * (2 ** (d + 1) - 1)
            cur = -cur
            


        return op 
    
if __name__ == "__main__": 
    n = 6
    n = 333
    ret = Solution().minimumOneBitOperations(n)
    print(ret)