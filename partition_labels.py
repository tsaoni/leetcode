from typing import List
from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parent = {}
        def find_parent(x):
            return x if parent[x] == "" else find_parent(parent[x])
        
        def joint_set(x1, x2): 
            p1 = find_parent(x1)
            p2 = find_parent(x2)
            if p1 != p2: 
                parent[p2] = p1
            return 
        
        cnt = Counter()
        root = []
        cuts = []
        for sidx, c in enumerate(s): 
            cnt[c] += 1 
            if cnt[c] == 1: 
                root.append(c)
                parent[c] = ""
                cuts.append((sidx, sidx))
            else: 
                # print(sidx, c)
                # print(root)
                r = find_parent(c)
                while root[-1] != r: 
                    sr = root.pop(-1)
                    joint_set(r, sr)
                    cuts.pop(-1)
                    # joint_set(c, node)
                cuts[-1] = (cuts[-1][0], sidx)
        
        print(parent)
        ret = []
        for s, e in cuts: 
            ret.append(e - s + 1)
        return ret
    
if __name__ == "__main__": 
    s = "ababcbacadefegdehijhklij" 
    s = "eccbbbbdec"
    test_case = (s, )
    ret = Solution().partitionLabels(*test_case)
    print(ret)