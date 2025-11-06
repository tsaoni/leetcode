class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        lst = []
        tmp = numBottles 
        while tmp > 0: 
            r = tmp % numExchange 
            lst.insert(0, r)
            tmp = tmp // numExchange 
        ret = numBottles
        while len(lst) > 1: 
            # print(lst)
            _lst = [lst[-1]]
            exp = 1
            for i in range(len(lst)): 
                if i > 1: 
                    _lst.insert(0, 0)
                if i > 0:
                    ret += lst[-i - 1] * exp 
                    exp *= numExchange
                    _lst[0] += lst[-i - 1]
            lst = _lst
            # print(lst)
            if lst[0] >= numExchange: 
                lst[0] -= numExchange
                if len(lst) > 1: 
                    lst[1] += 1 
                else: 
                    lst.insert(0, 1)
            # print(lst, ret)
        return ret
    
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles 
        em = numBottles 
        while em >= numExchange: 
            em -= numExchange 
            numExchange += 1 
            ret += 1 
            em += 1 
        return ret

if __name__ == "__main__": 
    numBottles = 9
    numExchange = 3
    numBottles = 15
    numExchange = 4
    # numBottles = 12
    # numExchange = 4
    ret = Solution().numWaterBottles(numBottles, numExchange)
    print(ret)