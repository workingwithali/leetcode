class NodeTree:
    def __init__(self,val = 0 , left = None ,right = None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def boolen(self,root):
        if not root.left:
            return root.val == 1
        