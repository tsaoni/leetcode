from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)
        if modulo == 1 and k == 0: 
            return N * (N - 1) // 2 + N
        
        idxs = []
        for i in range(N): 
            if nums[i] % modulo == k: 
                idxs.append(i)
        
        # print(idxs)
        Ni = len(idxs)
        n_start_ids = [0] * Ni
        ret = 0
        get_start_length_fn = lambda i: idxs[i] - idxs[i - 1] if i > 0 else idxs[i] + 1
        get_end_length_fn = lambda i: idxs[i + 1] - idxs[i] if i < Ni - 1 else N - idxs[i] 
        for i in range(Ni): 
            n_end = get_end_length_fn(i)
            n_start = 0
            if k == 0: 
                n_start_ids[i] += get_start_length_fn(i)
                # print(n_start_ids[i])
                n_start = 0
                if i - modulo >= 0:
                    n_start_ids[i] += n_start_ids[i - modulo]
                if i - modulo + 1 >= 0:
                    n_start = n_start_ids[i - modulo + 1] 
            else:
                if i - k + 1 >= 0: 
                    n_start_ids[i] += get_start_length_fn(i - k + 1)
                    n_start = n_start_ids[i]
                if i - modulo >= 0:
                    n_start_ids[i] += n_start_ids[i - modulo]
                    n_start = n_start_ids[i]
            
            ret += n_start * n_end
            # import pdb 
            # pdb.set_trace()
        # print(n_start_ids)

        if k == 0: 
            pre = -1
            for idx in idxs + [N]: 
                ret += (idx - pre - 1)
                ret += (idx - pre - 1) * (idx - pre - 2) // 2
                pre = idx
        return ret
    
if __name__ == "__main__": 
    nums = [3,2,4]
    modulo = 2
    k = 1
    nums = [3,1,9,6]
    modulo = 3
    k = 0
    # nums = [2,4]
    # modulo = 7
    # k = 2
    # nums = [5,1,6] 
    # modulo = 2 
    # k = 1

    nums = [1,8,6,3,2,8,8] 
    modulo = 2 
    k = 0
    test_case = (nums, modulo, k)
    ret = Solution().countInterestingSubarrays(*test_case)
    print(ret)