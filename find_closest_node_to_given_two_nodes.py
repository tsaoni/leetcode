from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        N = len(edges)
        flag = [0] * N
        d = 0
        pnt1, pnt2 = node1, node2 
        while True: 
            cands = set()
            if pnt1 < 0 and pnt2 < 0: 
                return -1
            if pnt1 >= 0:
                if flag[pnt1] == 0: 
                    flag[pnt1] = 1
                    pnt1 = edges[pnt1]
                elif flag[pnt1] == 1: 
                    pnt1 = -1 
                else: 
                    cands.add(pnt1)
                
            if pnt2 >= 0:
                if flag[pnt2] == 0: 
                    flag[pnt2] = 2
                    pnt2 = edges[pnt2]
                elif flag[pnt2] == 2: 
                    pnt2 = -1 
                else: 
                    cands.add(pnt2)

            if len(cands) > 0: 
                return min(cands)
            

        
if __name__ == "__main__": 
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1

    edges = [1,2,-1]
    node1 = 0
    node2 = 2

    edges = [4,4,8,-1,9,8,4,4,1,1]
    node1 = 5
    node2 = 6
    ret = Solution().closestMeetingNode(edges, node1, node2)
    print(ret)