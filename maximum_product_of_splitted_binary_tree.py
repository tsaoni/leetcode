from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def get_sum(node):
            if node is None: 
                return 0 
            node.sum = get_sum(node.left) + get_sum(node.right) + node.val
            return node.sum
        
        s = get_sum(root)
        mid = s / 2 
        _get_node_sum = lambda x: x.sum if x else 0 
        def get_mid(node): 
            if node is None: 
                return 0
            l = s - _get_node_sum(node.left)
            r = s - _get_node_sum(node.right)
            bst = 0
            lv = get_mid(node.left)
            rv = get_mid(node.right)
            for x in [l, r, lv, rv]: 
                if abs(x - mid) < abs(bst - mid): 
                    bst = x 
            return bst

        modulo = 10 ** 9 + 7 
        bst = get_mid(root)
        return (bst % modulo) * ((s - bst) % modulo) % modulo

    
if __name__ == "__main__": 
    Solution().maxProduct