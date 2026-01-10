from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def build(self, lst): 
        q = []
        root = None
        p = None
        for v in lst: 
            if v is not None: 
                node = TreeNode(v, None, None)
            else: 
                node = None 
            if len(q) == 0: 
                root = node 
            else: 
                if p is None: 
                    while q[0] is None: 
                        q.pop(0)
                    p = q.pop(0)
                    p.left = node 
                else: 
                    p.right = node 
                    p = None 
            q.append(node)
        return root
    
    def traverse(self, node): 
        print(node.val if node is not None else None)
        if node is None: 
            return 
        self.traverse(node.left)
        self.traverse(node.right)
        

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        import math 
        MAXN = 10 ** 4 
        # 2 ** x - 1 <= MAXN 
        MAXL = MAXN #math.floor(math.log2(MAXN + 1))
        acc = [0] * MAXL 
        def traverse(node, level):
            if node is None: 
                return level 
            ll = traverse(node.left, level + 1)
            rl = traverse(node.right, level + 1) 
            acc[level] += node.val
            # _v, _l = acc[level], level + 1
            # for v, l in [(lv, ll), (rv, rl)]: 
            #     if v > _v: 
            #         _v = v 
            #         _l = l 
            #         print(_v, _l)
            return max(ll, rl)
        
        # print(traverse(root, 0))
        maxl = traverse(root, 0)
        # print(maxl)
        # print(acc[:10])
        ret = 0 
        for i in range(maxl): 
            if acc[i] > acc[ret]: 
                ret = i 
        return ret + 1
    
if __name__ == "__main__": 
    root = [1,7,0,7,-8,None,None]
    root = [989,None,10250,98693,-89388,None,None,None,-32127]
    r = Solution().build(root)
    Solution().traverse(r)
    ret = Solution().maxLevelSum(r)
    print()
    print(ret)