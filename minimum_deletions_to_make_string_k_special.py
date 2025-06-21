class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        freq = Counter()
        for c in word: 
            freq[c] += 1 
        freq = sorted([f for _, f in freq.items()])
        # print(freq)
        ret = 0 
        idx = 0
        acc = 0
        while idx < len(freq) and freq[idx] <= freq[0] + k: 
            idx += 1
        for i in range(len(freq) - 1):
            if idx == len(freq): 
                return ret 
            tmp = 0
            ub = freq[i + 1] + k
            while idx < len(freq) and freq[idx] <= ub: 
                tmp += freq[idx] - (freq[i] + k)
                idx += 1
            tmp += (freq[i + 1] - freq[i]) * (len(freq) - idx)
            # print(tmp, freq[i])
            ret = min(acc + freq[i], acc + tmp, ret + tmp)
            acc += freq[i]
            # if tmp >= freq[i]:  
            #     ret += freq[i]
            # else: 
            #     ret += tmp
            #     break 

        # print(idx)
        # while idx < len(freq): 
        #     ret += freq[idx] - ub
        #     idx += 1
        return ret
    
if __name__ == "__main__": 
    word = "aabcaba"
    k = 0
    # word = "dabdcbdcdcd"
    # k = 2
    # word = "aaabaaa"
    # k = 2
    word = "yynaayyyy" 
    k = 1
    # word = "qbbbbvbbbvqb" 
    # k = 0
    ret = Solution().minimumDeletions(word, k)
    print(ret)