from typing import List
import numpy as np

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n_vertex = len(set([k for k, _ in edges] + [k for _, k in edges]))
        record = [[] for _ in range(n_vertex)]
        source_lst = [[] for _ in range(n_vertex)]
        ret = None
        cnt = 0
        for start, end in edges: 
            # if len(record[end - 1]) == 0: # root 
            #     record[end - 1] += [start - 1]
            # else: 
            if True:
                # record[end - 1] += [start - 1]
                # detect the parent of start/end
                def get_parent(record, cur_lst, source_lst=source_lst): 
                    # ret = []
                    # while len(cur_lst) > 0: 
                    #     p = cur_lst.pop(0)
                    #     cur_lst += record[p]
                    #     if len(record[p]) == 0: # root 
                    #         ret += [p]
                    #     # print(record)
                    
                    ret = []
                    for p in cur_lst: 
                        if len(source_lst[p]) == 0: 
                            ret += [p]
                        else:
                            ret += source_lst[p]
                    ret = list(set(ret))

                    return ret

                p_start_lst = [start - 1]
                p_end_lst = [end - 1]
                p_start_lst = get_parent(record, p_start_lst)
                p_end_lst = get_parent(record, p_end_lst)
                # check if overlap (parent)
                # start_bin_lst = [False] * n_vertex 
                # end_bin_lst = [False] * n_vertex
                # for idx in p_start_lst: 
                #     start_bin_lst[idx] = True 
                # for idx in p_end_lst: 
                #     end_bin_lst[idx] = True
                
                # n_parent_overlap = sum(np.array(start_bin_lst) & np.array(end_bin_lst))
                n_parent_overlap = len(set(p_start_lst) & set(p_end_lst))
                # check if overlap (children)
                n_child_overlap = 0
                for i, p in enumerate(record): 
                    # parent_bin_lst = [False] * n_vertex 
                    sources = []
                    for x in p: 
                        # print(cnt)
                        # cnt += 1
                        sources += get_parent(record, [x])
                    # for x in sources:
                    #     parent_bin_lst[x] = True
                    # pair_bin_lst = [False] * n_vertex
                    # pair_bin_lst[start - 1] = True 
                    # pair_bin_lst[end - 1] = True 
                    # if sum(np.array(parent_bin_lst) & np.array(pair_bin_lst)) == 2: # overlap
                    if len(set(sources) & set([start - 1, end - 1])) == 2:
                        n_child_overlap = 1
                        child = i + 1
                        break
                
                if n_parent_overlap > 0 or n_child_overlap > 0: # detect cycle
                    ret = [start, end]
                else: # add edge
                    def add_source(source_lst, src, tgt): 
                        # print("start")
                        # add sources of src to tgt
                        src_p_lst = []
                        if len(record[src]) == 0: # root 
                            src_p_lst = [src]
                        else: 
                            src_p_lst = [x for x in source_lst[src]]
                        # source_lst[tgt] += src_p_lst
                        # ones share the same sources should also updated
                        for i, p in enumerate(source_lst): 
                            is_sub = False
                            if tgt in p: 
                                p.remove(tgt)
                                is_sub = True 
                            elif len(source_lst[tgt]) and set(p) == set(source_lst[tgt]):
                                is_sub = True 
                            elif i == tgt: 
                                is_sub = True
                            if is_sub: 
                                source_lst[i] += src_p_lst
                        # print(source_lst)
                        # print("exit")
                        return 

                    record[end - 1] += [start - 1] 
                    add_source(source_lst, start - 1, end - 1)
                # while True: 
                #     tmp = []
                #     for p in p_start_lst:
                #         record[p]
                #         p_start = record[p_start]
                # p_end = end - 1 
                # while record[p_end] != -1: 
                #     p_end = record[p_end]
                    
                # if p_start == p_end
        n_root = len([len(x) for x in record if len(x) == 0])
        if n_root > 1: # multiple root 
            start, end = ret 
            record[end - 1] += [start - 1]
            add_source(source_lst, start - 1, end - 1)
            edges.reverse()
            for src, tgt in edges: 
                src_source = set(source_lst[src - 1]) if len(source_lst[src - 1])> 0 else set([src - 1])
                if len(set(record[tgt - 1])) > 1 and src_source == set(source_lst[tgt - 1]): 
                    ret = [src, tgt]
                    break

            # tmp = end - 1
            # while len(record[tmp]) == 1: 
            #     tmp = record[tmp][0]
            # for p in record[tmp]: 
            #     if len(record[p]) == 1: 
            #         ret = [p + 1, tmp + 1]
            #         # acyclic = False
            #         break
            # if n_child_overlap > 0: 
            #     edges.reverse()
            #     for e in edges: 
            #         if child in e:
            #             ret = e
            #             break
            print(source_lst)
            print(record)
        return ret
    
if __name__ == "__main__": 
    test_case = [[3,4],[4,1],[1,2],[2,3],[5,1]]
    # [[5,2],[5,1],[3,1],[3,4],[3,5]]
    # [[2,1],[3,1],[4,2],[1,4]]
    # [[7,2],[10,1],[2,3],[3,5],[10,6],[4,6],[10,9],[2,4],[7,10],[3,8]]
    # [[4,2],[1,5],[5,2],[4,3],[4,1]]
    ret = Solution().findRedundantDirectedConnection(test_case)
    print(ret)