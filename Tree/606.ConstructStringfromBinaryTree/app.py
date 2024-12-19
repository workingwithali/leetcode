class NodeTree:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def string(self,root):
        res = []
        def preorder(root):
            if not root:
                return
            res.append("(")
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
            res.append(")")
    
    
    
        return "".join(res)[1:-1]
