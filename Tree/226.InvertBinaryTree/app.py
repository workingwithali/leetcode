class TreeNode:
    def __init__(self,val=0,right=None,left=None) -> None:
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invert(self,root):
        if not root:
            return None
        