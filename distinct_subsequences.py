class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prev_cnt_lst = [0] * len(s)
        for i, c_t in enumerate(t): 
            f_cnt = 0
            cur_cnt_lst = []
            for j, c_s in enumerate(s): 
                if i == 0: # first iter
                    if c_t == c_s: 
                        f_cnt += 1 
                    cur_cnt_lst += [f_cnt]
                else: 
                    if j == 0: 
                        cur_cnt_lst += [0]
                    else:
                        tmp = cur_cnt_lst[-1]
                        if c_t == c_s: 
                            tmp += prev_cnt_lst[j - 1]
                        cur_cnt_lst += [tmp]
            prev_cnt_lst = cur_cnt_lst
        return cur_cnt_lst[-1]
    
if __name__ == "__main__": 
    test_case = ("babgbag", "bag")
    #("rabbbit", "rabbit")
    ret = Solution().numDistinct(*test_case)
    print(ret)