from typing import List 

class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.st = [0] * (4 * self.n)
        self.tree = [0] * (4 * self.n)
        self.itvls = [0] * (4 * self.n)
        self.arr = arr
        self.build()

    def build(self, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        if start == end: 
            self.itvls[node] = self.arr[start]
        else:
            mid = (start + end) // 2 
            ll = self.build(2 * node + 1, start, mid)
            rl = self.build(2 * node + 2, mid + 1, end)
            self.itvls[node] = ll + rl
        return self.itvls[node]

    def set(self, val, L, R, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        
        if start == L and end == R: 
            # if (self.st[node] == 0 and val == 1) or (self.st[node] == 1 and val == -1): 
            #     inc = self.itvls[node] * val
            # else: 
            #     inc = 0
            self.st[node] += val 
            if self.st[node] > 0:
                newv = self.itvls[node]
            else: 
                get_child_val_fn = lambda idx: self.tree[idx] if idx < len(self.tree) else 0
                newv = get_child_val_fn(2 * node + 1) + get_child_val_fn(2 * node + 2)
            inc = newv - self.tree[node]
            self.tree[node] = newv
            # import pdb 
            # pdb.set_trace()
            return inc

        mid = (start + end) // 2 
        linc, rinc = 0, 0
        if L <= mid: 
            _R = min(R, mid)
            linc = self.set(val, L, _R, 2 * node + 1, start, mid)
            if self.st[node] > 0: 
                linc = 0
        if R > mid: 
            _L = max(L, mid + 1)
            rinc = self.set(val, _L, R, 2 * node + 2, mid + 1, end)
            if self.st[node] > 0: 
                rinc = 0

        # import pdb 
        # pdb.set_trace()
        # if node == 1: 
        #     import pdb 
        #     pdb.set_trace()
        self.tree[node] += (linc + rinc)

        return linc + rinc

    
    def get_itvl(self, ): 
        return self.tree[0]

class Solution:
    def separateSquares_2(self, squares: List[List[int]]) -> float:
        from collections import defaultdict
        xs = sorted(set([x for x, _, _ in squares] + [x + l for x, _, l in squares]))
        xd = [xs[i] - xs[i - 1] for i in range(1, len(xs))]
        xs_rev = {x: i for i, x in enumerate(xs)}
        yd = defaultdict(list)
        st = SegmentTree(xd)
        total = 0.
        for x, y, l in squares: 
            yd[y].append((x, x + l, 1))
            yd[y + l].append((x, x + l, -1))

        prev = -1
        A = []
        ll = 0
        for k in sorted(yd): 
            if prev >= 0:
                total += ll * (k - prev)
                A.append((prev, total, ll))
            for L, R, val in yd[k]:
                l, r = xs_rev[L], xs_rev[R] - 1
                st.set(val, l, r, node=0, start=0, end=None)
            ll = st.get_itvl()
            # import pdb 
            # pdb.set_trace()
            prev = k
        
        hf = total / 2 
        l, r = 0, len(A) - 1 
        while l < r: 
            mid = (l + r + 1) // 2 
            if A[mid][1] <= hf: 
                l = mid 
            else: 
                r = mid - 1
        
        if A[l][1] > hf: 
            l = -1

        # import pdb 
        # pdb.set_trace()
        if l >= 0 and A[l][1] == hf: 
            return A[l + 1][0] + 0. if A[l][2] > 0 else A[l][0] + 0.
        else:
            acc = A[l][1] if l >= 0 else 0.
            return A[l + 1][0] + (hf - acc) / A[l + 1][2]


    def separateSquares(self, squares: List[List[int]]) -> float:
        import heapq 
        ys = []
        tot = 0
        for x, y, l in squares: 
            ys += [(y, l), (y + l, -l)]
            tot += l ** 2 
        ys.sort()
        tot /= 2 
        w = 0 
        i = 0 
        acc = 0 
        # print(ys, tot)
        while i < len(ys): 
            cur = ys[i][0]
            while cur == ys[i][0]: 
                w += ys[i][1]
                i += 1 
            # print(i, acc)
            # import pdb 
            # pdb.set_trace()
            h = ys[i][0] - ys[i - 1][0]
            inc = w * h 
            if acc + inc >= tot: 
                return ys[i - 1][0] + (tot - acc) / w 
            acc += inc
        return -1 
    

if __name__ == "__main__": 
    squares = [[0,0,1],[2,2,1]]
    squares = [[0,0,2],[1,1,1]]
    squares = [[15,21,2],[19,21,3]]
    squares = [[16,27,3],[18,24,5]]
    squares = [[12,14,7],[8,12,6]]
    # squares = [[0,0,2],[1,1,1]]
    squares = [[17,27,7],[15,23,5],[13,21,7]]
    squares = [[9,14,1],[16,30,1],[26,27,3],[17,24,5]]
    ret = Solution().separateSquares_2(squares)
    print(ret)