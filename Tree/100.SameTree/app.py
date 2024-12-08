class Tree:
    def __init__(self,val=0,left= None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSame(self,p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSame(p.left,q.left) and self.isSame(p.right,q.right)
        