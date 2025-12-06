from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        from collections import Counter
        cnt = Counter()
        # N = len(points)
        modulo = 10 ** 9 + 7
        for x, y in points: 
            cnt[y] += 1 
        ret = 0 
        c2 = lambda x: x * (x - 1) // 2
        tot = 0
        for x, c in cnt.items(): 
            cnt[x] = c2(c) 
            tot += cnt[x]
        for _, c in cnt.items(): 
            tot -= c
            ret += tot * c
            ret %= modulo
        return ret 
    
    def countTrapezoids_2(self, points: List[List[int]]) -> int:
        
        return 0 
    
if __name__ == "__main__": 
    points = [[1,0],[2,0],[3,0],[2,2],[3,2]]
    # points = [[0,0],[1,0],[0,1],[2,1]]
    ret = Solution().countTrapezoids(points)
    print(ret)