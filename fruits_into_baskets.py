from typing import List

class Solution:
    def numOfUnplacedFruits2(self, fruits: List[int], baskets: List[int]) -> int:
        """
        a wrong approach
        """
        bidxs = [(baskets[i], i) for i in range(len(baskets))]
        bidxs.sort()
        taken = [False] * len(baskets)
        # fidxs = []
        ret = 0
        def search(f): 
            l, r = 0, len(baskets) - 1 
            while l < r: 
                mid = (l + r) // 2 
                if bidxs[mid][0] < f: 
                    l = mid + 1 
                else: 
                    r = mid
            return l if bidxs[l][0] >= f else -1 
        # import pdb 
        # pdb.set_trace()
        for f in fruits: 
            idx = search(f)
            if idx >= 0:
                while idx < len(baskets) and taken[bidxs[idx][1]]: 
                    idx += 1 
                if idx < len(baskets): 
                    taken[bidxs[idx][1]] = True  
                else: 
                    ret += 1 
            else: 
                ret += 1 
            print(taken)
        return ret
    
    def numOfUnplacedFruits2_1(self, fruits: List[int], baskets: List[int]) -> int:
        taken = [False] * len(baskets)
        ret = len(fruits)
        for f in fruits: 
            for i in range(len(baskets)): 
                if not taken[i] and baskets[i] >= f: 
                    taken[i] = True
                    ret -= 1 
                    break 
            
        return ret

    def numOfUnplacedFruits3(self, fruits: List[int], baskets: List[int]) -> int:
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


            def get_max(self, val, node=0, start=0, end=None): 
                if end is None: 
                    end = self.n - 1 
                if self.tree[node] >= val: 
                    if start == end: 
                        value = self.tree[node]
                        self.tree[node] = 0 
                        return value 
                    else: 
                        mid = (start + end) // 2 
                        if self.tree[2 * node + 1] >= val:
                            value = self.get_max(val, 2 * node + 1, start, mid)
                        else:
                            value = self.get_max(val, 2 * node + 2, mid + 1, end)
                        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
                        return value
                else: 
                    return -1
        
        st = SegmentTree(baskets)
        ret = 0
        for f in fruits: 
            tmp = st.get_max(f)
            if tmp < 0: 
                ret += 1 
            
        return ret

if __name__ == "__main__": 
    fruits = [4,2,5]
    baskets = [3,5,4]
    fruits = [3,6,1]
    baskets = [6,4,7]
    ret = Solution().numOfUnplacedFruits3(fruits, baskets)
    print(ret)