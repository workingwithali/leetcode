class TreeNode:
    def __init__(self,val=0,right=None,left=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def insert(self,root,val):
        if not root :
            return TreeNode(val)
        if val > root.val:
            root.right = self.insert(root.right,val)
        else:
            root.right = self.insert(root.right,val)