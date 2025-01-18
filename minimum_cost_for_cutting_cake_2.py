from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(key=lambda x: -x)
        verticalCut.sort(key=lambda x: -x)
        h_cnt_lst, h_cut = [1 for i in range(m)], [1 for i in range(m)]
        v_cnt_lst, v_cut = [1 for i in range(n)], [1 for i in range(n)]
        h_val, v_val = horizontalCut, verticalCut #[x for x in horizontalCut], [x for x in verticalCut]
        if m > 1 and n > 1:
            h_max, v_max = horizontalCut[0], verticalCut[0] #max(horizontalCut), max(verticalCut)
            h_idx, v_idx = 0, 0
            while True: #h_max > 0 and v_max > 0: 
                if h_max > v_max: 
                    # h_idx = horizontalCut.index(h_max)
                    v_cnt_lst = [v_cnt_lst[i] + 1 if v_cut[i] else v_cnt_lst[i] for i in range(n - 1)]
                    h_cut[h_idx] = 0
                    # horizontalCut[h_idx] = -1
                    h_idx += 1
                    if h_idx == m - 1: break
                    h_max = horizontalCut[h_idx] #max(horizontalCut)
                else: 
                    # v_idx = verticalCut.index(v_max)
                    h_cnt_lst = [h_cnt_lst[i] + 1 if h_cut[i] else h_cnt_lst[i] for i in range(m - 1)]
                    v_cut[v_idx] = 0
                    # verticalCut[v_idx] = -1
                    v_idx += 1
                    if v_idx == n - 1: break
                    v_max = verticalCut[v_idx] #max(verticalCut)

        h_ret, v_ret = [], []

        if m > 1:
            h_ret = [cnt * cut for cnt, cut in zip(h_cnt_lst, h_val)]
        if n > 1:
            v_ret = [cnt * cut for cnt, cut in zip(v_cnt_lst, v_val)]

        return sum(h_ret + v_ret)
    
if __name__ == "__main__": 
    test_case = (3, 2, [1, 3], [5])
    ret = Solution().minimumCost(*test_case)
    print(ret)