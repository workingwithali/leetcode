class TreeNode:
    def __init__(self,val = 0,right = None,left=None):
        self.val =val
        self.left = left
        self.right = right

class Solution:
    def symmetric(self,root):
        def hepler(rootL,rootR):
            if not rootL and not rootR:
                return True
            if not rootL or rootR:
                return False
            return (rootL.val == rootR and hepler(rootL.left,rootR.right)and hepler(rootL.right,rootR.left))
        return hepler(root.left,root.rigth)
