from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        cands = Counter()
    
        for d in digits: 
            cands[d] += 1
        
        ret = []
        def find(n, i): 
            if i == 3: 
                if n % 2 == 0:
                    ret.append(n)
            else:
                for k in sorted(cands): 
                    if not (i == 0 and k == 0) and cands[k] > 0:
                        cands[k] -= 1
                        find(n * 10 + k, i + 1)
                        cands[k] += 1
                
        find(0, 0)
        return ret
    
if __name__ == "__main__": 
    digits = [2,1,3,0]
    ret = Solution().findEvenNumbers(digits)
    print(ret)