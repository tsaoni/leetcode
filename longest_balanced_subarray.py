from typing import List

class SegmentTree: 
    def __init__(self, arr): 
        self.n = len(arr)
        self.tree = [[0, 0, 0] for _ in range(4 * self.n)] 
        self.arr = arr

    def update(self, val, pos, R, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        
        # print(start, end)
        if start == end: 
            if start == pos:
                self.tree[node] = [val, val, val] 
        else: 
            # if node == 1: 
            #     import pdb 
            #     pdb.set_trace()
            mid = (start + end) // 2 
            if pos <= mid: 
                lmin, lmax, vsum = self.update(val, pos, R, 2 * node + 1, start, mid)
                lmin += self.tree[2 * node + 2][2]
                lmax += self.tree[2 * node + 2][2]
                vsum += self.tree[2 * node + 2][2]
                if mid + 1 <= R:
                    rmin, rmax = self.tree[2 * node + 2][: 2]
                else: 
                    rmin, rmax = float("inf"), -float("inf")
            else: 
                # lsum = self.query(start, mid, 2 * node + 1)
                rmin, rmax, rsum = self.update(val, pos, R, 2 * node + 2, mid + 1, end)
                vsum = rsum + self.tree[2 * node + 1][2]
                lmin, lmax = self.tree[2 * node + 1][0] + rsum, self.tree[2 * node + 1][1] + rsum
                # vsum = rsum + self.tree[2 * node + 1][2]
                # vsum = lsum + rsum
            # vsum = self.tree[node][2] + val
            
            self.tree[node] = [min(lmin, rmin), max(lmax, rmax), vsum]
            # if node == 1: 
            #     print(pos, val, R, self.tree[node])
            #     import pdb 
            #     pdb.set_trace()
        return self.tree[node]


    def get_left(self, val, node=0, start=0, end=None): 
        if end is None: 
            end = self.n - 1 
        
        # print(node)
        if start == end: 
            if self.tree[node][0] <= val and self.tree[node][1] >= val: 
                return start
            else: 
                return -1

        
        mid = (start + end) // 2
        lsum, rsum = self.tree[2 * node + 1][2], self.tree[2 * node + 2][2]
        # print(node, val, lsum, rsum)
        if self.tree[2 * node + 1][0] <= (val - rsum) and self.tree[2 * node + 1][1] >= (val - rsum): 
            return self.get_left(val - rsum, 2 * node + 1, start, mid)
        else: #self.tree[2 * node + 2][0] <= (val - lsum) and self.tree[2 * node + 2][1] >= (val - lsum):
            return self.get_left(val, 2 * node + 2, mid + 1, end)
        # else: 
        #     return -1
     
    

class Solution:

    def longestBalanced_1(self, nums: List[int]) -> int:
        ret = 0
        occur = {}
        N = len(nums)
        A = [0] * N
        st = SegmentTree(A)
        for i in range(N): 
            n = nums[i]
            val = 1 if n & 1 == 0 else -1
            # print('a', i)
            st.update(val, i, i)#N - 1)
            st.arr[i] = val
            if n in occur: 
                prev = occur[n]
                # print('b')
                st.update(0, prev, i) #N - 1)
                st.arr[prev] = 0
            # print(st.tree)
            # if i == 4: 
            #     import pdb 
            #     pdb.set_trace()
            l = st.get_left(0)
            if l >= 0: 
                # print(i, l)
                ret = max(ret, i - l + 1)
            occur[n] = i 

        return ret 
    
    def longestBalanced(self, nums: List[int]) -> int:
        # psum = []
        # n_e, n_o = 0, 0
        
        ret = 0
        for i in range(len(nums)):
            epre, opre = set(), set()
            for j in range(i, -1, -1): 
                n = nums[j]
                if n & 1 == 0: 
                    epre.add(n)
                else: 
                    opre.add(n)
                if len(epre) == len(opre):
                    ret = max(ret, i - j + 1)
        return ret 
    
if __name__ == "__main__": 
    nums = [2,5,4,3]
    nums = [3,2,2,5,4]
    # nums = [1,2,3,2]
    # nums = [3,2,2,5,4]
    # nums = [1,2,3,2]
    # nums = [6,6]
    # nums = [47,12,54,54]
    # nums = [16,25,36,38,23]
    ret = Solution().longestBalanced_1(nums)
    print(ret)