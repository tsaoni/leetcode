from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        liters = 0
        l_max_lst, r_max_lst = [0], [0]
        l_max, r_max = 0, 0
        for i in range(1, len(height)): 
            l_max = max(height[i - 1], l_max)
            l_max_lst += [l_max]
            r_max = max(height[len(height) - i], r_max)
            r_max_lst = [r_max] + r_max_lst
        # print(l_max_lst)
        # print(r_max_lst)
        for i in range(1, len(height) - 1): 
            l = l_max_lst[i] #max(height[: i])
            r = r_max_lst[i] #max(height[i + 1:])
            h = min(l, r)
            if h > height[i]: 
                liters += (h - height[i])
        return liters
    
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        import heapq
        mp = {} # area, height, res
        m, n = len(heightMap), len(heightMap[0])
        t = [[-1] * n for _ in range(m)]
        pq = [(heightMap[i][j], i, j) for i in range(m) for j in range(n)]
        heapq.heapify(pq)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        roots = {}
        def find(x): 
            while roots[x] >= 0: 
                x = roots[x]
            return x 
        def merge(p1, p2): 
            roots[p2] = p1
        
        def is_boundary(i, j): 
            return i == 0 or i == m - 1 or j == 0 or j == n - 1
        while len(pq) > 0: 
            height, i, j = heapq.heappop(pq)
            p = -1
            for di, dj in dirs: 
                if i + di >= 0 and i + di < m and j + dj >= 0 and j + dj < n: 
                    if t[i + di][j + dj] >= 0:
                        if p < 0:
                            p = find(t[i + di][j + dj])
                            a, h, r, c = mp[p]
                            inc = (height - h) * a if c else 0
                            mp[p] = (a, height, r + inc, c)
                            # print(height, i, j, (p, mp[p]))
                            # print(p, find(p))
                        else: 
                            _p = find(t[i + di][j + dj])
                            if _p != p:
                                merge(p, _p)
                                _a, _h, _r, _c = mp[_p]
                                a, h, r, c = mp[p]
                                inc = (height - h) * a if c else 0
                                _inc = (height - _h) * _a if _c else 0
                                mp[p] = (_a + a, height, _r + _inc + r + inc, c & _c)
                                # print("merge", height, i, j, (p, _p, mp[p]))
            if p < 0: 
                idx = len(mp)
                if is_boundary(i, j):
                    mp[idx] = (1, height, 0, False)
                else: 
                    mp[idx] = (1, height, 0, True)
                roots[idx] = -1
                p = idx
            else: 
                a, h, r, c = mp[p]
                if is_boundary(i, j):
                    mp[p] = (a + 1, h, r, False) 
                else:
                    mp[p] = (a + 1, h, r, c)
            t[i][j] = p

        ret = 0
        # print(mp)
        # print(roots)
        for idx, (_, _, res, c) in mp.items(): 
            if roots[idx] == -1: 
                ret += res
        return ret

if __name__ == "__main__": 
    # test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
    # ret = Solution().trap(test_case)
    heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    heightMap = [[1,3,3,1,3,2],[3,2,1,3,2,3],[3,3,3,2,3,1]]
    heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
    ret = Solution().trapRainWater(heightMap)
    print(ret)