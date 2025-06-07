class Solution:
    def clearStars(self, s: str) -> str:
        stacks = [[] for _ in range(26)]
        top = -1
        ret = [c for c in s]
        for i, c in enumerate(s): 
            if c == "*": 
                while len(stacks[top]) == 0: 
                    top += 1 
                idx = stacks[top].pop(-1)
                ret[idx] = ""
                ret[i] = ""
            else: 
                idx = ord(c) - ord("a")
                stacks[idx].append(i)
                if top == -1 or idx < top: 
                    top = idx 
            
        return "".join(ret)
    
if __name__ == "__main__": 
    s = "aaba*"
    s = "abc"
    ret = Solution().clearStars(s)
    print(ret)