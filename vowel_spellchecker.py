from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """
        results in TLE
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        ret = []
        for query in queries: 
            s = 3
            cur = ""
            for word in wordlist: 
                status = 0
                if query == word: 
                    cur = word
                    break
                if not len(query) == len(word): 
                    continue
                for i in range(len(query)): 
                    if query[i] in vowels: 
                        if query[i] == word[i]: 
                            # equal 
                            status = max(status, 0)
                        elif abs(ord(query[i]) - ord(word[i])) == 32: 
                            # capitalization
                            status = max(status, 1)
                        elif word[i] in vowels: 
                            # vowel errors
                            # print(word[i], query[i])
                            # import pdb 
                            # pdb.set_trace()
                            status = max(status, 2)
                        else: 
                            # mismatch
                            status = max(status, 3)
                    else: 
                        if query[i] == word[i]: 
                            # equal 
                            status = max(status, 0)
                        elif abs(ord(query[i]) - ord(word[i])) == 32: 
                            # capitalization
                            status = max(status, 1)
                        else:
                            # mismatch
                            status = max(status, 3)
                        # import pdb 
                        # pdb.set_trace()
                # print(query, word, status)
                if status == 0: 
                    cur = word
                    break 
                else: 
                    # import pdb 
                    # pdb.set_trace()
                    if s > status: 
                        cur = word
                    s = min(s, status)
            ret.append(cur)    
        return ret           
    
if __name__ == "__main__": 
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    wordlist = ["yellow"]
    queries = ["YellOw"]
    ret = Solution().spellchecker(wordlist, queries)
    print(ret)