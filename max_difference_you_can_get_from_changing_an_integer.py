class Solution:
    def maxDiff(self, num: int) -> int:
        masks = [0] * 10 
        tmp = num 
        cur = 1
        maxd, mind = 9, 1
        top = -1
        while tmp > 0: 
            masks[tmp % 10] += cur 
            cur *= 10 
            if tmp % 10 < 9:
                maxd = tmp % 10 
            if tmp % 10 > 1:
                mind = tmp % 10 
            top = tmp % 10
            tmp //= 10 
        a = masks[maxd] * (9 - maxd)
        b = masks[mind] * (mind - 1 if mind == top else mind)
        # print(masks, a, b)
        return a + b 
    
if __name__ == "__main__": 
    num = 555
    num = 9
    ret = Solution().maxDiff(num)
    print(ret)