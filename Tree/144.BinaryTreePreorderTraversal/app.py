class TreeNode:
    def __init__(self,val=0,left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class solution:
    def preorder(self, root):
        res = []
        def preorder(root):
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
    
solution = solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
r = solution.preorder(root)
print(r)
