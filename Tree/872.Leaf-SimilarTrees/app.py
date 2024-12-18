class NodeTree:
    def __init__(self,val = 0 ,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def similar(self,root1,root2):
        def leaf(root,leaf):
            if not root:
                return
            if not root.left and not root.right:
                leaf.append(root.val)
                return

        leaf1,leaf2 =[],[]
        leaf(root1,leaf1)
        leaf(root2,leaf2)
        return leaf1 == leaf2