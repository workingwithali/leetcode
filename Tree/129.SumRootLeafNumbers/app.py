class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
        
class Solution:
    def sum(self,root):
        def dfs(root,sum):
            if not root:
                return 0
            num = num*10+root.val
            if not root.left and not root.right:
                return sum
            return (dfs(root.left,sum)+dfs(root.right,sum))
        return dfs(root,0)
