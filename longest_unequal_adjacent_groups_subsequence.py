from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ret = []
        p = -1
        for w, idx in zip(words, groups): 
            if p != idx: 
                ret.append(w)
                p = idx 
        return ret
    
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        N = len(words)
        dp = [0] * N 
        parents = [-1] * N
        def dist(s1, s2): 
            if len(s1) == len(s2): 
                return sum([c1 != c2 for c1, c2 in zip(s1, s2)])
            return -1
        
        pg = -1 
        midx = 0
        for i, (w, g) in enumerate(zip(words, groups)): 
            if pg != g: 
                # pidx = i 
                pg = g
            for j in range(i): 
                if groups[i] != groups[j] and dist(words[j], w) == 1: 
                    if dp[i] < dp[j] + 1: 
                        dp[i] = dp[j] + 1 
                        parents[i] = j 
                        if dp[i] > dp[midx]: 
                            midx = i 
        
        ret = []
        p = midx
        while p >= 0: 
            ret.insert(0, words[p])
            p = parents[p]

        return ret

if __name__ == "__main__": 
    words = ["bab","dab","cab"]
    groups = [1,2,2]

    words = ["a","b","c","d"]
    groups = [1,2,3,4]
    ret = Solution().getWordsInLongestSubsequence(words, groups)
    print(ret)