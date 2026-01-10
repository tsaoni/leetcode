from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        subr, subl = root, 0
        def get_root(node, level): 
            nonlocal subr, subl
            if node is None: 
                return -1
            else: 
                ll = get_root(node.left, level + 1)
                rl = get_root(node.right, level + 1)
                curl = level if ll < 0 and rl < 0 else max(ll, rl) 
                if ll == rl: 
                    if curl >= subl: 
                        subl = curl 
                        subr = node
                
                return curl
        get_root(root, 0)

        return subr
        # def getv(node): 
        #     _q = []
        #     q = [node]
        #     ret = []
        #     while len(q) > 0: 
        #         for x in q:
        #             ret.append(x.val if x is not None else None)
        #             if x:
        #                 _q += [x.left, x.right]
        #         while len(_q) > 0 and _q[-1] is None: 
        #             _q.pop(-1)
        #         q = _q 
        #         _q = []
        #     return ret
        # return getv(subr)