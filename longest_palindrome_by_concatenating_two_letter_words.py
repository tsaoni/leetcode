from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = [[0] * 26 for _ in range(26)]
        for w in words: 
            idx1, idx2 = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            cnt[idx1][idx2] += 1 
        l = 0
        mid = 0
        for i in range(26): 
            for j in range(26): 
                if i > j: 
                    l += min(cnt[i][j], cnt[j][i]) * 4
                elif i == j: 
                    if mid == 0 and cnt[i][j] & 1: 
                        mid = 1 
                        l += cnt[i][j] * 2 
                    else: 
                        if cnt[i][j] & 1: 
                            l += (cnt[i][j] - 1) * 2 
                        else: 
                            l += cnt[i][j] * 2
                else: 
                    break 
        return l
    
if __name__ == "__main__": 
    words = ["lc","cl","gg"]
    words = ["ab","ty","yt","lc","cl","ab"]
    words = ["cc","ll","xx"]
    ret = Solution().longestPalindrome(words)
    print(ret)