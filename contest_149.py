from typing import List
from collections import defaultdict
import numpy as np

class Solution:
    def findValidPair(self, s: str) -> str:
        c_dict = defaultdict(int)
        for c in s: 
            c_dict[c] += 1
        ret = ""
        for i in range(len(s) - 1): 
            if not s[i] == s[i + 1]: 
                c1, c2 = s[i], s[i + 1]
                if c_dict[c1] == int(c1) and c_dict[c2] == int(c2): 
                    ret = s[i: i + 2]
                    return ret
        return ret

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # n = len(startTime)
        intervals = []
        startTime += [eventTime]
        endTime = [0] + endTime
        for s, e in zip(startTime, endTime): 
            intervals += [s - e]
        duration = 0
        for i in range(0, len(intervals) - k): 
            tmp = sum(intervals[i: i + k + 1])
            duration = max(duration, tmp)
        return duration

    def maxFreeTime2(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # n = len(startTime)
        intervals = []
        # startTime += [eventTime]
        # endTime = [0] + endTime
        for s, e in zip(startTime + [eventTime], [0] + endTime): 
            intervals += [s - e]
        duration = 0
        # print(intervals)
        for i in range(len(startTime)): 
            # tmp = sum(intervals[i: i + k + 1])
            tmp = intervals[: i] + [intervals[i] + intervals[i + 1] + (endTime[i] - startTime[i])] + intervals[i + 2:]
            # print(tmp)
            idxs = np.argsort(tmp)
            if tmp[idxs[-2]] - (endTime[i] - startTime[i]) >= 0: 
                t = tmp[idxs[-1]]
            else:
                t = tmp[idxs[-1]] - (endTime[i] - startTime[i])
            duration = max(duration, t)
            # print(t)
        return duration

    def minCostGoodCaption(self, caption: str) -> str:
        c_list = []
        r = [caption[0], 1]
        for c in caption[1:]: 
            if c == r[0]: 
                r[1] += 1 
            else: 
                c_list += [r]
                r = [c, 1]
        ret = []
        for i in range(c_list): 
            if c_list[i][1] >= 3: 
                for j in range(len(ret)):
                    ret[j] = r + c_list[i][0] * c_list[i][1]
            else: 
                if c_list[i][1] == 1: # sacrifice
                    tmp = []
                    a = []
                    if i > 0: 
                        a += [c_list[i - 1][0]]
                    if i < len(c_list) - 1: 
                        a += [c_list[i + 1][0]]
                    for r in ret: 
                        for x in a: 
                            tmp += [r + x]
                    if len(tmp): 
                        ret = tmp
                elif c_list[i][1] == 2: 
                    if i > 0 and c_list[i - 1][1] > 3: 
                        pass 
        return 

if __name__ == "__main__": 
    # s = "2523533"
    # test_case = (s, )
    # ret = Solution().findValidPair(*test_case)
    

    # eventTime = 5
    # k = 1
    # startTime = [1,3]
    # endTime = [2,5]
    
    eventTime = 10
    k = 1
    startTime = [0,2,9]
    endTime = [1,4,10]

    eventTime = 5
    startTime = [1,3]
    endTime = [2,5]

    # eventTime = 10
    # startTime = [0,7,9]
    # endTime = [1,8,10]

    # eventTime = 10
    # startTime = [0,3,7,9]
    # endTime = [1,4,8,10]

    test_case = (eventTime, startTime, endTime )
    ret = Solution().maxFreeTime2(*test_case)
    print(ret)
    