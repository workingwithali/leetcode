class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def MergeTree(self,root1,root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root.lef