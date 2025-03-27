"""
the file is for some common data structures
"""

class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end): 
        if start == end: 
            self.tree[node] = arr[start]
        else: 
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])


    def set(self, index, value, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        if start == end: 
            self.tree[node] = value 
        else: 
            mid = (start + end) // 2 
            if index <= mid: 
                self.set(index, value, 2 * node + 1, start, mid)
            else: 
                self.set(index, value, 2 * node + 2, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def get_max(self, L, R, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        if R < start or L > end: 
            return float("-inf")
        if L <= start and R >= end: 
            return self.tree[node]
        mid = (start + end) // 2 
        val = max(self.get_max(L, R, 2 * node + 1, start, mid), 
                  self.get_max(L, R, 2 * node + 2, mid + 1, end))
        return val