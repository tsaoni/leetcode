from typing import List
from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_dict = defaultdict(int)
        for w in words: 
            words_dict[w] += 1
        match_lst = [defaultdict(int) for _ in range(len(s))]
        w_len = len(words[0])
        ret = []
        for i in range(len(s)): 
            print(i)
            # detect match words 
            match_word = ""
            for w in words: 
                if w in s[i: i + w_len]: 
                    match_word = w
                    break 
            # union with previous substrings
            sum_word_fn = lambda d: sum([v for k, v in d.items()])
            if len(match_word): 
                if i - w_len >= 0:
                    match_lst[i].update(match_lst[i - w_len])
                match_lst[i][match_word] += 1
                if match_lst[i][match_word] > words_dict[match_word]: 
                    # n_word = sum_word_fn(match_lst[i]) - 1
                    # n_char = n_word * w_len
                    # if s[i - n_char: i - n_char + w_len] == match_word: 
                    #     match_lst[i][match_word] -= 1
                    # else: 
                    if True:
                        # find the ckpt for the same word 
                        # match_lst[i][match_word] -= 1
                        idx = i - w_len
                        tmp = defaultdict(int)
                        while True: 
                            tmp[s[idx: idx + w_len]] += 1
                            # if s[idx: idx + w_len] == match_word and match_lst[idx][match_word] == 1: 
                            if tmp[match_word] == words_dict[match_word]:
                                break 
                            idx -= w_len
                        # tmp = defaultdict(int)
                        # tmp.update({k: v - match_lst[idx][k] for k, v in match_lst[i].items()})
                        match_lst[i] = tmp
                        # match_lst[i] = {}
            print(match_lst[i])
            if sum_word_fn(match_lst[i]) == sum_word_fn(words_dict): 
                n_word = sum_word_fn(match_lst[i]) - 1 
                n_char = n_word * w_len
                ret += [i - n_char]
            
                # n_word = sum([v for _, v in match_lst[i].items()]) - 1
                # n_char = n_word * w_len
                # ret += [i - n_char]
    
        return ret
    
if __name__ == "__main__": 
    test_case = ("wordgoodgoodgoodbestword", 
                 ["word","good","best","word"])
    # ("aaaaaaaaaaaaaa", 
    #              ["aa","aa"])
    # ("barfoofoobarthefoobarman", 
    #             ["bar","foo","the"])
    ("wordgoodgoodgoodbestword", 
                 ["word","good","best","word"])
    # ("barfoothefoobarman", 
    #             ["foo","bar"])
    ret = Solution().findSubstring(*test_case)
    print(ret)