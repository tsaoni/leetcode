from collections import defaultdict
from copy import deepcopy

class Solution:

    def minWindow3(self, s: str, t: str) -> str: 
        
        char_cnt = defaultdict(int)
        for c in t: 
            char_cnt[c] += 1 
        n_need = len(char_cnt)
        min_len = -1
        n_have = 0
        char_acc_cnt = defaultdict(int) 
        start = 0
        for i1 in range(0, len(s)): 
            c = s[i1]
            if c in char_cnt: 
                char_acc_cnt[c] += 1
                if char_acc_cnt[c] == char_cnt[c]: 
                    n_have += 1 
            
            # print(n_have, n_need)
        
            if n_have == n_need: 
                while True: 
                    tmp = s[start] 
                    if tmp in char_cnt: 
                        if char_acc_cnt[tmp] > char_cnt[tmp]: 
                            start += 1 
                            char_acc_cnt[tmp] -= 1 
                        else: 
                            break 
                    else: 
                        start += 1
                
                if min_len == -1: 
                    r = slice(start, i1 + 1)
                    min_len = i1 + 1 - start
                else: 
                    if i1 + 1 - start < min_len: 
                        r = slice(start, i1 + 1)
                        min_len = i1 + 1 - start

        if min_len == -1: 
            return "" 
        else: 
            return s[r]

            # for i2 in range(i1, len(s)): 
            #     c = s[i2]
            #     char_acc_cnt[c] += 1 
            #     if c in char_cnt and char_acc_cnt[c] == char_cnt[c]: 
            #         n_have += 1 
            #     if n_have == n_need: 
            #         end = i2 + 1 
            #         break 
            # if i1 == 0: 
            #     if n_have < n_need: 
            #         return ""
            #     else: 
            #         min_len = end - i1
            #         r = slice(i1, end)
            # elif n_have == n_need: 
            #     if end - i1 < min_len:
            #         min_len = end - i1 
            #         r = slice(i1, end)

        # print(r)     
        
        return s[r]

    # def minWindow3(self, s: str, t: str) -> str: # don't do this
    #     char_cnt = defaultdict(int)
    #     for c in t: 
    #         char_cnt[c] += 1 
    #     char_cnt = sorted([(k, v + 1) for k, v in char_cnt.items()], key=lambda x: x[0])
    #     def multiply(arr): 
    #         ret = 1
    #         for x in arr: 
    #             ret *= x 
    #         return ret 
        
    #     mul_arr = [x[1] for x in char_cnt[1:]] + [1]
    #     div = [multiply(mul_arr[-i - 1:]) for i in range(len(mul_arr))]
    #     div.reverse()
    #     module = [x[1] for x in char_cnt]

    #     print(div)
    #     print(module)
    #     N = multiply([x[1] for x in char_cnt])
    #     states = [-1] * N 

    #     for c in s: 
            
    #         import pdb 
    #         pdb.set_trace()
    #     return 
    
    def minWindow2(self, s: str, t: str) -> str:
        """
        results in TLE
        """
        char_cnt = defaultdict(int)
        for c in t: 
            char_cnt[c] += 1 
        
        char_acc_cnt = defaultdict(int)
        queue = []
        sufficient = False
        end = -1
        for i, c in enumerate(s): 
            if c in char_cnt:
                if False: #char_acc_cnt[c] < char_cnt[c]: 
                    # queue += [[c, i]]
                    # char_acc_cnt[c] += 1 
                           
                    # is_sufficient = all([x2 <= char_acc_cnt[x1] for x1, x2 in char_cnt.items()])
                    # is_min = sum([x2 == char_acc_cnt[x1] for x1, x2 in char_cnt.items()]) == 1
                    # print("suf", is_sufficient)
                    # print("min", is_min)
                    if is_sufficient and is_min: 
                        end = len(queue) - 1
                    
                else: 
                    queue += [[c, i]]
                    char_acc_cnt[c] += 1 
                    idx = 0
                    tmp_acc_cnt = deepcopy(char_acc_cnt)
                    while True: 
                        tmp = queue[idx][0]
                        if tmp_acc_cnt[tmp] > char_cnt[tmp]: 
                            idx += 1 
                            tmp_acc_cnt[tmp] -= 1
                        else: 
                            break 
                    if i - queue[idx][1] <= queue[end][1] - queue[0][1]:
                        # import pdb 
                        # pdb.set_trace()
                        char_acc_cnt = tmp_acc_cnt
                        queue = queue[idx: ]
                        end = len(queue) - 1
                    

                    if not sufficient: 
                        if all([char_acc_cnt[x1] >= x2 for x1, x2 in char_cnt.items()]): 
                            sufficient = True
                        end = len(queue) - 1

                    # if is_sufficient and is_min: 
                    #     end = len(queue) - 1    

                        # print(end)
                    # if c == queue[0][0]:
                    #     if i - queue[end][1] < queue[1][1] - queue[0][1]: 
                    #         queue.pop(0)
                    #         while True: 
                    #             tmp = queue[0][0]
                    #             if char_acc_cnt[tmp] > char_cnt[tmp]: 
                    #                 queue.pop(0)
                    #             else: 
                    #                 break
                            # end = len(queue) - 1
            # print(char_cnt)
            # print(char_acc_cnt)
            # print(queue)
            # print(end)

        if len(queue):
            idx = 0
            char_acc_cnt = defaultdict(int)
            for x in queue[: end + 1]:
                tmp = x[0] 
                char_acc_cnt[tmp] += 1
            # print(char_acc_cnt)
            # print(char_cnt)
            while True: 
                tmp = queue[idx][0]
                if char_acc_cnt[tmp] > char_cnt[tmp]: 
                    idx += 1 
                    char_acc_cnt[tmp] -= 1
                else: break 
            start = queue[idx][1] 

            idx = end
            while True: 
                tmp = queue[idx][0]
                if char_acc_cnt[tmp] > char_cnt[tmp]: 
                    idx -= 1 
                    char_acc_cnt[tmp] -= 1
                else: break 
            end = idx
            end = queue[end][1]
            ret = s[start: end + 1] #end + 1 - start
        else: ret = ""
        for k, v in char_cnt.items(): 
            if char_acc_cnt[k] < v: 
                ret = ""
        # print(s[start: end + 1])
        return ret
    
    def minWindow1(self, s: str, t: str) -> str:
        """
        I just forget how to implement... 
        """
        rec = []
        d = []
        t_dict = defaultdict(int)
        for c in t: 
            t_dict[c] += 1
        for c in s: 
            if c in t: 
                for i in range(len(rec)): 
                    rec[i][c]
                    d[i]
                rec += [t_dict]
                rec[-1][c] -= 1
                d += [1]
            import pdb 
            pdb.set_trace()
        return 

    def comb(self, cnt_dict, keys): 
        if len(keys) == 0: 
            return []
        c = keys.pop(0)
        cnt = cnt_dict[c]
        states = [{c: i} for i in range(0, cnt + 1)]
        prev = self.comb(cnt_dict, keys)
        ret = []
        if len(prev) > 0:
            for s in states: 
                for ps in prev:
                    ret += [{**s, **ps}]
        else: 
            ret = states
        return ret

    def minWindow(self, s: str, t: str) -> str:
        """
        I just forget how to implement... 
        """
        # create combinations of t 
        cnt_dict = defaultdict(int)
        for c in t: 
            cnt_dict[c] += 1
        # print(cnt_dict)
        keys = list(cnt_dict.keys())
        states = self.comb(cnt_dict, keys)

        # return states
        # computing minimal windows
        """
        the ones that contain a single character should be updated proactively
        """

        for c in s: 
            # select states contain at least one of c
            
            # update windows of states 
            
            import pdb 
            pdb.set_trace()
        return 

if __name__ == "__main__": 
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "a"
    # s = "a"
    # t = "aa"
    # s = "aaaaaaaaaaaabbbbbcdd"
    # t = "abcdd"
    # s = "cabwefgewcwaefgcf"
    # t = "cae"
    # s = "abcabdebac" 
    # t = "cda"
    # s = "aaabdabcefaecbef"
    # t = "abc"
    # s = "abABaBBBBb"
    # t = "abb"
    # s = "onlswwtraopuasovmrmdouldsqiryidoxpgtlcmnschswxpirbmfxzkqpsjncnebekupoheglmyhlqsctgirfsjunskrfotj"
    # t = "apapyfvjtwtemnhf"
    test_case = (s, t)
    ret = Solution().minWindow3(*test_case)
    print(ret)