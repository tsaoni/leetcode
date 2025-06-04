class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1: 
            return word 
        else: 
            start_idx1 = 0
            start_idx2 = -1
            for i in range(1, len(word)): 
                c = word[i]
                if c > word[start_idx1]: 
                    start_idx1 = i 
                    start_idx2 = -1 
                elif c == word[start_idx1]: 
                    if start_idx2 < 0:
                        start_idx2 = i 
               
                if start_idx2 > 0: 
                    cur1 = start_idx1 + (i - start_idx2)
                    if c > word[cur1]: 
                        start_idx1 = start_idx2 
                        start_idx2 = -1 
                    elif c == word[cur1]: 
                        if cur1 + 1 == start_idx2: 
                            start_idx2 = -1 
                    else: 
                        start_idx2 = -1 
            
            length = len(word) - max(numFriends - 1, start_idx1)
            # print(start_idx1, length)
            return word[start_idx1: start_idx1 + length]
    
if __name__ == "__main__": 
    word = "dbca"
    numFriends = 2
    word = "gggg"
    numFriends = 4
    word = "aann"
    numFriends = 2
    word = "gh"
    numFriends = 1
    # word = "epbbppl" 
    # numFriends = 2
    ret = Solution().answerString(word, numFriends)
    print(ret)