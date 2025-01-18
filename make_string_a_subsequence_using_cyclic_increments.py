
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        """
        complexity: 
        """
        stack = []
        def detect_circular(c1, c2): 
            fn = lambda x: (x - ord('a')) % 26
            if fn(ord(c1) + 1) == fn(ord(c2)):
                return True 
        
        for i in range(len(str1)): 
            for j, (p, flag) in enumerate(stack): 
                if p == len(str2): 
                    return True
                
                if str1[i] == str2[p]: 
                    stack[j] = (p + 1, flag)
                elif flag in [0, 1] and detect_circular(str1[i], str2[p]): 
                    stack[j] = (p + 1, 1)
                # elif flag == 1: 
                #     stack[j] = (p + 1, 2)
            #     else: 
            #         stack[j] = None

            if str1[i] == str2[0]: # create new
                stack += [(1, 0)]
            elif detect_circular(str1[i], str2[0]): 
                stack += [(1, 1)]

            # stack = list(filter(lambda x: x is not None, stack))

        for p, flag in stack: 
            if p == len(str2): 
                return True
            
        return False
    
    def canMakeSubsequence_dp(self, str1: str, str2: str) -> bool:
        """
        simlar to LCS but it will get TLE
        n: len(str1)
        m: len(str2)
        complexity: O(n * m)
        """
        # table = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        # flag = [[False for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        table = [[0 for _ in range(len(str2) + 1)] for _ in range(2)]
        flag = [[False for _ in range(len(str2) + 1)] for _ in range(2)]
        # ret = False
        # if len(str2) == 0: ret = True
        def detect_circular(c1, c2): 
            fn = lambda x: (x - ord('a')) % 26
            if fn(ord(c1) + 1) == fn(ord(c2)):
                return True 
            
        for i, c1 in enumerate(str1): 
            for j, c2 in enumerate(str2): 
                # f = False
                tmp = [table[0][j + 1], table[1][j]]
                f_tmp = [flag[0][j + 1], flag[1][j]]
                if c1 == c2: # match
                    tmp += [table[0][j] + 1]
                    f_tmp += [flag[0][j]]
                elif not flag[0][j] and detect_circular(c1, c2): # circular match 
                    tmp += [table[0][j] + 1] 
                    f_tmp += [True]
                    # f = True
                # set value
                table[1][j + 1] = max(tmp)
                f = True 
                for x in f_tmp: 
                    f = f and x 
                flag[1][j + 1] = f

                if table[1][j + 1] == len(str2): 
                    return True
            # update
            table[0] = table[1]
            table[1] = [0 for _ in range(len(str2) + 1)]
            flag[0] = flag[1]
            flag[0] = [False for _ in range(len(str2) + 1)]
        

        return False
    
if __name__ == "__main__": 
    test_case = ("abc", "ad")
    # ("ab", "d")
    # ("zc", "ad")
    # ("abc", "ad")
    ret = Solution().canMakeSubsequence(*test_case)
    print(ret)