from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        bits = []
        tmp = k - 1 
        while tmp > 0: 
            bits.append(tmp & 1)
            tmp //= 2 
        c = 0
        for i in range(len(bits)): 
            if bits[i] and operations[i]: 
                c = (c + 1) % 26 

        return chr(97 + c)
    
if __name__ == "__main__": 
    k = 5
    operations = [0,0,0]
    # k = 10
    # operations = [0,1,0,1]
    ret = Solution().kthCharacter(k, operations)
    print(ret)