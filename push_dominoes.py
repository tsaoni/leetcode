class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dcnt = 0
        pact = ""
        s = ""
        for c in dominoes: 
            if c == ".": 
                dcnt += 1 
            else: 
                if pact == "": 
                    if c == "L": 
                        s += "L" * dcnt 
                    else: 
                        s += "." * dcnt 
                    
                elif pact == "L": 
                    if c == "L": 
                        s += "L" * dcnt  
                    else: 
                        s += "." * dcnt 
                else: 
                    if c == "R": 
                        s += "R" * dcnt 
                    else: 
                        s += "R" * (dcnt // 2) + "." * (dcnt & 1) + "L" * (dcnt // 2)
                s += c
                dcnt = 0
                pact = c 
        if pact == "R": 
            s += "R" * dcnt 
        else:
            s += "." * dcnt
        return s
    
if __name__ == "__main__": 
    dominoes = "RR.L"
    # dominoes = ".L.R...LR..L.."
    ret = Solution().pushDominoes(dominoes)
    print(ret)