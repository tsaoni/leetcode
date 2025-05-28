from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = max([max(e) for e in edges1]) + 1
        m = max([max(e) for e in edges2]) + 1
        T1 = [[] for _ in range(n)]
        T2 = [[] for _ in range(m)]
        for u, v in edges1: 
            T1[u].append(v)
            T1[v].append(u)
        for u, v in edges2: 
            T2[u].append(v)
            T2[v].append(u)
        def get_kpath_node_num(T, root, k): 
            visited = [False] * len(T)
            s = [root]
            cnt = 1
            visited[root] = True
            for i in range(k): 
                ns = []
                for node in s: 
                    for child in T[node]: 
                        if not visited[child]:
                            cnt += 1 
                            visited[child] = True
                            ns.append(child)
                s = ns
            return cnt
        
        path_num = []
        second_path_num = []
        max_second_path_num = 0
        if k > 0:
            for i in range(m): 
                second_path_num.append(get_kpath_node_num(T2, i, k - 1)) 
            max_second_path_num = max(second_path_num)
        for i in range(n): 
            path_num.append(get_kpath_node_num(T1, i, k) + max_second_path_num)
        
        
        return path_num
    
if __name__ == "__main__": 
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    k = 2
    edges1 = [[0,1],[0,2],[0,3],[0,4]]
    edges2 = [[0,1],[1,2],[2,3]]
    k = 1
    ret = Solution().maxTargetNodes(edges1, edges2, k)
    print(ret)