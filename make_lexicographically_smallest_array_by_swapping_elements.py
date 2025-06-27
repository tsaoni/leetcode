from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        sets = [] # (range, candidates, positions)
        def binary_search(num): 
            l, r = 0, len(sets)
            n_match = 0
            while l < r: 
                mid = (l + r) // 2 
                if num > sets[mid][0][1]: 
                    l = mid + 1
                else: 
                    r = mid
            if num >= sets[l][0][0] and num <= sets[l][0][1]: 
                if l < len(sets) - 1 and num >= sets[l + 1][0]: 
                    n_match = 2 
                else: 
                    n_match = 1
            return l, n_match

        def insert(num, lst): 
            l, r = 0, len(lst)
            while l < r: 
                mid = (l + r) // 2
                if num > lst[mid]: 
                    l = mid + 1 
                else: 
                    r = mid
            lst.insert(l, num)
        
        def merge(lst1, lst2): 
            lst = []
            while len(lst1) > 0 and len(lst2) > 0: 
                if lst1[0] < lst2[0]: 
                    lst.append(lst1.pop(0))
                else: 
                    lst.append(lst2.pop(0))
            return lst + lst1 + lst2

        for i, num in enumerate(nums): 
            idx, n_match = binary_search(num)
            if n_match == 0: 
                sets.insert(idx, [[num - limit, num + limit], [num], [i]])
            elif n_match == 1: 
                insert(num, sets[idx][1])
                sets[idx][2].append(i)
                if num - limit < sets[idx][0][0]: 
                    sets[idx][0][0] = num - limit
                if num + limit > sets[idx][0][1]:
                    sets[idx][0][1] = num + limit 
            elif n_match == 2: 
                sets[idx][0][1] = sets[idx + 1][0][1]
                sets[idx][1] += [num] + sets[idx + 1][1]
                sets[idx][2] = merge(sets[idx][2], sets[idx + 1][2])
                sets.pop(idx + 1)

        for ele in sets: 
            for num, pos in zip(ele[1], ele[2]): 
                nums[pos] = num
        return nums
    
if __name__ == "__main__": 
    nums = [1,5,3,9,8]
    limit = 2
    ret = Solution().lexicographicallySmallestArray(nums, limit)
    print(ret)