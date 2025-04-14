from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ret = 0
        for i in range(len(arr)): 
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a: 
                    for k in range(j + 1, len(arr)): 
                        ret += abs(arr[j] - arr[k]) <= b and abs(arr[k] - arr[i]) <= c
        return ret

if __name__ == "__main__": 
    ret = Solution().countGoodTriplets()
    print(ret)