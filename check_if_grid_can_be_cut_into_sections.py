from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        xs = [(startX, endX) for startX, _, endX, _ in rectangles]
        ys = [(startY, endY) for _, startY, _, endY in rectangles]
        return max(self._countMerged(xs),
                self._countMerged(ys)) >= 3

    def _countMerged(self, intervals: list[tuple[int, int]]) -> int:
        count = 0
        prevEnd = 0
        for start, end in sorted(intervals):
            if start < prevEnd:
                prevEnd = max(prevEnd, end)
            else:
                prevEnd = end
                count += 1
        return count

    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xsl, xel, ysl, yel = [], [], [], []
        for xs, ys, xe, ye in rectangles: 
            xsl += [xs]
            xel += [xe]
            ysl += [ys]
            yel += [ye]

        xsl.sort()
        xel.sort()
        ysl.sort()
        yel.sort()

        def check_cut(sl, el):
            stack_len = 0
            cnt = -1
            pre_stack_len = -1
            while len(sl) > 0: 
                # print(sl, el)
                b = min(sl[0], el[0])
                while len(el) and el[0] == b: 
                    el.pop(0)
                    stack_len -= 1 

                if pre_stack_len != 0 and stack_len == 0: 
                    cnt += 1
                while len(sl) and sl[0] == b: 
                    sl.pop(0)
                    stack_len += 1 

                pre_stack_len = stack_len
            # print(cnt)
            if cnt >= 2: 
                return True 
            else: 
                return False

        a = check_cut(xsl, xel)
        b = check_cut(ysl, yel)
        # print(a, b)
        return a | b
    
if __name__ == "__main__": 
    n = 5
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    
    n = 4
    rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]

    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]

    # n = 6
    # rectangles = [[4,0,5,2],[0,5,4,6],[4,5,6,6]]

    test_case = (n, rectangles)
    ret = Solution().checkValidCuts(*test_case)
    print(ret)