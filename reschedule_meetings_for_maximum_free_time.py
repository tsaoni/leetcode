from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        startTime.append(eventTime)
        endTime.insert(0, 0)
        durations = [s - e for s, e in zip(startTime, endTime)]
        # print(durations)
        ret = sum(durations[: k + 1])
        tmp = ret
        for start in range(len(durations) - k - 1): 
            tmp = tmp - durations[start] + durations[start + k + 1]
            ret = max(tmp, ret)
            # print(ret)
        return ret
    
    def maxFreeTime_2(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        N = len(startTime)
        startTime.append(eventTime)
        endTime.insert(0, 0)
        fir_max_idx, sec_max_idx, thi_max_idx = -1, -1, -1
        for i, (s, e) in enumerate(zip(startTime, endTime)): 
            if fir_max_idx == -1 or s - e >= startTime[fir_max_idx] - endTime[fir_max_idx]: 
                thi_max_idx = sec_max_idx
                sec_max_idx = fir_max_idx 
                fir_max_idx = i 
            elif sec_max_idx == -1 or s - e >= startTime[sec_max_idx] - endTime[sec_max_idx]: 
                thi_max_idx = sec_max_idx 
                sec_max_idx = i 
            elif thi_max_idx == -1 or s - e >= startTime[thi_max_idx] - endTime[thi_max_idx]: 
                thi_max_idx = i 

        ret = 0
        for i in range(N): 
            if fir_max_idx not in [i, i + 1]: 
                d = startTime[fir_max_idx] - endTime[fir_max_idx]
            elif sec_max_idx not in [i, i + 1]: 
                d = startTime[sec_max_idx] - endTime[sec_max_idx] 
            else: 
                d = startTime[thi_max_idx] - endTime[thi_max_idx] 
            
            if d >= endTime[i + 1] - startTime[i]: 
                ret = max(ret, startTime[i + 1] - endTime[i])
            else: 
                ret = max(ret, startTime[i] - endTime[i] + startTime[i + 1] - endTime[i + 1])
            # startTime[i] - endTime[i]
            # startTime[i + 1] - endTime[i + 1]
            # endTime[i + 1] - startTime[i]
        return ret

if __name__ == "__main__": 
    # eventTime = 5
    # k = 1
    # startTime = [1,3]
    # endTime = [2,5]

    # eventTime = 10
    # k = 1
    # startTime = [0,2,9]
    # endTime = [1,4,10]

    # eventTime = 5
    # k = 2
    # startTime = [0,1,2,3,4]
    # endTime = [1,2,3,4,5]

    # eventTime = 99 
    # k = 1 
    # startTime = [7,21,25] 
    # endTime = [13,25,78]
    # ret = Solution().maxFreeTime(eventTime, k, startTime, endTime)
    # print(ret)

    eventTime = 5
    startTime = [1,3]
    endTime = [2,5]

    eventTime = 10
    startTime = [0,7,9]
    endTime = [1,8,10]

    eventTime = 10
    startTime = [0,3,7,9]
    endTime = [1,4,8,10]
    ret = Solution().maxFreeTime_2(eventTime, startTime, endTime) 
    print(ret)