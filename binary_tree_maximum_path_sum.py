from typing import Optional
import numpy as np 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_path_sum(self, root): 
        if root is None:
            return 0, 0
        elif root.left is None and root.right is None: # leaf 
            return root.val, root.val
        root_max_lst, max_lst = [0], []
        if root.left:
            l_root_max, l_max = self.max_path_sum(root.left)
            root_max_lst += [l_root_max]
            max_lst += [l_max]
        if root.right:
            r_root_max, r_max = self.max_path_sum(root.right)
            root_max_lst += [r_root_max]
            max_lst += [r_max]

        root_max = max(root_max_lst) + root.val
        cur_max = max(root_max, *max_lst, root.val + sum(root_max_lst))
        return root_max, cur_max

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, ret = self.max_path_sum(root)
        return ret
    
if __name__ == "__main__": 
    def build_test_case(inputs): 
        cnt = 1
        while True: 
            cur = []
            start = 2 ** (cnt - 1) - 1
            end = min(2 ** cnt - 2, len(inputs) - 1)
            if start == 0: 
                root = TreeNode(inputs[start], None, None)
                cur = [root]
            else: 
                for i in range(start, end + 1): 
                    cur += [TreeNode(inputs[i], None, None) if inputs[i] else None]
                # link with parents 
                for j, p in enumerate(cur): 
                    p_idx = int(j / 2)
                    if j % 2 == 0: # left 
                        parent[p_idx].left = p 
                    else: # right
                        parent[p_idx].right = p
            parent = cur
            cnt += 1
            if end == len(inputs) - 1:
                break
        return root
    
    inputs = [2, -1]
    #[-10,9,20,None,None,15,7]
    test_case = build_test_case(inputs)
    ret = Solution().maxPathSum(test_case)
    print(ret)