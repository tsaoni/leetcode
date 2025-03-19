from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        num_lst = []
        for i  in range(len(nums)): 
            end_idx = max(0, i - nums[i])
            tmp = sum(nums[end_idx: i + 1])
            num_lst += [tmp]
        return int(sum(num_lst))

    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = 0
        def c_func(n, m): 
            if m == 0: 
                return 1
            a = [n - i for i in range(m)]
            b = [i + 1 for i in range(m)]
            f_a = 1 
            for x in a: 
                f_a *= x
            f_b = 1 
            for x in b: 
                f_b *= x
            return int(f_a / f_b)
        
        for l in range(k): 
            tmp = []
            for i in range(len(nums)): 
                # min 
                n = len(nums) - 1 - i
                m = l
                if n >= m: 
                    s_min = nums[i] * c_func(n, m)
                else: 
                    s_min = 0
                # max
                n = len(nums) - 1 - i
                m = l
                if n >= m: 
                    s_max = nums[len(nums) - 1 - i] * c_func(n, m)
                else: 
                    s_max = 0
                tmp += [s_min + s_max]
                # print(tmp)
                # import pdb 
                # pdb.set_trace()
            ret += sum(tmp)
        print(len(nums))
        return ret

    def mincost(self, n, idx, cost, flag): 
        vals = []
        idx_lst = []
        for i in range(3): 
            if idx == 2: 
                import pdb 
                pdb.set_trace()
            if flag[idx][i] == 1: 
                continue
            
            if idx < n - 1:
                flag[idx + 1][i] = 1 
            flag[idx - 1][i] = 1
            flag[n - 1 - idx][i] = 1

            tmp = cost[idx][i]
            if idx == n - 1:
                tmp2 = 0 
            else:
                tmp2 = self.mincost(n, idx + 1, cost, flag)
            vals += [tmp + tmp2]

            if idx < n - 1:
                flag[idx + 1][i] = 0
            flag[idx - 1][i] = 0
            flag[n - 1 - idx][i] = 0
        
        return min(vals)

    def minCost(self, n: int, cost: List[List[int]]) -> int:
        vals = []
        idx = []
        for i in range(3): 
            flag = [[0, 0, 0] for _ in range(n)]
            tmp = cost[0][i]
            flag[1][i] = 1 
            flag[n - 1][i] = 1
            tmp2 = self.mincost(n, 1, cost, flag)
            vals += [tmp + tmp2]
        
        return min(vals)

if __name__ == "__main__": 
    nums = [10,5,9,9,10,10,7,7,9,6,9,6,7,6,4,9,8,4,2,0,0,3,9,3,10,3,1,9,8,2,8,2,0,7,7,6,4,6,7,3,2,5,6,6,5,0,5,7,8,1]
    
    # test_case = (nums, )
    # ret = Solution().subarraySum(*test_case)

    nums = [10,5,9,9,10,10,7,7,9,6,9,6,7,6,4,9,8,4,2,0,0,3,9,3,10,3,1,9,8,2,8,2,0,7,7,6,4,6,7,3,2,5,6,6,5,0,5,7,8,1]
    k = 29
    test_case = (nums, k)
    ret = Solution().minMaxSums(*test_case)

    # n = 4
    # cost = [[3,5,7],[6,2,9],[4,8,1],[7,3,5]]
    # n = 6
    # cost = [[2,4,6],[5,3,8],[7,1,9],[4,6,2],[3,5,7],[8,2,4]]
    # test_case = (n, cost)
    # ret = Solution().minCost(*test_case)
    print(ret)