from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        """TLE"""
        N = len(nums1)
        seen = [-1 for _ in range(N)]
        n2_idx = [-1 for _ in range(N)]
        for i in range(N): 
            if nums1[i] == nums2[i]: 
                n2_idx[i] = i
            else: 
                if seen[nums1[i]] == -1: 
                    seen[nums1[i]] = i
                else: 
                    n2_idx[i] = seen[nums1[i]]
                
                if seen[nums2[i]] == -1: 
                    seen[nums2[i]] = i
                else: 
                    n2_idx[seen[nums2[i]]] = i
        
        # print(n2_idx)
        
        """increasing in n2_idx"""
        # v1
        # order_lst = [(i, n2_idx[i]) for i in range(N)]
        # order_lst.sort(key=lambda x: x[1])
        # idx_right_larger = [[] for _ in range(N)]
        # for i, (oidx, _) in enumerate(order_lst): 
        #     for j in range(i + 1, N): 
        #         if order_lst[j][0] > oidx:
        #             idx_right_larger[oidx].append(order_lst[j][0])
        # # print(idx_right_larger)
        
        # ret = 0
        # for px in range(N): 
        #     ret += sum([len(idx_right_larger[py]) for py in idx_right_larger[px]])
        
        # v2 
        seen = [0] * N
        xcnt, ycnt = [0] * N, [0] * N
        for i in range(N): 
            idx = n2_idx[i]
            seen[idx] = 1 
            xcnt[i] = sum(seen[: idx])
        
        seen = [0] * N
        for i in range(N - 1, -1, -1):
            idx = n2_idx[i]
            seen[idx] = 1 
            ycnt[i] = sum(seen[idx + 1:])

        # print(xcnt, ycnt)
        ret = 0
        for i in range(1, N - 1): 
            ret += xcnt[i] * ycnt[i]
        return ret
    
    def goodTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        """with fenwick tree"""
        N = len(nums1)
        seen = [-1 for _ in range(N)]
        n2_idx = [-1 for _ in range(N)]
        for i in range(N): 
            if nums1[i] == nums2[i]: 
                n2_idx[i] = i
            else: 
                if seen[nums1[i]] == -1: 
                    seen[nums1[i]] = i
                else: 
                    n2_idx[i] = seen[nums1[i]]
                
                if seen[nums2[i]] == -1: 
                    seen[nums2[i]] = i
                else: 
                    n2_idx[seen[nums2[i]]] = i
        
        # print(n2_idx)
        
        """increasing in n2_idx"""
        def lowbit(x): 
            return x & -x
        
        def update(pos): 
            pos += 1
            while pos < N + 1: 
                BIT[pos] += 1
                pos += lowbit(pos)
            return 
        
        def query(pos): 
            pos += 1
            cnt = 0
            while pos > 0: 
                cnt += BIT[pos]
                pos -= lowbit(pos)
            return cnt
        
        BIT = [0] * (N + 1) 
        ret = 0
        for i in range(N): 
            idx = n2_idx[i]
            lc = query(idx)
            rc = (N - idx - 1) - (i - lc)
            ret += lc * rc
            update(idx)
        return ret

if __name__ == "__main__": 
    nums1 = [2,0,1,3]
    nums2 = [0,1,2,3]
    # nums1 = [4,0,1,3,2]
    # nums2 = [4,1,0,2,3]
    nums1 = [7,8,1,0,4,2,5,6,3,9,11,10] 
    nums2 = [7,9,10,6,0,8,1,2,3,11,4,5]
    test_case = (nums1, nums2)
    ret = Solution().goodTriplets1(*test_case)
    print(ret)