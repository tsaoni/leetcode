from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ret = []
        ptns = [None] * n 
        def all_patterns(start, end): 
            if start == end: 
                return [None]
            else: 
                ret = []
                for i in range(start, end): 
                    llst = all_patterns(start, i)
                    rlst = all_patterns(i + 1, end)
                    for lnode in llst: 
                        for rnode in rlst: 
                            node = TreeNode(val=i)
                            node.left = lnode 
                            node.right = rnode 
                            ret.append(node)
                return ret
            
        
        return all_patterns(1, n + 1) 
    
if __name__ == "__main__": 
    ret = Solution().generateTrees(n = 3)