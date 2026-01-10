from typing import List

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        ret = [0] * numberOfUsers 
        ol_t = [0] * numberOfUsers
        events.sort(key=lambda x: (int(x[1]), -ord(x[0][0])))
        # print(events)
        al = [i for i in range(numberOfUsers)]
        def parse_user(ms, ts): 
            if ms == "ALL": 
                return al 
            elif ms == "HERE": 
                usrs = []
                for i in range(numberOfUsers): 
                    if ol_t[i] <= ts: 
                        usrs.append(i)
                return usrs 
            else: 
                usrs = []
                # print(ms)
                for s in ms.split(): 
                    # print(s)
                    usrs.append(int(s[2:])) 
                return usrs
        
        for tp, ts, ms in events: 
            ts = int(ts)
            if tp == "MESSAGE": 
                usrs = parse_user(ms, ts)
                for usr in usrs: 
                    ret[usr] += 1
            else: 
                usr = int(ms)
                ol_t[usr] = ts + 60
        return ret 
    
if __name__ == "__main__": 
    numberOfUsers = 2
    events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]
    numberOfUsers = 2
    events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]]
    numberOfUsers = 2
    events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]
    numberOfUsers = 3
    events = [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]]
    events = [["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]]
    ret = Solution().countMentions(numberOfUsers, events)
    print(ret)