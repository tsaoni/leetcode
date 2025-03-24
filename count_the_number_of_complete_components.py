from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        G = [[] for _ in range(n)]
        for v1, v2 in edges: 
            G[v1] += [v2] 
            G[v2] += [v1]

        set_idx = 0
        sets = [-1] * n
        set_cnt = {}
        def dfs(v, depth): 
            # is_leaf = True
            sets[v] = set_idx
            N = 1
            for v2 in G[v]: 
                if sets[v2] < 0: 
                    # is_leaf = False
                    N += dfs(v2, depth + 1)
            
            return N
            # if not is_leaf: 
            #     depth = N
            
            # if depth < 0: 
            #     return -1 
            # else:
            #     if len(G[v]) == depth - 1: 
            #         return depth 
            #     else: 
            #         return -1 

        for i in range(n): 
            if sets[i] < 0: 
                N = dfs(i, 1)
                set_cnt[set_idx] = N
                # if tmp > 0: 
                #     ret += 1
                set_idx += 1
        # print(set_idx)
        set_valid = {i: True for i in range(set_idx)}
        for i in range(n): 
            idx = sets[i]
            if len(G[i]) == set_cnt[idx] - 1: 
                set_valid[idx] &= True
            else: 
                set_valid[idx] &= False
        # print(set_valid)
        return sum([v for k, v in set_valid.items()])
    
if __name__ == "__main__": 
    n = 6
    edges = [[0,1],[0,2],[1,2],[3,4]]

    # n = 6
    # edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]

    # n = 5
    # edges = [[1,0],[2,0],[3,1],[3,2],[4,0],[4,1],[4,3]]

    # n = 3 
    # edges = [[2,0],[2,1]]

    test_case = (n, edges)
    ret = Solution().countCompleteComponents(*test_case)
    print(ret)