from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        liters = 0
        l_max_lst, r_max_lst = [0], [0]
        l_max, r_max = 0, 0
        for i in range(1, len(height)): 
            l_max = max(height[i - 1], l_max)
            l_max_lst += [l_max]
            r_max = max(height[len(height) - i], r_max)
            r_max_lst = [r_max] + r_max_lst
        # print(l_max_lst)
        # print(r_max_lst)
        for i in range(1, len(height) - 1): 
            l = l_max_lst[i] #max(height[: i])
            r = r_max_lst[i] #max(height[i + 1:])
            h = min(l, r)
            if h > height[i]: 
                liters += (h - height[i])
        return liters
    
if __name__ == "__main__": 
    test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
    ret = Solution().trap(test_case)
    print(ret)