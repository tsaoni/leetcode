from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lst = []
        def dfs(node): 
            if node is not None:
                dfs(node.left)
                lst.append(node.val)
                dfs(node.right)
        dfs(root)

        def build(start, end): 
            if start > end: 
                return None 
            mid = (start + end + 1) // 2
            l = build(start, mid - 1)
            r = build(mid + 1, end)
            root = TreeNode(lst[mid], l, r)
            return root 
        ret = build(0, len(lst) - 1)
        return ret