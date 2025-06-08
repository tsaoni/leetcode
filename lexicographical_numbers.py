from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # nums = []
        # while n > 0: 
        #     nums.insert(0, n % 10)
        #     n //= 10 
        ret = [1]
        # print(nums)
        num = 1
        while len(ret) < n: 
            if num * 10 <= n: 
                num *= 10 
                ret.append(num)
            elif num % 10 < 9 and num + 1 <= n: 
                num += 1 
                ret.append(num)
            else: 
                while num % 10 == 9:
                    num //= 10 
                num += 1 
                if num <= n: 
                    ret.append(num)
        return ret
    
if __name__ == "__main__": 
    n = 1000
    ret = Solution().lexicalOrder(n)
    print(ret)