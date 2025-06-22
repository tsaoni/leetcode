from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        # roots = {i for i in range(N)}
        # nonroots = set()
        # for nodes in graph: 
        #     nonroots = nonroots.union(nodes)
        # roots = roots - nonroots
        
        def insert(li, num): 
            l, r = 0, len(li)
            while l < r: 
                mid = (l + r) // 2 
                if li[mid] > num: 
                    r = mid  
                else: 
                    l = mid + 1
            if l > 0 and li[l - 1] == num:
                return
            li.insert(l, num)
        
        def dfs(node): 
            visited[node] = -vid 
            is_safe = True
            
            for child in graph[node]: 
                if visited[child] == -vid: 
                    is_safe = False
                elif visited[child] > 0: 
                    is_safe &= is_safe_lst[child]
                else:
                    is_safe &= dfs(child)
            # if node == 3:
            #     import pdb 
            #     pdb.set_trace()
            # if is_safe: 
            #     insert(safe_nodes, node)
            is_safe_lst[node] = is_safe
            visited[node] = vid
            return is_safe
        
        safe_nodes = []
        vid = 1
        visited = [0] * N
        is_safe_lst = [True] * N
        for r in range(N): 
            if visited[r] == 0:
                dfs(r)
            vid += 1
            if is_safe_lst[r]: 
                safe_nodes.append(r)
        return safe_nodes
    
if __name__ == "__main__": 
    graph = [[1,2],[2,3],[5],[0],[5],[],[]]
    graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
    graph = [[],[0,2,3,4],[3],[4],[]]
    ret = Solution().eventualSafeNodes(graph)
    print(ret)