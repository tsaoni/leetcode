from typing import List

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        dist = [abs(nums[i] - nums[(i + 1) % len(nums)]) for i in range(len(nums))]
        return max(dist)
    
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        dists = [abs(a - b) for a, b in zip(arr, brr)]
        ans1 = sum(dists)
        arr.sort()
        brr.sort()
        dists = [abs(a - b) for a, b in zip(arr, brr)]
        ans2 = sum(dists) + k
        return min(ans1, ans2)

    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        special_path_lst = [[[0], {nums[0]}, 0]] # (path, number, length)
        cur_lst = [0]
        while True: 
            if all([e == None for e in edges]): 
                break
            # get edge 
            next_cur_lst = []
            cur_edge_lst = []
            for i, e in enumerate(edges): 
                if e is not None:
                    add_edge = None
                    for c in cur_lst:
                        if c == e[0]: 
                            next_cur_lst += [e[1]]
                            cur_edge_lst += [[c, e[1], e[2]]]
                            edges[i] = None
                        elif c == e[1]: 
                            next_cur_lst += [e[0]]
                            cur_edge_lst += [[c, e[0], e[2]]]
                            edges[i] = None
                        break

            # next_cur_lst = list(set(next_cur_lst))
            # cur_edge_lst = list(set(cur_edge_lst))
            
            # extend from old 
            for p in special_path_lst: 
                for e in cur_edge_lst:
                    if p[0][-1] == e[0] and nums[e[1]] not in p[1]: 
                        p[0] += [e[1]]
                        p[1] |= {nums[e[1]]}
                        p[2] += e[2]
            # add new
            tmp = []
            for e in cur_edge_lst: 
                if not nums[e[0]] == nums[e[1]]:
                    tmp += [[e[:2], {nums[e[0]], nums[e[1]]}, e[2]]]
                    # import pdb 
                    # pdb.set_trace()
            special_path_lst += tmp
            
            cur_lst = next_cur_lst
        # return [#len, #numnode]
        max_len = 0
        min_node = 1
        # print(special_path_lst)
        for p in special_path_lst:
            if p[2] >= max_len: 
                max_len = p[2]
                if min_node > 1:
                    min_node = min(min_node, len(p[0]))
                else:
                    min_node = len(p[0])
        return [max_len, min_node]

    def distanceSum(self, m: int, n: int, k: int) -> int:
        def dist(pos): 
            return 
        total_len = m * n 
        pos = [i for i in range(k)]
        total_dist = 0
        while True: 
            # terminate
            # total_len - 1, ..., total_len - k
            tmp = [pos[i] == total_len - 1 - i for i in range(k)]
            if all(tmp): 
                break
            # calculate 
            for start in pos[: -1]: 
                for end in pos[0: ]: 
                    x1, y1 = int(start / m), start % m
                    x2, y2 = int(end / m), end % m
                    total_dist += abs(x1 - x2) + abs(y1 - y2)
            
            # check reset
            back = False
            for i in range(k - 1, -1): 
                if pos[i] == total_len - 1 - i: 
                    back = True 
                    continue 
                else: 
                    import pdb 
                    pdb.set_trace()

            # inc 
            
        return 

if __name__ == "__main__": 
    nums = [1,2,4]
    # test_case = (nums, )
    # ret = Solution().maxAdjacentDistance(*test_case)

    arr = [-7,9,5]
    brr = [7,-2,-5]
    k = 2
    # test_case = (arr, brr, k)
    # ret = Solution().minCost(*test_case)

    # edges = [[0,1,2],[1,2,3],[1,3,5],[1,4,4],[2,5,6]]
    # nums = [2,1,2,1,3,1]
    edges = [[1,0,8]]
    nums = [2,2]
    # test_case = (edges, nums)
    # ret = Solution().longestSpecialPath(*test_case)

    test_case = (edges, nums)
    ret = Solution().longestSpecialPath(*test_case)
    print(ret)