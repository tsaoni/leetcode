from typing import List
from collections import defaultdict
import heapq
import math

class MaxHeap(): 
    def __init__(self, val) -> None:
        tmp = [-v for v in val]
        heapq.heapify(tmp) 
        self.val = [-t for t in tmp]
        self.table = defaultdict(list) 
        # self.N = len(val)
        for i, v in enumerate(val): 
            self.table[v] += [i]

    def push(self, val, idx): 
        tmp = [-v for v in self.val] 
        heapq.heappush(tmp, -val)
        self.val = [-t for t in tmp] 
        self.table[val] += [idx]
        # self.N += 1 
        # return self.val
    
    def pop(self): 
        """
        return the index in the original array
        """
        tmp = [-v for v in self.val] 
        val = heapq.heappop(tmp) 
        self.val = [-t for t in tmp]
        idx = self.table[-val].pop(0)
        # self.N -= 1
        return idx 

# li = [10, 20, 15, 30, 40]
# heap = MaxHeap(li)
# import pdb 
# pdb.set_trace()


class Solution:

    def maximumCandies2(self, candies: List[int], k: int) -> int:
        """
        binary search
        (can be rephrased as finding a higher common divisor between 1 and the sum of candies / k)
        """
        def good(pile): 
            n_child = 0
            for c in candies: 
                n_child += c // pile
            if n_child >= k: 
                return True 
            else:
                return False
        
        left, right = 0, sum(candies) // k
        while left < right: 
            # print("left", left)
            # print("right", right)
            mid = math.ceil((left + right) / 2)
            # print(mid)
            # if mid == left: 
            #     break
            if good(mid): 
                left = mid 
            else: 
                right = mid - 1
        
        return left
        

    def maximumCandies1(self, candies: List[int], k: int) -> int:
        """
        results in TLE
        """
        # store operations in a queue
        # queue = [] # (#pile, val, k)
        n_candies = len(candies)
        # for i, pile in enumerate(candies): 
        #     split = 1 
        #     subpile = pile // split
        #     while subpile >= 1: 
        #         queue += [(i, subpile, split)]
        #         split += 1 
        #         subpile = pile // split 
        
        # queue.sort(key=lambda x: -x[1])
        
        # acc_k = 0 
        vals = [0 for _ in candies]
        k_lst = [0 for _ in range(n_candies)]
        heap = MaxHeap([c for c in candies])
        acc_k = 0
        while True: 
            if acc_k >= k: 
                break 

            idx = 0
            tmp = -1
            for i, (c, kv) in enumerate(zip(candies, k_lst)): 
                if c // (kv + 1) > tmp: 
                    idx = i 
                    tmp = c // (kv + 1)
            
            idx = heap.pop()
            tmp = candies[idx] // (k_lst[idx] + 1)

            if tmp == 0: 
                return 0
            i, pile, split = idx, tmp, k_lst[idx] + 1
            vals[i] = pile 
            k_lst[i] = split 

            val = candies[idx] // (k_lst[idx] + 1)
            heap.push(val, idx)
            
            acc_k = sum(k_lst)
            # print("vals", vals)
            # print("klst", k_lst)
            # print("acc", acc_k)
            # print("k", k)

        # vals = [v for i, v in enumerate(vals) if v > 0 and k_lst[i] > 0]
        return min(list(filter(lambda x: x > 0, vals)))
    
    def maximumCandies(self, candies: List[int], k: int) -> int:
        """
        results in MLE
        """
        # store operations in a queue
        queue = [] # (#pile, val, k)
        n_candies = len(candies)
        for i, pile in enumerate(candies): 
            split = 1 
            subpile = pile // split
            while subpile >= 1: 
                queue += [(i, subpile, split)]
                split += 1 
                subpile = pile // split 
        
        queue.sort(key=lambda x: -x[1])
        
        acc_k = 0 
        vals = [0 for _ in range(n_candies)]
        k_lst = [0 for _ in range(n_candies)]
        while True: 
            if acc_k >= k: 
                break 
            elif len(queue) == 0: 
                return 0
            i, pile, split = queue.pop(0)
            vals[i] = pile 
            k_lst[i] = split 
            
            acc_k = sum(k_lst)
            # print("vals", vals)
            # print("klst", k_lst)

        return min(list(filter(lambda x: x > 0, vals)))

if __name__ == "__main__": 

    # candies = [5,8,6]
    # k = 5
    candies = [2,5]
    k = 11
    # candies = [1,2,3,4,10]
    # k = 5
    test_case = (candies, k)
    ret = Solution().maximumCandies2(*test_case)
    print(ret)