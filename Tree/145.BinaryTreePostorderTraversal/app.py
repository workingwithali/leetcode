class TreeNode:
    def __init__(self,val=0,left= None, right=None) -> None:
        self.val = val
        self.left = left
        self.right =right
class Solution:
    def tree(self,root):
        res=[]
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)
        postorder(root)
        return res