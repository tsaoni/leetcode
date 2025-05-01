from typing import List
class Solution:
    def maxTaskAssign2(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        use binary search: assign k weakest tasks to k strongest workers
        Complexity: O(n * logn)
        """
        import bisect
        tasks.sort()
        workers.sort()
        left, right = 0, min(len(tasks), len(workers))
        def check(k): 
            p = pills
            avail = workers[-k: ]
            # print(k)
            for t in reversed(tasks[: k]): 
                # print(avail_idxs)
                if avail[-1] >= t: 
                    avail.pop(-1)
                else: 
                    if p > 0: 
                        idx = bisect.bisect_left(avail, t - strength)
                        if idx == len(avail): 
                            return False 
                        else:
                            avail.pop(idx)
                            p -= 1
                    else: 
                        return False
            
            return True
        
        while left < right: 
            mid = (left + right + 1) // 2 
            if check(mid): 
                left = mid 
            else: 
                right = mid - 1
        return left
    
    def maxTaskAssign1(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        a wrong implementation 
        """
        tasks.sort()
        workers.sort()
        stack = []
        wi, ti = 0, 0
        print(len(tasks), len(workers))
        while wi < len(workers): 
            if ti < len(tasks):
                while len(stack) > 0 and stack[0] < tasks[ti]: 
                    stack.pop(0)
                
                if workers[wi] < tasks[ti]: 
                    stack.append(workers[wi] + strength)
                    wi += 1 
                else:
                    if pills > 0 and len(stack) > 0 and stack[0] < workers[wi]:
                        pills -= 1 
                        stack.pop(0)
                    else: 
                        wi += 1
                    ti += 1
            else: 
                break 
        # print(stack)
        print(ti, pills)
        while pills > 0 and len(stack) > 0 and ti < len(tasks): 
            if stack[0] >= tasks[ti]: 
                ti += 1
                pills -= 1 
            stack.pop(0)
        return ti 

    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        wi = 0
        ret = 0
        used = [0] * len(workers)
        occupy = [0] * len(tasks)
        for ti, t in enumerate(tasks): 
            while wi < len(workers) and workers[wi] < t: 
                wi += 1
            if wi < len(workers):
                used[wi] = 1
                occupy[ti] = 1
                wi += 1 
                ret += 1
            else: 
                break            
        print(used, occupy)
        wi = 0
        for ti, t in enumerate(tasks): 
            if occupy[ti]: 
                continue
            while wi < len(workers) and (used[wi] or (pills > 0 and workers[wi] < t - strength)): 
                wi += 1
            if pills > 0 and wi < len(workers):
                pills -= 1 
                wi += 1 
                ret += 1
                print(wi - 1)
            else: 
                break  

        return ret

if __name__ == "__main__": 
    tasks = [3,2,1]
    workers = [0,3,3]
    pills = 1
    strength = 1
    # tasks = [5,4]
    # workers = [0,0,0]
    # pills = 1
    # strength = 5
    # tasks = [10,15,30]
    # workers = [0,10,10,10,10]
    # pills = 3
    # strength = 10
    tasks = [5,9,8,5,9]
    workers = [1,6,4,2,6]
    pills = 1 
    strength = 5
    
    test_case = (tasks, workers, pills, strength)
    ret = Solution().maxTaskAssign2(*test_case)
    print(ret)