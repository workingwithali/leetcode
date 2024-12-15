class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def path(self, root , targeSum):
        def helper(root, curSum):
            if not root :
                return False
            curSum += targeSum
            if not root.left and not root.right:
                return 
