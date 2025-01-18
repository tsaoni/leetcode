from typing import List
from itertools import chain
import numpy as np

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        """
        three cases to form a circular:
        1. two points shared a same ancestor link with each other
        2. a point link to its ancestor
        3. two points shared a same decendant 
        """
        n_vertex = len(set(list(chain(*edges))))
        # root_lst = []
        ancestor_lst = [set() for _ in range(n_vertex)]
        ret = None
        # build 
        for start, end in edges: 
            # detect cycle 
            if len(ancestor_lst[start - 1] & ancestor_lst[end - 1]) > 0: 
                return [start, end]
            elif len(ancestor_lst[start - 1] & {end - 1}) > 0: 
                ret = [start, end]
                continue
            else:
                # print(ancestor_lst)
                for i, x in enumerate(ancestor_lst): 
                    # print(start, " ", end)
                    # print(x)
                    if len(set([start - 1, end - 1]) & x) == 2: 
                        for j in range(len(edges) - 1, -1, -1): 
                            if edges[j][1] == i + 1: 
                                return edges[j]

            # add ancestor
            ancestor_lst[end - 1] = ancestor_lst[start - 1] | ancestor_lst[end - 1]
            ancestor_lst[end - 1] = ancestor_lst[end - 1] | {start - 1}
            ancestor_lst[end - 1] = ancestor_lst[end - 1] | ancestor_lst[start - 1]
            # add ancestor to decendents
            for i, x in enumerate(ancestor_lst): 
                if end - 1 in x: 
                    ancestor_lst[i] |= {start - 1}
                    ancestor_lst[i] |= ancestor_lst[start - 1]
            
        
        print(ancestor_lst)
        if len(list(filter(lambda x: len(x) == 0, ancestor_lst))) > 1: 
            start, end = ret
            ancestor_lst[end - 1] = ancestor_lst[start - 1] | ancestor_lst[end - 1]
            ancestor_lst[end - 1] |= {start - 1}
            tmp = ancestor_lst[end - 1]

            for start, end in edges: 
                print({start - 1, end - 1} - tmp)
                if len({start - 1, end - 1} - tmp) == 0 and \
                    len(ancestor_lst[end - 1] - ancestor_lst[start - 1] - set([start - 1])) > 0: 
                        
                        return [start, end]

        return ret


if __name__ == "__main__": 
    test_case = [[4,2],[1,5],[5,2],[5,3],[2,4]]
    # [[4,2],[1,5],[5,2],[4,3],[4,1]]
    # [[3,4],[4,1],[1,2],[2,3],[5,1]]
    # [[5,2],[5,1],[3,1],[3,4],[3,5]]
    # [[2,1],[3,1],[4,2],[1,4]]
    # [[7,2],[10,1],[2,3],[3,5],[10,6],[4,6],[10,9],[2,4],[7,10],[3,8]]
    # [[4,2],[1,5],[5,2],[4,3],[4,1]]
    ret = Solution().findRedundantDirectedConnection(test_case)
    print(ret)