from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        T = {}
        for i, path in enumerate(paths): 
            cur = T
            for dir in path: 
                if dir not in cur: 
                    cur[dir] = {}
                cur = cur[dir]
            cur[""] = i
        uniq_paths = defaultdict(set)
        uniq_leaf_paths = defaultdict(set)
        def dfs(cname, cur): 
            rep = ""
            to_store = -1 
            for child in sorted(cur): 
                if child:
                    tmp = dfs(child, cur[child])
                    rep += f"{child}({tmp})"
                else: 
                    to_store = cur[child] 
            if len(cur) == 1 and "" in cur: 
                if f"{cname}()" in uniq_leaf_paths: 
                    uniq_leaf_paths[f"{cname}()"] = set() 
                else:
                    uniq_leaf_paths[f"{cname}()"].add(to_store)
            else:
                if to_store >= 0: 
                    if rep in uniq_paths: 
                        uniq_paths[rep] = set() 
                        rep.split("()")
                    else: 
                        uniq_paths[rep].add(to_store)
                    # if rep == "": 
                    #     if f"{cname}()" in uniq_paths: 
                    #         uniq_paths[f"{cname}()"] = -1 
                    #     else: 

                    # if rep in uniq_paths: 
                    #     uniq_paths[rep] = -1 
                    # else:
                    #     uniq_paths[f"{cname}({rep})"] = to_store
            return rep
        dfs("", T)
        # print(uniq_paths)
        # print(uniq_leaf_paths)
        return [paths[i] for _, s in uniq_paths.items() for i in s] + [paths[i] for _, s in uniq_leaf_paths.items() for i in s]
    
if __name__ == "__main__": 
    paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    # paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
    # paths = [["a","b"],["c","d"],["c"],["a"]]
    # paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]
    ret = Solution().deleteDuplicateFolder(paths)
    print(ret)