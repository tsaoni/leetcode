class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        tmp = k 
        bits = ""
        while tmp > 0: 
            bits = str(tmp % 2) + bits 
            tmp //= 2 
    
        N = len(s)
        cnt0 = [0] * N
        for i in range(N): 
            if i > 0:
                cnt0[i] += cnt0[i - 1]
            if s[i] == "0": 
                cnt0[i] += 1
        # print(cnt0)
        # print(len(bits))
        start = N - 1
        ret = min(len(bits) - 1, len(s))
        end = 0
        while start >= 0:
            if True: #s[start] == "1": 
                end = 0
                i = start
                while i < N: 
                    if end == len(bits): 
                        break
                    if int(s[i]) < int(bits[end]): 
                        end = min(N - i - 1 + (end + 1), len(bits))
                        break
                    elif int(s[i]) == int(bits[end]): 
                        end += 1 
                        i += 1
                    else: 
                        i += 1
                
                # print(i)
                # import pdb 
                # pdb.set_trace()
                ret = max(ret, cnt0[start - 1] + end if start > 0 else end)
            
            start -= 1 
        return ret 
    
if __name__ == "__main__": 
    s = "1001010"
    k = 5
    # s = "00101001"
    # k = 1
    s = "001010101011010100010101101010010" 
    k = 93951055
    s = "1011"
    k = 281854076
    ret = Solution().longestSubsequence(s, k)
    print(ret)