from typing import List
import heapq 

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.mp = [None] * (10 ** 5 + 1)
        self.pq = []
        for userId, taskId, priority in tasks:
            self.pq.append((-priority, -taskId, userId))
        heapq.heapify(self.pq)
        
        for i in range(len(self.pq)):
            _, taskId, _ = self.pq[i]
            taskId = -taskId
            self.mp[taskId] = i

    def add(self, userId: int, taskId: int, priority: int) -> None:
        idx = self.mp[taskId] = len(self.pq)
        self.pq.append((-priority, -taskId, userId))
        while idx > 0: 
            p = (idx - 1) // 2 
            if self.pq[idx] < self.pq[p]: 
                ptidx = -self.pq[p][1]
                if self.mp[ptidx] is not None:
                    self.mp[ptidx] = idx 
                tmp = self.pq[idx]
                self.pq[idx] = self.pq[p]
                self.pq[p] = tmp 
            else: 
                break 
            idx = p
        self.mp[taskId] = idx

    def edit(self, taskId: int, newPriority: int) -> None:
        idx = self.mp[taskId]
        self.pq[idx] = (-newPriority, -taskId, self.pq[idx][2])
        while idx > 0: 
            p = (idx - 1) // 2 
            if self.pq[idx] < self.pq[p]: 
                ptidx = -self.pq[p][1]
                if self.mp[ptidx] is not None:
                    self.mp[ptidx] = idx 
                tmp = self.pq[idx]
                self.pq[idx] = self.pq[p]
                self.pq[p] = tmp 
            else: 
                break 
            idx = p
        while idx * 2 + 1 < len(self.pq): 
            if idx * 2 + 2 == len(self.pq): 
                child = idx * 2 + 1 
            elif self.pq[idx * 2 + 1] < self.pq[idx * 2 + 2]: 
                child = idx * 2 + 1 
            else: 
                child = idx * 2 + 2 
            if self.pq[child] < self.pq[idx]: 
                ctidx = -self.pq[child][1]
                if self.mp[ctidx] is not None:
                    self.mp[ctidx] = idx 
                tmp = self.pq[idx]
                self.pq[idx] = self.pq[child]
                self.pq[child] = tmp 
            else: 
                break 
            idx = child
        self.mp[taskId] = idx
        

    def rmv(self, taskId: int) -> None:
        idx = self.mp[taskId]
        self.mp[taskId] = None
        if idx == len(self.pq) - 1: 
            self.pq.pop(-1)
        else:
            # print(idx, len(self.pq))
            self.pq[idx] = self.pq.pop(-1)
            taskId = -self.pq[idx][1]
            while idx > 0: 
                p = (idx - 1) // 2 
                if self.pq[idx] < self.pq[p]: 
                    ptidx = -self.pq[p][1]
                    if self.mp[ptidx] is not None:
                        self.mp[ptidx] = idx 
                    tmp = self.pq[idx]
                    self.pq[idx] = self.pq[p]
                    self.pq[p] = tmp 
                else: 
                    break 
                idx = p
            while idx * 2 + 1 < len(self.pq): 
                if idx * 2 + 2 == len(self.pq): 
                    child = idx * 2 + 1 
                elif self.pq[idx * 2 + 1] < self.pq[idx * 2 + 2]: 
                    child = idx * 2 + 1 
                else: 
                    child = idx * 2 + 2 
                if self.pq[child] < self.pq[idx]: 
                    ctidx = -self.pq[child][1]
                    if self.mp[ctidx] is not None:
                        self.mp[ctidx] = idx 
                    tmp = self.pq[idx]
                    self.pq[idx] = self.pq[child]
                    self.pq[child] = tmp 
                else: 
                    break 
                idx = child
            self.mp[taskId] = idx
        
        # print(taskId, self.mp[taskId])

        

    def execTop(self) -> int:
        userId = -1
        while len(self.pq) > 0:
            taskId = -self.pq[0][1]
            # print(taskId, self.mp[taskId])
            if self.mp[taskId] is not None: 
                idx = self.mp[taskId]
                userId = self.pq[idx][2]
                self.mp[taskId] = None
            if True: 
                last = self.pq.pop(-1)
                if len(self.pq) > 0:
                    self.pq[0] = last 
                    taskId = -last[1]
                    idx = 0
                    while idx * 2 + 1 < len(self.pq): 
                        if idx * 2 + 2 == len(self.pq): 
                            child = idx * 2 + 1 
                        elif self.pq[idx * 2 + 1] < self.pq[idx * 2 + 2]: 
                            child = idx * 2 + 1 
                        else: 
                            child = idx * 2 + 2 
                        if self.pq[child] < self.pq[idx]: 
                            ctidx = -self.pq[child][1]
                            if self.mp[ctidx] is not None: 
                                self.mp[ctidx] = idx 
                            tmp = self.pq[idx]
                            self.pq[idx] = self.pq[child]
                            self.pq[child] = tmp 
                        else: 
                            break 
                        idx = child
                    if self.mp[taskId] is not None:
                        self.mp[taskId] = idx
            if userId != -1: 
                break 
        # print(self.pq)
        return userId


func = ["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
args = [[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

# func = ["TaskManager","rmv","execTop"]
# args = [[[[10,26,25]]],[26],[]]

# func = ["TaskManager","execTop","rmv","execTop"] 
# args = [[[[6,4,48],[2,7,45],[6,28,44],[10,27,10]]],[],[7],[]]

func = ["TaskManager","rmv","rmv","execTop"] 
args = [[[[1,17,32],[5,4,49]]],[4],[17],[]]

func = ["TaskManager","rmv","rmv","execTop","execTop"] 
args = [[[[8,9,14],[9,11,43],[2,20,7],[3,12,20]]],[9],[12],[],[]]

# func = ["TaskManager","edit","rmv","rmv","edit","add","add","add","execTop","edit","edit","edit","edit","execTop"] 
# args = [[[[7,15,28],[3,8,21],[1,11,12],[1,5,39],[10,19,30],[9,22,42],[4,28,24]]],[11,19],[19],[8],[11,27],[7,26,48],[2,18,46],[0,19,41],[],[5,16],[22,9],[28,28],[18,22],[]]

ret = []
for f, a in zip(func, args): 
    if f == "TaskManager": 
        obj = TaskManager(*a)
        ret.append(None)
        print(f, a, obj.pq)
    elif f == "add": 
        obj.add(*a)
        ret.append(None)
        print(f, a, obj.pq)
    elif f == "edit": 
        obj.edit(*a)
        ret.append(None)
        print(f, a, obj.pq)
    elif f == "rmv": 
        obj.rmv(*a)
        ret.append(None)
        print(f, a, obj.pq)
    elif f == "execTop": 
        s = obj.execTop(*a)
        ret.append(s)
        print(f, a, obj.pq)

print(ret)

# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()