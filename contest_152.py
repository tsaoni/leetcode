from typing import List
from collections import defaultdict
from copy import deepcopy
import math

import string
class Spreadsheet:

    def __init__(self, rows: int):
        self.table = {}
        for c in string.ascii_uppercase: 
            self.table[c] = [0] * rows 
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        r, col = cell[0], int(cell[1:]) - 1
        self.table[r][col] = value

    def resetCell(self, cell: str) -> None:
        r, col = cell[0], int(cell[1:]) - 1
        self.table[r][col] = 0

    def getValue(self, formula: str) -> int:
        num1, num2 = formula[1:].split("+")
        vals = []
        for n in [num1, num2]: 
            if n[0] in string.ascii_uppercase: 
                r, col = n[0], int(n[1:]) - 1
                vals += [self.table[r][col]] 
            else: 
                vals += [int(n)]
        return sum(vals)

# Your Spreadsheet object will be instantiated and called as such:

# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

# exit(-1)

class Solution: 
    def func(): 
        return 
    
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = defaultdict(int)
        for d in digits: 
            cnt[d] += 1 

        ret = 0
        for num, c in cnt.items(): 
            if num % 2 == 0: 
                tmp = deepcopy(cnt)
                tmp[num] -= 1 
                for num1, c1 in tmp.items(): 
                    if num1 > 0 and c1 > 0: 
                        tmp[num1] -= 1 
                        for num2, c2 in tmp.items(): 
                            if c2 > 0: 
                                ret += 1 
                        tmp[num1] += 1
        
        return ret

    def longestCommonPrefix2(self, words: List[str], k: int) -> List[int]:
        N = max([len(w) for w in words])
        cnt, ncnt = {"": 0}, {}
        match = ["" for _ in words]
        for i in range(N): 
            for w in words: 
                if i < len(w): 
                    if w[: i] in cnt: 
                        if w[: i + 1] in ncnt: 
                            ncnt[w[: i + 1]] += 1
                        else: 
                            ncnt[w[: i + 1]] = 1
            cnt = {}
            for s, c in ncnt.items(): 
                if c >= k: 
                    cnt[s] = c 
            ncnt = {}

        

    def longestCommonPrefix1(self, words: List[str], k: int) -> List[int]:
        """
        """
        def find_max_prefix(words, k):
            # print(words)
            def good(num): 
                cnt, ncnt = {"": 0}, {}
                for i in range(num): 
                    for w in words: 
                        if i < len(w): 
                            if w[: i] in cnt: 
                                if w[: i + 1] in ncnt: 
                                    ncnt[w[: i + 1]] += 1
                                else: 
                                    ncnt[w[: i + 1]] = 1
                    cnt = {}
                    for s, c in ncnt.items(): 
                        if c >= k: 
                            cnt[s] = c 
                    ncnt = {}
                # print(num)
                # print(cnt)
                return cnt
            
            word_len = [len(w) for w in words]
            max_word_len = max(word_len)
            left, right = 0, max_word_len
            rcnt = {}
            while True: 
                mid = math.ceil((left + right) / 2)
                if left == mid: 
                    break
                cnt = good(mid)
                if len(cnt) > 0: 
                    rcnt = cnt
                    left = mid
                else: 
                    right = mid - 1
            return left, rcnt
        
        if len(words) == 1: 
            return [0]
        
        valk, cntk = find_max_prefix(words, k)
        # valk1, cntk1 = find_max_prefix(words, k + 1)
        # print(valk)
        # print(cntk)
        # print(valk1)
        # print(cntk1)
        ret = []
        for i, w in enumerate(words): 
            s = w[: valk]
            if s in cntk:
                if cntk[s] > k: 
                    ret += [valk] 
                else: 
                    if len(cntk) > 1: 
                        ret += [valk] 
                    else:
                        val, _ = find_max_prefix(words[: i] + words[i + 1: ], k)
                        ret += [val]
            else: 
                ret += [valk]
        # for i in range(len(words)): 
        #     val = find_max_prefix(words[: i] + words[i + 1: ])
        #     ret += [val]
        return ret

    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        """
        results in TLE
        """
        def find_max_prefix(i_words):
            # print(i_words)
            def good(num): 
                cnt, ncnt = {"": 0}, {}
                for i in range(num): 
                    for w in i_words: 
                        if i < len(w): 
                            if w[: i] in cnt: 
                                if w[: i + 1] in ncnt: 
                                    ncnt[w[: i + 1]] += 1
                                else: 
                                    ncnt[w[: i + 1]] = 1
                    cnt = {}
                    for s, c in ncnt.items(): 
                        if c >= k: 
                            cnt[s] = c 
                    ncnt = {}
                # print(num)
                # print(cnt)
                return len(cnt) > 0
            
            word_len = [len(w) for w in i_words]
            max_word_len = max(word_len)
            left, right = 0, max_word_len
            while True: 
                mid = math.ceil((left + right) / 2)
                if left == mid: 
                    break
                if good(mid): 
                    left = mid
                else: 
                    right = mid - 1
            return left
        
        if len(words) == 1: 
            return [0]
        ret = []
        for i in range(len(words)): 
            val = find_max_prefix(words[: i] + words[i + 1: ])
            ret += [val]
        return ret

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        
        return 

if __name__ == "__main__": 
    # digits = [1,3,5]
    # test_case = (digits, )
    # ret = Solution().totalNumbers(*test_case)
    # print(ret)

    words = ["jump","run","run","jump","run"]
    k = 2
    # words = ["dog","racer","car"]
    # k = 2
    # words = ["fdcc","ccfef","acaa","adfa","afc","fdbda"] 
    # k = 1
    words = ["efea","ceb","aff","ebb","cffaf","b","faaf","fbe","aed","dacc","ddd","fda"] 
    k = 1
    test_case = (words, k)
    ret = Solution().longestCommonPrefix1(*test_case)
    print(ret)

    # edges = [[0,1,1],[1,2,3],[1,3,1],[2,4,6],[4,7,2],[3,5,2],[3,6,5],[6,8,3]]
    # nums = [1,1,0,3,1,2,1,1,0] 
    # test_case = (edges, nums)
    # ret = Solution().longestSpecialPath(*test_case)
    # print(ret)

