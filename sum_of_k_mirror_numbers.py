class Solution:
    def kMirror(self, k: int, n: int) -> int:
        ret = 0 
        n_digits = 1
        cur_k = 0
        def find(n_digits, cur, d_mirror, stack): 
            nonlocal cur_k, ret
            if cur_k < n: 
                if cur > d_mirror: 
                    if cur == d_mirror + 1: 
                        stack = stack + list(reversed(stack))
                    else: 
                        stack = stack + list(reversed(stack[: -1]))
                    num = 0 
                    for x in stack: 
                        num *= k
                        num += x
                    digits = [] 
                    tmp = num
                    while tmp > 0: 
                        digits.insert(0, tmp % 10)
                        tmp //= 10
                    for i in range(len(digits) // 2): 
                        if digits[i] != digits[-i - 1]: 
                            return
                    cur_k += 1 
                    ret += num
                    # print(num, stack)
                else:
                    start = 1 if cur == 0 else 0
                    for i in range(start, k): 
                        find(n_digits, cur + 1, d_mirror - 1, stack + [i])

        while cur_k < n: 
            find(n_digits, 0, n_digits - 1, [])
            n_digits += 1
        return ret 
    
if __name__ == "__main__": 
    k = 2
    n = 5
    # k = 3
    # n = 7
    k = 7
    n = 17
    ret = Solution().kMirror(k, n)
    print(ret)