class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        st = [0] * k 
        n = 1 
        l = 1
        if k == 1: 
            return 1
        while st[n] == 0: 
            st[n] = 1
            while n < k: 
                n = n * 10 + 1 
                l += 1
            n = n % k
            if n == 0: 
                return l
            
            # print(n)
        return -1
    
if __name__ == "__main__": 
    k = 2
    ret = Solution().smallestRepunitDivByK(k)
    print(ret)