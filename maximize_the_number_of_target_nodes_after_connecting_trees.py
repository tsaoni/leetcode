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
    
    def maxTargetNodes_2(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
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
        colors1 = [0] * n
        visited1 = [0] * n
        colors2 = [0] * m
        visited2 = [0] * m
        def dfs(u, colors, visited, T): 
            for v in T[u]: 
                if not visited[v]: 
                    visited[v] = True 
                    colors[v] = colors[u] ^ 1 
                    dfs(v, colors, visited, T)
        dfs(0, colors1, visited1, T1)
        dfs(0, colors2, visited2, T2)
        n0, n1 = n - sum(colors1), sum(colors1)
        n2 = max(m - sum(colors2), sum(colors2))
        # print(T2)
        # print(colors2)
        # print(n0, n1, n2)
        return [n0 + n2 if colors1[i] == 0 else n1 + n2 for i in range(n)]

if __name__ == "__main__": 
    edges1 = [[0,1],[0,2],[2,3],[2,4]]
    edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
    edges1 = [[0,1],[0,2],[0,3],[0,4]]
    edges2 = [[0,1],[1,2],[2,3]]
    
    ret = Solution().maxTargetNodes_2(edges1, edges2)
    print(ret)