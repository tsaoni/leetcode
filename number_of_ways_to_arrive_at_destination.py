from typing import List 
from collections import defaultdict

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        """
        may be very slow... :')
        """
        G = defaultdict(list)
        for u, v, t in roads: 
            G[u] += [[v, t]]
            G[v] += [[u, t]]
        
        min_time_lst = [0] + [float("inf")] * (n - 1)
        n_way_lst = [{-1: 1}] + [{} for _ in range(n - 1)] 
        # print(min_time_lst)
        # print(n_way_lst)
        for _ in range(n - 1): 
            tmp_min_time_lst = [0]
            tmp_n_way_lst = [{-1: 1}]
            for i in range(1, n): 
                min_time = min_time_lst[i]
                n_way = {} #deepcopy(n_way_lst[i])
                for s, t in G[i]:
                    # print(n_way_lst[s])
                    if len(n_way_lst[s]) > 0: 
                        if min_time_lst[s] + t < min_time: 
                            n_way_cnt = sum([x for _, x in n_way_lst[s].items()])
                            # print(n_way_lst)
                            # print(n_way_cnt)
                            n_way = {s: n_way_cnt}
                            min_time = min_time_lst[s] + t
                        elif min_time_lst[s] + t == min_time: 
                            n_way_cnt = sum([x for _, x in n_way_lst[s].items()])
                            n_way[s] = n_way_cnt

                tmp_min_time_lst += [min_time]
                tmp_n_way_lst += [n_way]

            min_time_lst = tmp_min_time_lst
            n_way_lst = tmp_n_way_lst
            # print(tmp_min_time_lst)
            # print(tmp_n_way_lst)
            # print()

        # print(min_time_lst)
        print(n_way_lst[-1])
        
        n_way_cnt = sum([x for _, x in n_way_lst[-1].items()])
        modulo = 10 ** 9 + 7
        return n_way_cnt % modulo
    
if __name__ == "__main__": 
    n = 7
    roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
    
    # n = 2
    # roads = [[1,0,10]]
    test_case = (n, roads)
    ret = Solution().countPaths(*test_case)
    print(ret)