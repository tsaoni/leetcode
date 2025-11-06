from typing import List

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        cur = set()
        ret = set() 
        for n in arr: 
            _cur = set()
            for c in cur: 
                tmp = c | n 
                _cur.add(tmp)
         
            _cur.add(n)
            ret |= _cur
            cur = _cur
    
        return len(ret)
    
if __name__ == "__main__": 
    arr = [0]
    arr = [1,1,2]
    arr = [1,2,4]
    arr = [3,11]
    arr = [13,4,2]
    arr = [1,11,6,11]
    arr = [121,62,106,124,40,54]
    ret = Solution().subarrayBitwiseORs(arr)
    print(ret)