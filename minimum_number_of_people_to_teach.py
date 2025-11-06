from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        from collections import defaultdict
        G = defaultdict(list)
        for p1, p2 in friendships: 
            if len(set(languages[p1 - 1]) & set(languages[p2 - 1])) == 0:
                G[p1 - 1].append(p2 - 1)
                G[p2 - 1].append(p1 - 1)
        
        # print(G)
        ret = None
        for l in range(1, n + 1): 
            tmp = 0
            for p, friends in G.items(): 
                if len(friends) > 0 and not l in languages[p]: 
                    tmp += 1 
            ret = min(ret, tmp) if ret is not None else tmp
        

        return ret if ret is not None else 0
    
if __name__ == "__main__": 
    n = 2
    languages = [[1],[2],[1,2]]
    friendships = [[1,2],[1,3],[2,3]]
    n = 3
    languages = [[2],[1,3],[1,2],[3]]
    friendships = [[1,4],[1,2],[3,4],[2,3]]
    ret = Solution().minimumTeachings(n, languages, friendships)
    print(ret)
    