class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        MAX_INT = 10 ** 9
        # cands = []
        tmp = 1 
        def get_sorted_lst(num): 
            lst = []
            while num > 0: 
                lst.append(num % 10)
                num //= 10 
            return sorted(lst)
        tries = {}
        while tmp < 10 ** 9: 
            lst = get_sorted_lst(tmp)
            # cands.append(lst)
            d = tries
            for num in lst: 
                if num not in d: 
                    d[num] = {}
                d = d[num]
            d[""] = None
            tmp <<= 1 
        lst = get_sorted_lst(n)
        d = tries
        for num in lst: 
            if num not in d: 
                return False 
            d = d[num]
        return True if "" in d else False
    
if __name__ == "__main__": 
    n = 1
    n = 10
    n = 46
    ret = Solution().reorderedPowerOf2(n)
    print(ret)