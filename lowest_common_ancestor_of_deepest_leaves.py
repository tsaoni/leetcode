from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def find_lca(root, depth): 
            if root == None: 
                return None, -1
            
            lroot, ld = find_lca(root.left, depth + 1)
            rroot, rd = find_lca(root.right, depth + 1)
            if lroot == None and rroot == None: 
                return root, depth 
            # elif len(lcands) == 0: 
            #     return rcands, rd 
            # elif len(rcands) == 0: 
            #     return lcands, ld 
            else: 
                if ld == rd: 
                    return root, ld
                elif ld > rd: 
                    return lroot, ld
                else: 
                    return rroot, rd
    
        return find_lca(root, 0)[0]
    
if __name__ == "__main__": 
    
    ret = Solution().lcaDeepestLeaves()
    print(ret)