from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_dict = {k: len(k) for k in wordDict}
        sent_lst = []
        ptrs = []
        # for i in range(len(s)): 
        while True:
            if len(sent_lst) == 0: # first iter
                for k, v in word_dict.items(): 
                    if s[: v] == k: # match 
                        sent_lst += [[k]]
                        ptrs += [v]
            else: 
                new_sent_lst = []
                new_ptrs = []
                for i, p in enumerate(ptrs): 
                    if p >= 0 and p < len(s):
                        mth = 0
                        for k, v in word_dict.items(): 
                            if s[p: p + v] == k: # match 
                                if mth == 0:
                                    sent_lst[i] += [k]
                                    ptrs[i] = p + v 
                                    mth += 1
                                else: # match at least two words 
                                    new_sent_lst += [[x for x in sent_lst[i][:-1]] + [k]]
                                    new_ptrs += [p + v]
                                    mth += 1 
                        if mth == 0: 
                            ptrs[i] = -1 
                sent_lst += new_sent_lst 
                ptrs += new_ptrs
            # terminate cond 
            e = True
            for p in ptrs: 
                if p > 0 and p < len(s): 
                    e = False
            if e: break
            # print(ptrs)
            # import pdb 
            # pdb.set_trace()

        sents = []
        for p, sent in zip(ptrs, sent_lst): 
            if p >= 0: 
                sents += [" ".join(sent)]
    
        return sents
    
if __name__ == "__main__": 
    test_case = ("catsandog", 
                ["cats","dog","sand","and","cat"])
    # ("pineapplepenapple", 
    #         ["apple","pen","applepen","pine","pineapple"])
    ret = Solution().wordBreak(*test_case)
    print(ret)