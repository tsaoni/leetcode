class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        pattern = {
            "1": "11", 
            "11": "21", 
            "111": "31",
            "2": "12", 
            "22": "22", 
            "222": "32", 
            "3": "13", 
            "33": "23", 
            "333": "33", 
            
        }
        for i in range(n - 1): 
            ns = ""
            start = 0
            for i in range(len(s)): 
                if s[start: i + 1] not in pattern: 
                    ns += pattern[s[start: i]]
                    start = i 
            ns += pattern[s[start: len(s)]]
            s = ns

        return s
    
if __name__ == "__main__": 
    ret = Solution().countAndSay(7)
    print(ret)