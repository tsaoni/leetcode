class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        n_ops = 0
        tmp = num1
        def bitcount(n): 
            c = 0 
            while n > 0: 
                c += n & 1 
                n >>= 1 
            return c 
        for _ in range(60): 
            tmp -= num2 
            n_ops += 1 
            if tmp >= n_ops and bitcount(tmp) <= n_ops:
                # print(tmp)
                return n_ops
        return -1 
    
if __name__ == "__main__": 
    num1 = 3
    num2 = -2
    num1 = 5
    num2 = 7
    num1 = 110 
    num2 = 55
    ret = Solution().makeTheIntegerZero(num1, num2)
    print(ret)