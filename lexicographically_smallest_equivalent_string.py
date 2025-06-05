class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        import string
        parents = [-1] * 26 
        def find(i): 
            return i if parents[i] < 0 else find(parents[i])
        
        for c1, c2 in zip(s1, s2): 
            get_idx_fn = lambda c: ord(c) - ord("a")
            i1, i2 = get_idx_fn(c1), get_idx_fn(c2)
            p1, p2 = find(i1), find(i2)
            if p1 < p2:
                parents[p2] = p1 
            if p2 < p1: 
                parents[p1] = p2 
        
        roots = []
        for i in range(26): 
            roots.append(find(i)) 

        return "".join([string.ascii_lowercase[roots[get_idx_fn(c)]] for c in baseStr])
    
if __name__ == "__main__": 
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"
    ret = Solution().smallestEquivalentString(s1, s2, baseStr)
    print(ret)