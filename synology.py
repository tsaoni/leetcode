
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

if __name__ == "__main__": 
    x1 = "he are the generative ice tea"
    x2 = "we are the generative ai team"
    
    x1 = "she is shelly and he is jerry"
    x2 = "he is jerry and he is jeffery"

    test_case = (x1, x2)
    ret = SubtitleCalibrator().word_level_lss(*test_case)
    print(ret)