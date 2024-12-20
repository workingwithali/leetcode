class NodeTree:
    def __init__(self,val = 0,right = None,left = None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def lca(self,root,p,q):
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val<root.val:
                root = root.left
            else:
                return root
            

solution = Solution()
result = solution.lca()
