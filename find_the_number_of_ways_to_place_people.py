from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        import bisect
        points.sort(key=lambda x: x[1])
        px = sorted([(x, i) for i, (x, _) in enumerate(points)])
        py = sorted([(y, i) for i, (_, y) in enumerate(points)])
        ind_y = [0] * len(points)
        keys = [x for x, _ in px]
        for i, (_, ori) in enumerate(py): 
            ind_y[ori] = i

        ret = 0
        for x, ori in px: 
            y = py[ind_y[ori]][0]
            tx, ty = bisect.bisect_right(keys, x), len(points) 
            cx = -1
            for i in range(tx - 1, -1, -1): 
                _x, _ori = px[i]
                if _ori != ori: 
                    i_y = ind_y[_ori]
                    _y = py[i_y][0]
                    if _y >= y: 
                        if ty == len(points) or ty < len(points) and _y < py[ty][0]: 
                            # print(ty, i_y)
                            if cx != _x:
                                # print(_x, _y, x, y)
                                ret += 1 
                            ty = i_y
                            cx = _x
        return ret
    
if __name__ == "__main__": 
    points = [[1,1],[2,2],[3,3]]
    points = [[6,2],[4,4],[2,6]]
    # points = [[3,1],[1,3],[1,1]]
    # points = [[0,1],[0,2],[0,4]]
    # points = [[1,6],[0,9],[0,3]]
    # points = [[3,4],[5,3],[3,2],[6,2]]
    ret = Solution().numberOfPairs(points)
    print(ret)