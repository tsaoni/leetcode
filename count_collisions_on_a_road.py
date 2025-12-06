class Solution:
    def countCollisions(self, directions: str) -> int:
        start, end = 0, 0 
        N = len(directions)
        ret = 0
        while end < N: 
            while end < N and directions[start] == directions[end]: 
                end += 1
            if True: 
                if directions[end - 1] == "L": 
                    if start > 0: 
                        if directions[start - 1] in ["S", "R"]: 
                            ret += (end - start)
                elif directions[end - 1] == "R": 
                    if end < N: 
                        if directions[end] in ["S", "L"]: 
                            ret += (end - start)
                       
            # print(directions[start: end], ret)
            start = end 

        return ret 
    
if __name__ == "__main__": 
    directions = "RLRSLL"
    directions = "LLRR"
    ret = Solution().countCollisions(directions)
    print(ret)