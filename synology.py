from collections import defaultdict, Counter

class SubtitleCalibrator: 
    def word_level_lcs(
        self, subtitle_before_calibration: str, subtitle_after_calibration: str, 
    ): 
        bwl = subtitle_before_calibration.split()
        awl = subtitle_after_calibration.split()
        Nb, Na = len(bwl), len(awl)
        table = [[[] for _ in range(Nb + 1)] for _ in range(Na + 1)]
        for i in range(1, Na + 1): 
            for j in range(1, Nb + 1): 
                if bwl[j - 1] == awl[i - 1]: 
                    table[i][j] += table[i - 1][j - 1]
                    table[i][j] += [bwl[j - 1]]
                else: 
                    x1, x2 = len(table[i - 1][j]), len(table[i][j - 1])
                    if x1 > x2: 
                        table[i][j] += table[i - 1][j]
                    else: 
                        table[i][j] += table[i][j - 1]
        
        return table[-1][-1]
    
    def word_level_lss(
        self, subtitle_before_calibration: str, subtitle_after_calibration: str, 
    ): 
        bwl = subtitle_before_calibration.split()
        awl = subtitle_after_calibration.split()
        Nb, Na = len(bwl), len(awl)
        table = [[[] for _ in range(Nb + 1)] for _ in range(Na + 1)]
        
        def similar_check(w1, w2): 
            N1 = len(w1)
            N2 = len(w2)
            t = [[0] * (N1 + 1) for _ in range(N2 + 1)]
            for i in range(1, N2 + 1): 
                for j in range(1, N1 + 1): 
                    if w2[i - 1] == w1[j - 1]: 
                        t[i][j] = t[i - 1][j - 1] + 1 
                    else: 
                        t[i][j] = max(t[i - 1][j], t[i][j - 1])
            
            if max(N1, N2) - t[-1][-1] <= 3: 
                return True 
            else: 
                return False


        for i in range(1, Na + 1): 
            for j in range(1, Nb + 1): 
                if similar_check(awl[i - 1], bwl[j - 1]): 
                    table[i][j] += table[i - 1][j - 1]
                    table[i][j] += [awl[j - 1]]
                else: 
                    x1, x2 = len(table[i - 1][j]), len(table[i][j - 1])
                    if x1 > x2: 
                        table[i][j] += table[i - 1][j]
                    else: 
                        table[i][j] += table[i][j - 1]
        
        return table[-1][-1]


# 25.04.07
class Node: 
    def __init__(self, val, left, right): 
        self.val = val 
        self.left = left 
        self.right = right

cost = 0
def total_cost(root): 
    if root is None: 
        return 0
    return root.val + total_cost(root.left) + total_cost(root.right)
    
# cur.acc_val 
def total_cost1(cur, parent, grandparent): 
    if parent is None and grandparent is None: 
        cur.acc_val = cur.val 
    elif grandparent is None: 
        cur.acc_val = max(cur.val, parent.val)
    else: 
        cur.acc_val = max(cur.val + grandparent.acc_val, parent.acc_val)

    if cur.left is None and cur.right is None: #leaf 
        return cur.acc_val

    lval = total_cost1(cur.left, cur, parent)
    rval = total_cost1(cur.right, cur, parent)
    
    return max(lval, rval)

def total_cost2(cur): 
    if cur.left is None and cur.right is None: #leaf 
        cur.ret_val = cur.val
        cur.not_ret_val = 0

    lval = total_cost1(cur.left)
    rval = total_cost1(cur.right)
    
    cur.ret_val = cur.val + cur.left.not_ret_val + cur.right.not_ret_val
    cur.not_ret_val = max(cur.left.ret_val, cur.left.not_ret_val) + \
        max(cur.right.ret_val, cur.right.not_ret_val)

    return max(cur.ret_val, cur.not_ret_val)

# 1

# 10  3 

# 4  5  6


if __name__ == "__main__": 
    x1 = "he are the generative ice tea"
    x2 = "we are the generative ai team"
    
    x1 = "she is shelly and he is jerry"
    x2 = "he is jerry and he is jeffery"

    test_case = (x1, x2)
    ret = SubtitleCalibrator().word_level_lss(*test_case)
    print(ret)