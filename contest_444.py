from typing import List
import math

from collections import defaultdict, Counter


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


class TreeNode: 
    def __init__(self, val, left, right): 
        self.val = val 
        self.left = left 
        self.right = right 
        self.cnt = 1

class Router1:

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
                elif t < node.val: 
                    if node.left is None: 
                        node.left = TreeNode(t, None, None)
                    else: 
                        add(node.left, t)
                else: 
                    if node.right is None: 
                        node.right = TreeNode(t, None, None)
                    else: 
                        add(node.right, t)

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
            else: 
                del self.metadata[dest]
        else: 
            root = self.metadata[dest]
            # print("del")
            def delete(node, t): 
                # print(dest, node.val, t)
                if node.val == t: 
                    if node.cnt > 1: 
                        node.cnt -= 1 
                    else: # find the replaced node
                        if node.left is not None: 
                            ptmp, tmp = None, node.left 
                            while tmp.right is not None: 
                                ptmp = tmp
                                tmp = tmp.right 
                            node.val, node.cnt = tmp.val, tmp.cnt
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
                            node.val, node.cnt = tmp.val, tmp.cnt
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
        
        if destination not in self.metadata: 
            return 0
        root = self.metadata[destination]
        cnt = count(root, startTime, endTime)
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
    ret = []
    for f, args in zip(funcl, argsl): 
        if f == "Router": 
            obj = Router1(*args)
            ret.append(None)
        else: 
            ret.append(getattr(obj, f)(*args))

    print(ret)