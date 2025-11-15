class Solution:
    def maxOperations(self, s: str) -> int:
        op = 0 
        i = 0 
        N = len(s)
        nz = 0
        no = 0
        while i < N: 
            if s[i] == "1": 
                if nz > 0: 
                    op += no
                no += 1 
                nz = 0 
            else: 
                nz += 1 
            i += 1

        if nz > 0: 
            op += no
        
        return op 

if __name__ == "__main__": 
    s = "1001101"
    s = "10011010"
    ret = Solution().maxOperations(s)
    print(ret)