
from typing import List

class SegmentTree(): 
    def __init__(self, xl): 
        self.xl = xl 
        self.N = len(xl)
        self.xr = dict()
        for i in range(len(xl)):
            x = xl[i]
            self.xr[x] = i
        self.count = [0] * (4 * self.N + 1)
        self.total = [0] * (4 * self.N + 1)

    def query(self, ): 
        return self.total[1]

    def update_range(self, ql, qr, val): 
        self._update_range(1, 0, self.N - 1, ql, qr, val)

    def _update_range(self, node, l, r, ql, qr, val): 
        if ql == self.xl[l] and qr == self.xl[r]: 
            self.count[node] += val
        else: 
            mid = (l + r) // 2
            left, right = node * 2, node * 2 + 1
            if ql < self.xl[mid]:
                qr2 = min(qr, self.xl[mid])
                self._update_range(left, l, mid, ql, qr2, val)
            if qr > self.xl[mid]:
                ql2 = max(ql, self.xl[mid])
                self._update_range(right, mid, r, ql2, qr, val)
        
        if self.count[node] > 0:
            self.total[node] = self.xl[r] - self.xl[l]
        else: 
            self.total[node] = self.total[node * 2] + self.total[node * 2 + 1] if node * 2 + 1 < len(self.total) else 0

class Solution:

    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        l = len(nums)
        ret = 0
        for i in range(l): 
            is_good = True
            if i - k >= 0: 
                tmp = True if nums[i - k] < nums[i] else False
                is_good &= tmp
            if i + k < l: 
                tmp = True if nums[i + k] < nums[i] else False
                is_good &= tmp
            if is_good: 
                ret += nums[i]
        return ret

    def separateSquares_2_1(self, squares: List[List[int]]) -> float:
        """
        the second problem in the contest
        use segment tree
        """
        from itertools import chain
        xl = list(chain(*[[x, x + l] for x, _, l in squares]))
        xl = sorted(list(set(xl)))
        st = SegmentTree(xl)
        
        events = []
        for x, y, l in squares: 
            events += [(y, 1, x, x + l), (y + l, -1, x, x + l)]
        events.sort()
        
        def calc(): 
            yd = -1e9
            current_sum = 0
            for y, delta, ql, qr in events:
                current_len = st.query()
                current_sum += current_len * (y - yd)
                st.update_range(ql, qr, delta)
                yd = y 
            return current_sum
        
        total_sum = calc()

        current_sum = 0
        def calc2(): 
            yd = -1e9
            current_sum = 0
            # print(events)
            for y, delta, ql, qr in events:
                current_len = st.query()
                tmp = current_len * (y - yd)
                st.update_range(ql, qr, delta)
                if (current_sum + tmp) * 2 >= total_sum: 
                    return yd + (total_sum / 2 - current_sum) / current_len
                current_sum += tmp
                yd = y 
                # print(current_sum)
        

        return calc2()

    def separateSquares_2(self, squares: List[List[int]]) -> float:
        """
        the second problem in the contest
        may encounter TLE
        """
        pnts = []

        for x in squares: 
            pnts += [x[0], x[0] + x[2]]
        pnts = list(set(pnts))
        pnts.sort()
        l_lst = [[] for _ in range(len(pnts) - 1)]
        
        # update l_lst
        def search(val, start, end, lst): 
            if start == end - 1: 
                if val < lst[start]: 
                    return (-1, 0)
                elif val > lst[end]: 
                    return (len(lst) - 1, -1)
                else: 
                    return (start, end)
            mid = int((start + end) / 2)
            if val == lst[mid]: 
                return (mid, mid)
            elif val < lst[mid]: 
                return search(val, start, mid, lst) 
            elif val > lst[mid]: 
                return search(val, mid, end, lst)
            
        def update_y_range(ins, old_lst): 
            if len(old_lst) == 0: 
                return ins
            else: 
                start, end = ins
                r_start = search(start, 0, len(old_lst) - 1, old_lst)
                r_end = search(end, 0, len(old_lst) - 1, old_lst)
                if r_start[0] == -1: 
                    new_start = start
                elif r_start[0] % 2 == 0: 
                    new_start = old_lst[r_start[0]]
                elif r_start[0] % 2 == 1: 
                    new_start = start
                
                if r_end[0] == -1: 
                    new_end = end
                elif r_end[0] % 2 == 0: 
                    new_end = old_lst[r_end[1]]
                elif r_end[0] % 2 == 1: 
                    new_end = end

            left, right = [], []
            add_left, add_right = True, True
            for i, x in enumerate(old_lst): 
                if x < new_start: 
                    left += [x]
                elif x > new_end: 
                    right += [x]
                if i % 2 == 1 and x == new_start: 
                    add_left = False 
                if i % 2 == 0 and x == new_end: 
                    add_right = False
            new_range = []
            if add_left:
                new_range += [new_start]
            if add_right: 
                new_range += [new_end]
            # print("old")
            # print(old_lst)
            # print("new")
            # print(left + [new_start, new_end] + right)
            # print("range")
            # print(ins)
            # print([new_start, new_end])
            
            return left + new_range + right
        
        for x in squares: 
            start, end = x[0], x[0] + x[2]
            start_idx, end_idx = pnts.index(start), pnts.index(end)
            for idx in range(start_idx, end_idx):
                y_range = [x[1], x[1] + x[2]]
                old_lst = l_lst[idx]
                l_lst[idx] = update_y_range(y_range, old_lst)
        
        # print(pnts)
        # print(l_lst)
        # return
        # compute total area 
        total_area = 0
        for i in range(len(l_lst)): 
            x_d = pnts[i + 1] - pnts[i]
            y_d = 0 
            for j in range(0, len(l_lst[i]), 2): 
                y_d += l_lst[i][j + 1] - l_lst[i][j]
            total_area += x_d * y_d

        # find y values 
        def good(y, pnts, l_lst): 
            below_area = 0 
            for i in range(len(l_lst)): 
                x_d = pnts[i + 1] - pnts[i]
                y_d = 0 
                for j in range(0, len(l_lst[i]), 2): 
                    v = min(l_lst[i][j + 1], y)
                    y_d += max(v - l_lst[i][j], 0)
                below_area += x_d * y_d

            if below_area < 1 / 2 * total_area: 
                return True 
            else: 
                return False
        
        # print(pnts) 
        # print(l_lst)
        y_min, y_max = min([x[1] for x in squares]), max(x[1] + x[2] for x in squares) 
        left, right = y_min, y_max
        for _ in range(100): 
            mid = (left + right) / 2 
            if good(mid, pnts, l_lst): 
                left = mid 
            else: 
                right = mid
        return left

    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        inspired from: 
        https://www.youtube.com/watch?v=TemUbBcvRLY&ab_channel=ProgrammingLivewithLarry
        """
        total_area = sum([x[2] ** 2 for x in squares])
        avg_area = 1 / 2 * total_area
        def good(target): 
            acc_area = 0
            for s in squares: 
                if target <= s[1]: 
                    h = 0 
                elif target >= s[1] + s[2]: 
                    h = s[2]
                elif target > s[1] and target < s[1] + s[2]: 
                    h = target - s[1]
                acc_area += h * s[2]
            if acc_area < avg_area:
                return True 
            else: 
                return False
        
        left, right = 0, 1e10
        for _ in range(100): 
            mid = (left + right) / 2 
            if good(mid): 
                left = mid 
            else: 
                right = mid
        return left

    def separateSquares3(self, squares: List[List[int]]) -> float:
        """
        hint: binary search + insert
        """
        def search(lst, start, end, pnt): 
            if start == -1: 
                return (-1, -1)
            if start == end: 
                if lst[start] > pnt: 
                    return (-1, 0)
                if lst[start] < pnt: 
                    return (0, -1)
                else:
                    return (0, 0)
            elif start == end - 1: 
                if lst[start] == pnt: 
                    return (start, start)
                elif lst[end] == pnt: 
                    return (end, end)
                elif lst[start] > pnt: 
                    return (-1, 0)
                elif lst[end] < pnt: 
                    return (1, -1)
                else:
                    return (start, end)
            
            mid = int((start + end) / 2)
            if lst[mid] == pnt: 
                return (mid, mid)
            elif lst[mid] < pnt:
                return search(lst, mid, end, pnt)
            elif lst[mid] > pnt: 
                return search(lst, start, mid, pnt)
            # return 
        
        def insert(pnts, pnt, l_lst): 
            if len(pnts) == 0: 
                start = end = -1 
            else: 
                start, end = 0, len(pnts) - 1
            start, end = search(pnts, start, end, pnt)
            if start == -1 and end == -1: 
                pnts += [pnt]
                return 0, pnts, l_lst
            elif start == -1: 
                pnts = [pnt] + pnts
                l_lst = [0] + l_lst
                return 0, pnts, l_lst
            elif end == -1: 
                pnts += [pnt]
                l_lst += [0]
                return len(pnts) - 1, pnts, l_lst
            elif start == end: 
                return start, pnts, l_lst
            else: 
                pnts = pnts[: end] + [pnt] + pnts[end: ]
                l_lst = l_lst[: end] + [l_lst[start]] + l_lst[end: ]
                return end, pnts, l_lst

        pnts = []
        l_lst = []
        for s in squares: 
            pnt = s[1]
            
            start, pnts, l_lst = insert(pnts, pnt, l_lst)
            pnt = s[1] + s[2]
            end, pnts, l_lst = insert(pnts, pnt, l_lst)
            l = s[2]
            for i in range(start, end): 
                l_lst[i] += l
            # print(start)
            # print(end)
            # print(pnts)
            # print(l_lst)
            # import pdb 
            # pdb.set_trace()

        total_area = sum([x[2] ** 2 for x in squares])
        avg_area = 1 / 2 * total_area
        acc_area = 0
        for i in range(len(l_lst)): 
            start, end = pnts[i], pnts[i + 1]
            l = l_lst[i]
            inc = (end - start) * l
            tmp = acc_area + inc 
            if tmp >= avg_area: 
                offset = (avg_area - acc_area) / l 
                return start + offset
            else: 
                acc_area = tmp

    def separateSquares2(self, squares: List[List[int]]) -> float:
        pnts = [x[1] for x in squares] + [x[1] + x[2] for x in squares]
        pnts.sort()
        total_area = sum([x[2] ** 2 for x in squares])
        avg_area = 1 / 2 * total_area
        acc_area = 0

        for i in range(len(pnts) - 1): 
            y, y1 = pnts[i], pnts[i + 1]
            acc_l = 0
            for square in squares: 
                if square[1] == y or square[1] + square[2] == y1 or square[1] < y and square[1] + square[2] > y1: 
                    acc_l += square[2]
            tmp = (y1 - y) * acc_l + acc_area
            if tmp == avg_area: 
                return float(y1) 
            elif tmp < avg_area: 
                acc_area = tmp 
            else: 
                offset = (avg_area - acc_area) / acc_l
                return y + offset
        # return 
    
    def separateSquares1(self, squares: List[List[int]]) -> float:
        s_squares = sorted(squares, key=lambda x: x[1] + x[2])
        l = len(s_squares)
        total_area = sum([x[2] ** 2 for x in squares])
        avg_area = 1 / 2 * total_area
        py = min([x[1] for x in s_squares])
        
        for i in range(l): 
            y = squares[i][1] + squares[i][2]
            def compute_area(square, y): 
                # (y, y + l)
                if y < square[1]: 
                    ret = 0
                elif y > square[1] + square[2]: 
                    ret = square[2] ** 2
                else: 
                    h = y - square[1]
                    ret = square[2] * h
                return ret
            acc_area = 0
            for j in range(l):
                area = compute_area(s_squares[j], y)
                acc_area += area
                if acc_area >= avg_area: 
                    break 
            if acc_area == avg_area: 
                return y 
            elif acc_area > avg_area: 
                
                return 
            py = y
        # return 

    def shortestMatchingSubstring2(self, s: str, p: str) -> int:
        """
        Solution after I aware of `exactly two *`
        """
        left, mid, right = p.split("*")
        # print(left, mid, right)
        l_pos, m_pos, r_pos = [-1] * len(s), [-1] * len(s), [-1] * len(s)
        cnt = -1
        # if len(left):
        l_pos = [-1] * len(s)
        for i in range(len(s)): 
            start, end = max(0, i + 1 - len(left)), i + 1
            if s[start: end] == left: 
                # l_pos[i] = 0
                cnt = 0
            if cnt >= 0 and i + 1 < len(s): 
                l_pos[i + 1] = cnt
                cnt += 1
        # else: 
        #     l_pos = [0] * len(s)
        print(l_pos)

        # if len(right):
        #     r_pos = [-1] * len(s)
        cnt = -1
        for i in range(len(s) - 1, -1, -1): 
            start, end = i, min(len(s), i + len(right))
            if s[start: end] == right: 
                # r_pos[i] = 0
                cnt = 0
            if cnt >= 0 and i - 1 >= 0: 
                r_pos[i - 1] = cnt
                cnt += 1
        # else: 
        #     r_pos = [0] * len(s)
        print(r_pos)

        d = -1
        l_d, r_d = 0, 0
        n_trial = len(s) - len(mid) + 1 if len(mid) else len(s)
        for i in range(n_trial): 
            # mid range: [i, i + len(mid) - 1]
            if s[i: i + len(mid)] == mid:
                if len(left) == 0: 
                    l_d = 0 
                else: 
                    if True: #i > 0: 
                        if l_pos[i] >= 0: 
                            l_d = l_pos[i]
                        else: 
                            l_d = -1
                    else: 
                        l_d = -1
                
                if len(right) == 0: 
                    r_d = 0 
                else: 
                    if i > 0: #i + len(mid) - 1 < len(s) - 1: 
                        if r_pos[i + len(mid) - 1] >= 0: 
                            r_d = r_pos[i + len(mid) - 1]
                        else: 
                            r_d = -1
                    else: 
                        r_d = -1

                if l_d >= 0 and r_d >= 0: 
                    tmp = len(left) + l_d + len(mid) + r_d + len(right)
                    if d == -1:
                        d = tmp
                    else: 
                        d = min(tmp, d)

                # if l_pos[i] > 0:
                #     l_d = l_pos[i - 1]
                # if r_pos[i + len(mid)] > 0:
                #     r_d = r_pos[i + len(mid)]
        
        check_left = len(mid + right) == 0
        check_right = len(left + mid) == 0 
        if check_left: 
            if s[-len(left):] == left: 
                return len(left)
            
        if check_right: 
            if s[:len(right)] == right: 
                return len(right)
        return d

    def shortestMatchingSubstring1(self, s: str, p: str) -> int:
        """
        Result in TLE
        """
        if len(p.strip("*")) == 0: 
            return 0
        toks = [x for x in p.strip("*").split("*") if len(x)]
        # tries = {}
        # for tok in toks: 
        #     d = tries
        #     for t in tok: 
        #         if t not in d: 
        #             d[t] = {}
        #         d = d[t]
        #     d[''] = tok # set end conditions
        
        def _detect_pattern(s, start_idx, toks, t_idx): 
            if t_idx == len(toks): 
                # print([-1, start_idx])
                return [-1, start_idx]
            elif start_idx >= len(s):
                # print([-1, start_idx])
                return [-1, -1]
            
            tok = toks[t_idx]
            dist = len(tok)
            start_idx += dist - 1
            ret_s, ret = -1, -1
            # print(tok)
            # print(start_idx, len(s))
            for i in range(start_idx, len(s)): 
                start, end = max(0, i - dist + 1), i + 1
                # print(start, end)
                if s[start: end] == tok: 
                    # print(tok)
                    _, tmp_e = _detect_pattern(s, i + 1, toks, t_idx + 1)
                    if ret < 0: 
                        ret_s = start
                        ret = tmp_e 
                    elif tmp_e > 0: 
                        # ret_s = start
                        if tmp_e - start < ret - ret_s: 
                            ret_s = start
                            ret = tmp_e
                        # ret = min(tmp_e, ret)
            # print([ret_s, ret])
            return [ret_s, ret]

        start, end = _detect_pattern(s, 0, toks, 0)
        # print(s)
        # print(p)
        # print(start, end)
        if end < 0: 
            return -1
        return end - start
        
        # prev_s = []
        # cur_s = []
        # for tok in toks:
        #     dist = len(tok)
        #     for i in range(1, len(s) + 1): 
        #         start, end = max(0, i - dist), i
        #         if s[start: end] == tok: 


    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        """
        WA: conflicts between two adjacent substrings
        """
        if len(p.strip("*")) == 0: 
            return 0
        toks = [x for x in p.strip("*").split("*") if len(x)]
        tries = {}
        for tok in toks: 
            d = tries
            for t in tok: 
                if t not in d: 
                    d[t] = {}
                d = d[t]
            d[''] = tok # set end conditions
        # print(tries)
        # return 
        states = [[-1, -1] for t in toks] # store [pos, dist]
        # tok_idx_dict = {t: i for i, t in enumerate(toks)}
        ptrs = [tries]
        for s_i, c in enumerate(s): 
            # update ptrs and detect match
            next_ptrs = []
            match_strs = []
            for p in ptrs: 
                if c in p: 
                    tmp = p[c]
                    if '' in tmp: 
                        tok = tmp['']
                        match_strs += [tok]
                    next_ptrs += [tmp]
            
            # update associated states
            for t_i, tok in enumerate(toks): 
                if tok in match_strs: 
                    update = True
                    pos = s_i - len(tok) + 1
                    if t_i == 0: 
                        dist = len(tok)
                    elif states[t_i - 1][1] > -1: 
                        dist = s_i - states[t_i - 1][0] - len(toks[t_i - 1]) + 1 + states[t_i - 1][1]
                        update = states[t_i - 1][0] + len(toks[t_i - 1]) - 1 < pos
                    else: 
                        update = False
    
                    if states[t_i][1] == -1 or states[t_i][1] > -1 and states[t_i][1] >= dist: 
                        if update:
                            states[t_i] = [pos, dist]

            # for ms in match_strs: 
            #     idx = toks.index(ms)
            #     pos = s_i - len(ms) + 1
            #     if idx == 0: 
            #         dist = len(ms)
            #     elif states[idx - 1][1] > -1: 
            #         dist = states[idx - 1][1] - len(toks[idx]) + (pos - states[idx - 1][0])
                
            #     states[idx]
            
            ptrs = [tries] + next_ptrs
        
        pos = states[-1][0] + len(toks[-1]) 
        tmp = s[pos - states[-1][1]: pos]
        # print(tmp)
        print(states)
        return states[-1][1]

if __name__ == "__main__": 
    # nums = [2, 1]
    # k = 1
    # test_case = (nums, k)
    # ret = Solution().sumOfGoodNumbers(*test_case)
    
    # squares = [[0,0,1],[2,2,1]]
    # [[16,27,3],[18,24,5]]
    # [[0,0,2],[1,1,1]]
    # [[15,30,4],[25,29,10]]
    # [[0,0,1],[2,2,1]]
    # [[15,30,4],[25,29,10]]
    # test_case = (squares, )
    # ret = Solution().separateSquares_2_1(*test_case)

    # s = "abaacbaecebce"
    # p = "ba*c*ce"
    # s = "baccbaadbc"
    # p = "cc*baa*adb"
    # s = "a"
    # p = "**"
    s = "uwkpnqhynsedqqgdw"
    p = "k**edq"
    # s = "srs"
    # p = "r**s"
    # s = "ccbfxp"
    # p = "c*cbf*"
    # s = "cvtrmfmvuhzncqffl"
    # p = "fl**"
    # s = "rpf"
    # p = "r*pf*"
    test_case = (s, p)
    ret = Solution().shortestMatchingSubstring2(*test_case)
    print(ret)