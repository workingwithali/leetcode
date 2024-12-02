class TreeNode:
    def __init__(self,val=0,left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree(self, root):
        res = []
        def preorder(root):
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res
    
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
Solution = Solution()
r = Solution.tree(root)
print(r)
