from typing import List
import heapq
from collections import defaultdict

class Solution:

    def repairCars1(self, ranks: List[int], cars: int) -> int:
        
        rank_cnt = defaultdict(int)
        for r in ranks: 
            rank_cnt[r] += 1
        
        cnt = 0
        acc_time = 0
        n_cars = {r: 1 for r in ranks} #[1] * len(ranks)
        
        heap = [x * (c ** 2) for x, c in n_cars.items()]
        idx_dict = {}
        for r, c in n_cars.items():
            val = r * (c ** 2)
            if val in idx_dict:
                idx_dict[val] += [r]
            else:
                idx_dict[val] = [r]
        
        heapq.heapify(heap)
        while True: 
            t = heapq.heappop(heap)
            idx = idx_dict[t].pop(0) # idx: rank
            n_cars[idx] += 1
            new_val = idx * (n_cars[idx] ** 2)
            heapq.heappush(heap, new_val)
            if new_val in idx_dict: 
                idx_dict[new_val] += [idx]
            else: 
                idx_dict[new_val] = [idx]
            acc_time = max(t, acc_time)
            # if acc_time > val: 
            #     break
            cnt += rank_cnt[idx] 
            if cnt >= cars: 
                break
            # print(t, acc_time, cnt)
        # print(n_cars)
        # print(cnt)
        # import pdb 
        # pdb.set_trace()
        # return cnt >= cars
        


        return acc_time
    
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def good(val): 
            cnt = 0
            acc_time = 0
            n_cars = [1] * len(ranks)
            
            heap = [x * (c ** 2) for x, c in zip(ranks, n_cars)]
            idx_dict = {}
            for i, x in enumerate(heap):
                if x in idx_dict:
                    idx_dict[x] += [i] 
                else: 
                    idx_dict[x] = [i]
            heapq.heapify(heap)
            while True: 
                t = heapq.heappop(heap)
                idx = idx_dict[t].pop(0)
                n_cars[idx] += 1
                new_val = ranks[idx] * (n_cars[idx] ** 2)
                heapq.heappush(heap, new_val)
                if new_val in idx_dict: 
                    idx_dict[new_val] += [idx]
                else: 
                    idx_dict[new_val] = [idx]
                acc_time = max(t, acc_time)
                if acc_time > val: 
                    break
                cnt += 1 
                # print(t, acc_time, cnt)
            # print(n_cars)
            # print(cnt)
            # import pdb 
            # pdb.set_trace()
            return cnt >= cars
        
        left, right = 0, max(ranks) * (cars ** 2) 
        for i in range(100): 
            mid = (left + right) / 2 
            # print(left, mid, right)
            if good(mid): 
                right = mid 
            else: 
                left = mid

        return round(left)
    
if __name__ == "__main__": 
    ranks = [4,2,3,1]
    cars = 10
    # ranks = [5,1,8]
    # cars = 6
    test_case = (ranks, cars)
    ret = Solution().repairCars1(*test_case)
    print(ret)