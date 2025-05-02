from typing import List
class Solution:
    def maxTaskAssign3(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        still a wrong implementation :')
        """
        tasks.sort()
        workers.sort()
        def find(l, v): 
            left, right = 0, len(l) - 1 
            
            while left < right: 
                mid = (left + right + 1) // 2 
                if v >= l[mid]: 
                    left = mid 
                else: 
                    right = mid - 1
            if l[left] > v: 
                return -1
            return left 
        
        
        import bisect
        avail = tasks
        ret = 0
        redundants = []
        for w in workers: 
            if len(avail) == 0: 
                return ret
            else:
                idx = find(avail, w)
                if idx < 0: 
                    redundants.append(w)
                else: 
                    ret += 1
                    avail.pop(idx)
    
        for w in redundants: 
            if pills > 0 and len(avail) > 0:
                idx = find(avail, w + strength)
                if idx >= 0: 
                    avail.pop(idx)
                    pills -= 1 
                    ret += 1 
            else: 
                break
       
        return ret

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
        """
        still a wrong implementation
        """
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
    tasks = [5,4]
    workers = [0,0,0]
    pills = 1
    strength = 5
    tasks = [10,15,30]
    workers = [0,10,10,10,10]
    pills = 3
    strength = 10
    tasks = [5,9,8,5,9]
    workers = [1,6,4,2,6]
    pills = 1 
    strength = 5
    tasks = [9,31,95,46] 
    workers = [5,53,17,77,45,48,53] 
    pills = 4 
    strength = 86
    tasks = [1943,2068,4077,7832,8061,6939,6263,8917,8008,5348,8837,4753,4607,7638,9000,7222,4552,1123,9225,6896,4154,6303,3186,2325,9994,5855,8851,7377,1930,1187,5094,2689,8852,1507,1567,9575,1193,1557,8840,9075,5032,3642,6917,7968,5310,2315,7516,4776,3091,7027,1788,2007,2651,6112,4264,5644,3585,9408,7410,9605,8151,1538,6905,6759,4518,3444,5036,1589,3902,3037,1468,9179,3000,5339,6805,7394,9418,9262,2888,4708,3402,5554,8714,7393,2848,5946,9808,4301,6675,8564,6300,4359,9506,1946,9673,7412,1164,2986,2198,5144,3763,4782,8835,6994,8035,3332,2342,5243,3150,9084,6519,9798,7682,9919,7473,7686,9978,8092,9897,3985,9874,5842,9740,2145,2426,7069,8963,9250,4142,9434,1895,6559,3233,8431,6278,6748,7305,4359,2144,8009,4890,6486,7464,8645,1704,5915,9586,1394,7504,2124,3150,2051,5026,7612,3715,5757,4355,6394,3202,2777,3949,2349,7398,3029,3081,5116,5078,8048,9934,4348,8518,5201,1203,7935,5006,6388,8680,3427,6048,1957,4026,4618,4080] 
    workers = [875,2347,939,3664,3926,4555,1947,4406,4601,3502,4964,1307,4232,2968,4572,3139,2788,1847,1208,2019,4184,1664,1747,3690,4333,891,686,1959,2218,4972,806,741,1490,4529,2909,925,2040,1234,1264,1135,3640,1455,2933,3699,2856,3074,4579,2458,2090,833,4140,4534,2336,4363,1948,4546,4155,3735,3577,2780,4874,1747,4844,3482,3053,3534,549,4500,2237,2128,1554,3210,4161,2211,950,3732,2182,1148,4368,4050,1452,1015,3192,4318,3908,2590,1103,2811,2821,690,2718,3360,2659,3315,579,3108,2979,3903,4367,1906,4964,889,4803,825,2270,4794,4825,4485,4461,1639,3857,1330,3169,2425,3694,1980,2268,3002,2177,3225,2499,2517,1916,2844,760,2167,1786,3179,3222,1432,3775,4747,1764,690,3223,4684,890,2701,1045,3034,1381,1011,2150,4798,2247,1334,3058,934,2895,1484,2784,3341,4412,1748,625,2610,3488,4810,669,4275,4929,1014,2104,3111] 
    pills = 122 
    strength = 3131
    
    test_case = (tasks, workers, pills, strength)
    ret = Solution().maxTaskAssign3(*test_case)
    print(ret)