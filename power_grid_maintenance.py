from typing import List
import heapq

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ret = []
        parents = [-1] * c
        conn = [[i] for i in range(c)] 
        rem = [False] * c
        def merge(l1, l2): 
            i, j = 0, 0
            tmp = [] 
            while i < len(l1) and j < len(l2): 
                if l1[i] < l2[j]: 
                    tmp.append(l1[i])
                    i += 1 
                else: 
                    tmp.append(l2[j])
                    j += 1 
            while i < len(l1): 
                tmp.append(l1[i])
                i += 1
            while j < len(l2): 
                tmp.append(l2[j])
                j += 1
            return tmp 
        
        def find(x): 
            return x if parents[x] < 0 else find(parents[x])
        
        def collapse(p, n): 
            while n >= 0: 
                _p = parents[n]
                parents[n] = p
                n = _p

        def join(n1, n2): 
            p1, p2 = find(n1), find(n2)
            if p1 != p2: 
                if p1 > p2: 
                    p1, p2 = p2, p1 
                    n1, n2 = n2, n1
                # parents[p2] = p1
                collapse(p1, n2)
                # conn[p1] = merge(conn[p1], conn[p2])
                conn[p1] += conn[p2]
                # heapq.heapify(conn[p1])
                conn[p2] = []
            

        for n1, n2 in connections: 
            join(n1 - 1, n2 - 1)

        for s in conn: 
            heapq.heapify(s)
        # print(conn, parents)
        def check(id): 
            p = find(id)
            
            if len(conn[p]) > 0: 
                # if search(id, conn[p]) >= 0:
                if rem[id]:
                    while len(conn[p]) > 0 and rem[conn[p][0]]: 
                        # conn[p].pop(0)
                        heapq.heappop(conn[p])
                    return conn[p][0] + 1 if len(conn[p]) > 0 else -1
                else:
                    return id + 1
               
            else: 
                # print(p, conn)
                return -1
        
        def search(id, lst): 
            if len(lst) == 0: 
                return -1
            l, r = 0, len(lst) - 1 
            while l < r: 
                mid = (l + r) // 2 
                if lst[mid] < id: 
                    l = mid + 1 
                else: 
                    r = mid 
            return l if lst[l] == id else -1
        def offline(id): 
            rem[id] = True
            # p = find(id)
            # ridx = search(id, conn[p])
            # if ridx >= 0:
            #     conn[p].pop(ridx)

        for op, id in queries: 
            # print(conn)
            if op == 1: 
                ret.append(check(id - 1))
            else: 
                offline(id - 1)
        return ret
    
if __name__ == "__main__": 
    c = 5
    connections = [[1,2],[2,3],[3,4],[4,5]]
    queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

    c = 3
    connections = []
    queries = [[1,1],[2,1],[1,1]]

    ret = Solution().processQueries(c, connections, queries)
    print(ret)