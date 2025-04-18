from typing import List
import math
import time

from collections import defaultdict, Counter, deque


class Router:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit 
        self.memory = []
        self.metadata = defaultdict(list)
        
    def search(self, dest, start, end, t, op): 
        if op == "u": 
            if t <= dest[0]:
                return 0 
            if t > dest[-1]: 
                return -1
        else: 
            if t >= dest[-1]: 
                return len(dest) - 1
            if t < dest[0]: 
                return -1
        # if start >= end: 
            # if start == len(dest) - 1 and t >= dest[start]: 
            #     return start
            # return -1

        # print(len(dest))
        # print(start, end, dest[start], dest[end], t, op)
        
        if op == "u": 
            mid = (start + end) // 2 
            if mid < len(dest) - 1 and dest[mid] < t and dest[mid + 1] >= t: 
                return mid + 1
            elif mid == 0 and dest[mid] == t: 
                return mid
            elif t <= dest[mid]:
                return self.search(dest, start, mid, t, op)
            else:
                return self.search(dest, mid + 1, end, t, op)
        else: 
            mid = (start + end) // 2 
            if mid < len(dest) - 1 and dest[mid] <= t and dest[mid + 1] > t: 
                return mid 
            elif mid == len(dest) - 1 and dest[mid] == t: 
                return mid 
            elif t < dest[mid]:
                return self.search(dest, start, mid, t, op)
            else:
                return self.search(dest, mid + 1, end, t, op)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        p = [source, destination, timestamp]
        if p in self.memory: 
            return False
        self.memory.append(p)
        self.metadata[destination].append(timestamp)
        if len(self.memory) > self.limit: 
            _, dest, _ = self.memory.pop(0)
            self.metadata[dest].pop(0)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.memory) > 0: 
            _, dest, _ = self.memory[0]
            self.metadata[dest].pop(0)
            return self.memory.pop(0)
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        cnt = 0
        dest = self.metadata[destination]
        if len(dest) == 0: 
            return 0
        dest = sorted(dest)
    
        sidx = self.search(dest, 0, len(dest) - 1, startTime, "u")
        eidx = self.search(dest, 0, len(dest) - 1, endTime, "l")
        # print(sidx, eidx)
        if sidx >= 0 and eidx >= 0: 
            return eidx - sidx + 1
        else: 
            return 0

class Router1:

    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit 
        self.memory = []
        self.seen = set()
        self.metadata = defaultdict(list)
    
    def iter_search_left(self, dest, start, end, t): 
        while True: 
            if start == end: 
                return start + 1 if dest[start] < t else start 
            else:
                mid = (start + end + 1) // 2 
                if dest[mid] < t: 
                    start = mid
                else: 
                    end = mid - 1

    def iter_search_right(self, dest, start, end, t): 
        while True: 
            if start == end: 
                return start if dest[start] > t else start + 1
            else:
                mid = (start + end) // 2 
                if dest[mid] > t: 
                    end = mid
                else: 
                    start = mid + 1

    def search_left(self, dest, start, end, t): 
        if start == end: 
            return start + 1 if dest[start] < t else start 
        # elif start == end - 1: 
        #     if dest[start] >= t: 
        #         return start 
        #     elif dest[start] < t and dest[end] >= t: 
        #         return end
        #     else: 
        #         return end + 1
        
        mid = (start + end + 1) // 2 
        if dest[mid] < t: 
            return self.search_left(dest, mid, end, t)
        else: 
            return self.search_left(dest, start, mid - 1, t)


    def search_right(self, dest, start, end, t): 
        if start == end: 
            return start if dest[start] > t else start + 1

        mid = (start + end) // 2 
        if dest[mid] > t: 
            return self.search_right(dest, start, mid, t)
        else: 
            return self.search_right(dest, mid + 1, end, t)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        p = (source, destination, timestamp)
        if p in self.seen: #self.memory: 
            return False
        self.memory.append(p)
        self.seen.add(p)
        # self.metadata[destination].append(timestamp)
        d = self.metadata[destination]
        if len(d) == 0: 
            d.append(timestamp)
        else:
            idx = self.iter_search_left(d, 0, len(d) - 1, timestamp)
            d.insert(idx, timestamp)
        
        if len(self.memory) > self.limit: 
            s, dest, t = self.memory.pop(0)
            self.seen.remove((s, dest, t))
            # self.metadata[dest].pop(0)
            d = self.metadata[dest]
            idx = self.iter_search_left(d, 0, len(d) - 1, t)
            d.pop(idx)
            if not d: 
                del self.metadata[dest]
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.seen) > 0: 
            s, dest, t = self.memory.pop(0)
            # self.metadata[dest].pop(0)
            d = self.metadata[dest]
            idx = self.iter_search_left(d, 0, len(d) - 1, t)
            d.pop(idx)
            if not d: 
                del self.metadata[dest]
            self.seen.remove((s, dest, t))
            return [s, dest, t]
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.metadata: 
            return 0 
        else: 
            dest = self.metadata[destination]

        # dest = sorted(dest)
        # print(dest)
    
        sidx = self.iter_search_left(dest, 0, len(dest) - 1, startTime)
        eidx = self.iter_search_right(dest, 0, len(dest) - 1, endTime)
        # print(sidx, eidx)
        
        return eidx - sidx

import collections
class Router1_1:

    def __init__(self, memoryLimit: int):
        self.memLim = memoryLimit
        self.q = collections.deque()
        self.seen = set()
        self.destMap = collections.defaultdict(list)

    def findLeft(self, lst:  List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] < x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def findRight(self, lst: List[int], x: int) -> int:
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] <= x:
                lo = mid+1
            else:
                hi = mid
        return lo

    def insert(self, lst: List[int], x: int):
        idx = self.findLeft(lst, x)
        lst.insert(idx, x)
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
        if len(self.seen) == self.memLim:
            s0,d0,t0 = self.q.popleft()
            self.seen.remove((s0,d0,t0))
            lst0 = self.destMap[d0]
            i0 = self.findLeft(lst0,t0)
            lst0.pop(i0)
            if not lst0:
                del self.destMap[d0]
        self.q.append((source, destination, timestamp))
        self.seen.add(key)
        self.insert(self.destMap[destination], timestamp)
        return True
            
    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s,d,t))
        lst = self.destMap[d]
        i = self.findLeft(lst,t)
        lst.pop(i)
        if not lst:
            del self.destMap[d]
        return [s,d,t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.destMap:
            return 0
        lst = self.destMap[destination]
        lo = self.findLeft(lst, startTime)
        ri = self.findRight(lst, endTime)
        return ri - lo

class TreeNode: 
    def __init__(self, val, left, right, ccnt=1): 
        self.val = val 
        self.left = left 
        self.right = right 
        self.cnt = 1
        self.ccnt = ccnt

class Router2:
    """BST version (still TLE QAQ)"""
    def __init__(self, memoryLimit: int):
        self.limit = memoryLimit 
        self.memory = []
        self.metadata = {}
        
    def _add_node(self, dest, timestamp): 
        if dest in self.metadata:
            root = self.metadata[dest]
            def add(node, t): 
                if t == node.val: 
                    node.cnt += 1 
                    node.ccnt += 1
                elif t < node.val: 
                    if node.left is None: 
                        node.left = TreeNode(t, None, None)
                    else: 
                        add(node.left, t)
                        node.ccnt += 1
                else: 
                    if node.right is None: 
                        node.right = TreeNode(t, None, None)
                    else: 
                        add(node.right, t)
                        node.ccnt += 1

            add(root, timestamp)
        else: 
            self.metadata[dest] = TreeNode(timestamp, None, None)

    def _traverse(self, root): 
        s = "traverse: "
        def _traverse(root): 
            nonlocal s
            if root is not None:
                s += f"{root.val} "
                _traverse(root.left)
                _traverse(root.right)
        _traverse(root)
        print(s)
    


    def _delete_node(self, dest, timestamp): 
        if self.metadata[dest].left is None and self.metadata[dest].right is None: 
            if self.metadata[dest].cnt > 1: 
                self.metadata[dest].cnt -= 1 
                self.metadata[dest].ccnt -= 1
            else: 
                del self.metadata[dest]
        else: 
            root = self.metadata[dest]
            # print("del")
            def delete(node, t): 
                # print(dest, node.val, t)
                node.ccnt -= 1
                if node.val == t: 
                    if node.cnt > 1: 
                        node.cnt -= 1 
                    else: # find the replaced node
                        if node.left is not None: 
                            ptmp, tmp = None, node.left 
                            while tmp.right is not None: 
                                ptmp = tmp
                                tmp = tmp.right 
                                ptmp.ccnt -= 1
                            node.val, node.cnt = tmp.val, tmp.cnt
                            node.ccnt += tmp.cnt
                            if ptmp:
                                ptmp.right = tmp.left 
                            else: 
                                node.left = tmp.left
                            return node
                        elif node.right is not None: 
                            ptmp, tmp = None, node.right 
                            while tmp.left is not None: 
                                ptmp = tmp
                                tmp = tmp.left 
                                ptmp.ccnt -= 1
                            node.val, node.cnt = tmp.val, tmp.cnt
                            node.ccnt += tmp.cnt
                            if ptmp:
                                ptmp.left = tmp.right
                            else: 
                                node.right = tmp.right
                            return node
                        else: 
                            return None             
                
                elif t < node.val: 
                    node.left = delete(node.left, t)
                else: 
                    node.right = delete(node.right, t)
            
            delete(root, timestamp)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        p = [source, destination, timestamp]
        if p in self.memory: 
            return False
        self.memory.append(p)
        self._add_node(destination, timestamp)
        if len(self.memory) > self.limit: 
            _, dest, t = self.memory.pop(0)
            self._delete_node(dest, t)
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.memory) > 0: 
            _, dest, t = self.memory[0]
            self._delete_node(dest, t)
            return self.memory.pop(0)
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        def count(node, start, end): 
            if node is None: 
                return 0
            if node.val >= start and node.val <= end: 
                cnt = node.cnt
            else: cnt = 0

            if node.val > start: 
                cnt += count(node.left, start, end)
            if node.val < end: 
                cnt += count(node.right, start, end)
            
            return cnt
        
        def count1(node, val): 
            if node is None: 
                return 0
            ret = 0
            if node.val < val: 
                if node.left:
                    ret = node.left.ccnt 
                return ret + count1(node.right, val) + node.cnt
            elif node.val > val: 
                return count1(node.left, val)
            else: 
                if node.left:
                    ret = node.left.ccnt 
                return ret + node.cnt


        if destination not in self.metadata: 
            return 0
        root = self.metadata[destination]
        # cnt = count(root, startTime, endTime)
        cnt = count1(root, endTime) - count1(root, startTime - 1)
        return cnt

class Solution: 
    def func(): 
        return  
    
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ret = 0
        while True: 
            if all([nums[i] <= nums[i + 1] for i in range(len(nums) - 1)]): 
                break
            tmp = nums[0] + nums[1]
            idx = 0
            for i in range(len(nums) - 1): 
                if nums[i] + nums[i + 1] < tmp: 
                    tmp = nums[i] + nums[i + 1] 
                    idx = i 
            nums = nums[: idx] + [nums[idx] + nums[idx + 1]] + nums[idx + 2:]
            ret += 1
        return ret

if __name__ == "__main__": 
    # nums = [2,2,-1,3,-2,2,1,1,1,0,-1]
    # test_case = (nums, )
    # ret = Solution().minimumPairRemoval(*test_case)

    funcl = ["Router", "addPacket", "addPacket", "addPacket", "addPacket", "addPacket", "forwardPacket", "addPacket", "getCount"]
    argsl = [[3], [1, 4, 90], [2, 5, 90], [1, 4, 90], [3, 5, 95], [4, 5, 105], [], [5, 2, 110], [5, 100, 110]]
    
    funcl = ["Router", "addPacket", "forwardPacket", "forwardPacket"]
    argsl = [[2], [7, 4, 90], [], []]

    funcl = ["Router","addPacket","forwardPacket","getCount"] 
    argsl = [[2],[2,5,1],[],[5,1,1]]
    
    funcl = ["Router","addPacket","getCount","getCount","addPacket","addPacket","addPacket","addPacket"]
    argsl = [[3],[3,5,1],[5,1,1],[5,1,1],[2,5,4],[2,4,9],[1,2,9],[1,3,9]]
    
    funcl = ["Router","addPacket","addPacket","addPacket","getCount"] 
    argsl = [[2],[3,1,3],[1,2,3],[4,5,3],[1,2,3]]

    ret = []
    start_time = time.time()
    for f, args in zip(funcl, argsl): 
        if f == "Router": 
            obj = Router1(*args)
            ret.append(None)
        else: 
            ret.append(getattr(obj, f)(*args))

    print(ret)
    print("duration: ", time.time() - start_time)