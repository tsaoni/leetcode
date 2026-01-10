class Solution:
    def numberOfWays(self, corridor: str) -> int:
        accs = 0 
        # ret, tmp = 0, 0
        pre, cur = 1, 0
        N = len(corridor)
        modulo = 10 ** 9 + 7
        for i in range(N): 
            x = corridor[i]
            if x == "S": 
                accs += 1 
            # if accs == 2: 
            #     ret += 1 
            
            if accs > 0 and accs % 2 == 0: 
                # tmp += pre 
                cur += 1 
            else: 
                if cur > 0:
                    # ret += tmp 
                    pre = pre * cur 
                    pre %= modulo
                    cur = 0
                # tmp = 0
        if accs == 0: 
            pre = 0
        elif accs == 2: 
            pre = 1
        return pre if accs % 2 == 0 else 0
      
    
if __name__ == "__main__": 
    corridor = "SSPPSPS"
    corridor = "PPSPSP"
    corridor = "S"
    corridor = "SPPSPSSSPPS"
    corridor = "P"
    ret = Solution().numberOfWays(corridor)
    print(ret)