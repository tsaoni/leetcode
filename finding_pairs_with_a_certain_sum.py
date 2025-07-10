from typing import List

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        from collections import Counter
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt2 = Counter()
        for n in nums2: 
            self.cnt2[n] += 1 
        

    def add(self, index: int, val: int) -> None:
        tmp = self.nums2[index] + val
        self.cnt2[self.nums2[index]] -= 1
        self.cnt2[tmp] += 1 
        if self.cnt2[self.nums2[index]] == 0: 
            del self.cnt2[self.nums2[index]]
        self.nums2[index] = tmp 
        
        

    def count(self, tot: int) -> int:
        ret = 0
        for n1 in self.nums1: 
            n2 = tot - n1
            if n2 in self.cnt2:
                ret += self.cnt2[n2]
        return ret


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)