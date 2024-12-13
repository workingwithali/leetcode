class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def sortArray(self,nums):
        def helper(l,r):
            if l>r:
                return None
            