# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ret = root
        start = min([p, q], key=lambda x: x.val)
        end = max([p, q], key=lambda x: x.val)
        while True: 
            if ret.val < start.val: 
                ret = ret.right 
            elif ret.val > end.val: 
                ret = ret.left 
            else:
                return ret 
    
    
if __name__ == "__main__": 
    def build_test_case(inputs): 
        idx = 0 
        
        return 
    inputs = [6,2,8,0,4,7,9,None,None,3,5]
    test_case = build_test_case(inputs)
    Solution().lowestCommonAncestor()